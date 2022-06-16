import tkinter as tk
from model import Model
from view import M643_view


class Controller:
    def __init__(self):
        #подключение моделей устройств
        self.model = Model(self)
        self.model.update_data = self.update_view # оппределить калбэк при обновлении модели
        #подключение отображений
        self.window = tk.Tk()
        self.window.title('Model 643 Controller')
        self.view = M643_view(self.window, self)
        self.view.pack()
        #связать управление в отображении
        self.bind_view()
        self.window.mainloop()
    
    def bind_view(self):
        self.view.btn_connect.bind("<Button-1>", self.connect)
        self.view.btn_disconnect.bind("<Button-1>", self.disconnect)
        self.view.btn_set_ramp.bind("<Button-1>",self.set_ramp)
        self.view.btn_set_i.bind("<Button-1>", self.set_i)
        self.view.btn_set_zero.bind("<Button-1>", self.set_zero)
        self.view.btn_stop.bind("<Button-1>", self.set_stop)
        self.view.btn_set_limit.bind("<Button-1>", self.set_limit)
        pass
    
    def connect(self, event):
        #print('controller connect 1')
        self.model.connect_m643(start_thread = True)
        #print('controller connect 2')
        
    def disconnect(self, event):
        #print('discontroller connect 1')
        self.model.disconnect_m643()
        #print('discontroller connect 2')
    
    def set_i(self, event):
        i = float(self.view.ent_i.get())
        self.model.set_i(i)
        
    def set_zero(self, event):
        self.model.set_zero()
        
    def set_ramp(self, event):
        i = float(self.view.ent_ramp.get())
        self.model.set_rate_i(i)

    def set_stop(self, event):
        print('controller set_stop')
        self.model.set_stop()
    
    def set_limit(self, event):
        i, rate = self.view.ent_limit.get().split(',')
        self.model.set_limit(int(i), int(rate))
    
    def update_view(self):
        #Вывести состояние прибора на окно
        s = ''
        for key, value in self.model.m643_data.items():
            s = s + key + ' : ' + value + '\n'
        print(s)
        self.view.lbl_status['text'] = s
        pass
        



if __name__ == '__main__':
   
    ctrl = Controller()
    