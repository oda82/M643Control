from lakeshore import Model643
from time import sleep
import threading
 
class M643_thread(threading.Thread):
    
    def __init__(self, model, fps=1):
        super().__init__()
        self.stop = False
        self.model = model # объект модели для обратной связи
        self.fps = fps #частота обновления данных с прибора
    
    def run(self):
        #print(self.stop, self.model.m643)
        #если прибор подключен и поток работает
        while not self.stop and self.model.m643:
            #read m643 --> write model
            self.model.get_out_i()
            self.model.get_out_v()
            self.model.get_limit()
            self.model.get_set_i()
            self.model.get_rate_i()
            # если задана функция обновления то вызвать    
            if self.model.update_data:
                self.model.update_data()
            sleep(1 / self.fps) #поменять на меньшее время
        
    
class Model:
    def __init__(self, ctrl=None):
        self.ctrl = ctrl #pointer to controler
        
        self.update_data = None  #указатель на метод для обновления данных
        
        self.m643 = None # pointer to Model643 module
        self.m643_delay = 0.05 #задержка между командами 5.3.5 Message Flow Control
        self.m643_data = {} #данные полученные с прибора
        
        # параметры потока считывания данных с прибора
        self.m643_thread = None #поток для получения данных с прибора
        self._lock = threading.Lock() #.acquire() .release() with self._lock:
       
    
    def connect_m643(self, start_thread = False):
        #подключить прибор и считать номер
        try:
            self.m643 = Model643()
            self.get_id()
            
            self.m643_data['Firmware Version'] = self.m643.firmware_version
            self.m643_data['Serial Number'] = self.m643.serial_number
            self.m643_data['Model Number'] = self.m643.model_number
            
            self.m643_data['state'] ='connected'
        except:
            self.m643 = None
            print('Не удалось подключиться к Model 643')
        #запустить покот считывания данных с прибора
        if start_thread:
            self.start_thread()
        
    def disconnect_m643(self):
        # отключить прибор
        #stop thread m643
        print('stoping thread')
        if self.m643_thread:
            self.stop_thread()
        print('thread stopped')
        #отключить прибор
        
        if self.m643:
            self.m643.disconnect_usb()
            self.m643 = None
            self.m643_data['state'] ='disconnected'
        print('usb disconnected')
    
    def start_thread(self, fps=1):
        # создать поток считывания с прибора и запустить его
        if self.m643:  #если прибор подключен запустить поток считывания
            self.m643_thread = M643_thread(self, fps)
            self.m643_thread.start()
        else:
            self.m643_thread = None
            print('поток не запущен')
        
    def stop_thread(self):
        #остановить поток
        self.m643_thread.stop = True
        self.m643_thread.join() #дождаться завершения потока
        self.m643_thread.stop = False
        self.m643_thread = None
        
    #import frpm M643_thread
    # m643 commands
    def set_i(self, i):
        #установить ток магнита 0.0000 - ±70.1000A        
        with self._lock:
            self.m643.command('SETI {}'.format(i))
            sleep(self.m643_delay)
            
    def set_zero(self):
        #установить ток магнита в 0       
        with self._lock:
            self.m643.command('SETI 0')
            sleep(self.m643_delay)
            
    def set_stop(self):
        #остановить изменение тока магнита в течении 2сек
        with self._lock:
            self.m643.command('STOP')
            sleep(self.m643_delay)
        
    def set_rate_i(self, i):
        #установить скорость изменения тока магнита 0.0001 A/s through 50.000 A/s.
        with self._lock:
            self.m643.command('RATE {}'.format(i))
            sleep(self.m643_delay)
    
    def set_limit(self, i, rate):
        #установить ограничения тока и скорости изменения тока магнита
        with self._lock:
            self.m643.command('LIMIT {},{}'.format(i,rate))
            sleep(self.m643_delay)
            
    def set_intwtr(self,i=2):
        #управление водой источника питания 0 = Manual Off, 1 = Manual On, 2 = Auto, 3 = Disabled
        with self._lock:
            self.m643.command('INTWTR {}'.format(i))
            sleep(self.m643_delay)
    
    def set_magwtr(self,i=2):
        #управление водой магнита 0 = Manual Off, 1 = Manual On, 2 = Auto, 3 = Disabled
        with self._lock:
            self.m643.command('MAGWTR {}'.format(i))
            sleep(self.m643_delay)
            
    # m643 queries
    def get_id(self):
        #получить идентификатор прибора
        with self._lock:
            self.m643_data['Id'] = self.m643.query('*IDN?').rstrip()
            sleep(self.m643_delay)
        return self.m643_data['Id']
        
    def get_out_i(self):
        #получить текущий ток с прибора
        with self._lock:
            self.m643_data['Output I'] = self.m643.query('RDGI?').rstrip()
            sleep(self.m643_delay)
        return self.m643_data['Output I']
        
    def get_out_v(self):
        #получить текущее напряжение с прибора
        with self._lock:
            self.m643_data['Output V'] = self.m643.query('RDGV?').rstrip()
            sleep(self.m643_delay)
        return self.m643_data['Output V']
        
    def get_limit(self):
        #получить ограничения по току и скорости изменения тока с прибора
        with self._lock:
            self.m643_data['Limit I'], self.m643_data['Limit Rate'] = self.m643.query('LIMIT?').rstrip().split(',')
            sleep(self.m643_delay)
        return self.m643_data['Limit I'], self.m643_data['Limit Rate']
    
    def get_set_i(self):
        #получить установленный ток с прибора
        with self._lock:
            self.m643_data['Set I'] = self.m643.query('SETI?').rstrip()
            sleep(self.m643_delay)
        return self.m643_data['Set I']
        
    def get_rate_i(self):
        #получить установленную скорость изменения тока с прибора
        with self._lock:
            self.m643_data['Rate'] = self.m643.query('RATE?').rstrip()
            sleep(self.m643_delay)
        return self.m643_data['Rate']
    
    def get_intwtr(self):
        #получить сотояние управление водой источника питания
        state = {0:'Manual Off', 1:'Manual On', 2:'Auto', 3:'Disabled'}
        with self._lock:
            self.m643_data['Internal Water'] =  state[ int(self.m643.query('INTWTR?').rstrip()) ]
            sleep(self.m643_delay)
        return self.m643_data['Internal Water']
    
    def get_magwtr(self):
        #олучить сотояние управление водой магнита
        state = {0:'Manual Off', 1:'Manual On', 2:'Auto', 3:'Disabled'}
        with self._lock:
            self.m643_data['Magnet Water'] =  state[ int(self.m643.query('MAGWTR?').rstrip()) ]
            sleep(self.m643_delay)
        return self.m643_data['Magnet Water']

                
if __name__ == '__main__':
    model = Model(None)
#     model.connect_m643()
#     print(model.get_id())
    