from lakeshore import Model643
from time import sleep
import threading

class M643_thread(threading.Thread):
    #передать объект модели для обратной связи
    def __init__(self, model):
        super().__init__()
        self.stop = False
        self.m643 = model.m643
        self._lock = threading.Lock() #.acquire() .release() with self._lock:
        self.model = model
    
    def set_i(self, i):
        #установить ток магнита 0.0000 - ±70.1000A        
        with self._lock:
            self.m643.command('SETI {}'.format(i))
            
    def set_zero(self):
        #установить ток магнита в 0       
        with self._lock:
            self.m643.command('SETI 0')
            
    def set_stop(self):
        #остановить изменение тока магнита в течении 2сек
        with self._lock:
            self.m643.command('STOP')
        
        
    def set_rate_i(self, i):
        #установить скорость изменения тока магнита 0.0001 A/s through 50.000 A/s.
        with self._lock:
            self.m643.command('RATE {}'.format(i))
    
    def set_limit(self, i, rate):
        #установить ограничения тока и скорости изменения тока магнита
        with self._lock:
            self.m643.command('LIMIT {},{}'.format(i,rate))
            
    def set_intwtr(self,i=2):
        #управление водой источника питания 0 = Manual Off, 1 = Manual On, 2 = Auto, 3 = Disabled
        with self._lock:
            self.m643.command('INTWTR {}'.format(i))
    
    def set_magwtr(self,i=2):
        #управление водой магнита 0 = Manual Off, 1 = Manual On, 2 = Auto, 3 = Disabled
        with self._lock:
            self.m643.command('MAGWTR {}'.format(i))
            
    def run(self):
        print(self.stop, self.m643)
        #если прибор подключен и поток работает
        while not self.stop and self.m643:
            with self._lock:
                #read m643 --> write model
                self.model.out_i = self.m643.query('RDGI?').rstrip()
                self.model.out_v = self.m643.query('RDGV?').rstrip()
                self.model.lim_i, self.model.lim_rate = self.m643.query('LIMIT?').rstrip().split(',')
                self.model.set_i = self.m643.query('SETI?').rstrip()
                self.model.rate_i = self.m643.query('RATE?').rstrip()
                #send commands
                
                #model.update_data()
            if self.model.update_data:
                self.model.update_data()
            sleep(1) #поменять на меньшее время
        
    
class Model:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.out_i = ''
        self.out_v = ''
        self.lim_i = ''
        self.lim_rate = ''
        self.set_i = ''
        self.rate_i = ''
        self.id ='disconnect'
        self.update_data = None
    
    def connect_m643(self):
        #подключить прибор и считать номер
        try:
            self.m643 = Model643()
            self.id = self.m643.query('*IDN?')
        except:
            self.m643 = None
            print('Не удалось подключиться к Model 643')
        #запустить покот считывания данных с прибора
        self.start_thread()
        
    def disconnect_m643(self):
        #stop thread m643
        self.stop_thread()
        #отключить прибор
        self.m643.disconnect_usb()
        self.id ='disconnect'
        
    
    def start_thread(self):
        # создать поток считывания с прибора и запустить его
        if self.m643:
            self.m643_thread = M643_thread(self)
            self.m643_thread.start()
        else:
            print('поток не запущен')
        
    def stop_thread(self):
        #остановить поток
        self.m643_thread.stop = True
        self.m643_thread.join() #дождаться завершения потока
        self.m643_thread.stop = False
        
#     def update_data(self):
#         #прописать сюда метод контролера для обновления данных в отображении
#         print('update_data')
#         #print( self.out_i, self.out_v, self.lim_i, self.lim_rate, self.set_i, self.rate_i, self.id)
if __name__ == '__main__':
    model = Model()