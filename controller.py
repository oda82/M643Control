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
        pass
    
    def connect(self, evnt):
        self.model.connect_m643()
        
    def disconnect(self, evnt):
        self.model.disconnect_m643()
    
    def set_i(self, evnt):
        i = float(self.view.ent_i.get())
        self.model.m643.set_i(i)
        
    def set_zero(self, evnt):
        self.model.m643.set_zero()
        
    def set_ramp(self, evnt):
        i = float(self.view.ent_ramp.get())
        self.model.m643.set_rate_i(i)

    def set_stop(self, evnt):
        self.model.m643.set_stop()
        
    
    def update_view(self):
        s = 'Serial number: {}\n Output I: {}\n Output V: {}\n Limit I: {}\n Limit Rate: {}\n Set I: {}\n Set Rate: {}'
        .format(self.model.id, self.model.out_i, self.model.out_v, self.model.lim_i, self.model.lim_rate, self.model.set_i, self.model.rate_i)
        print(s)
        self.view.lbl_status.set(s)
        pass
        



if __name__ == '__main__':
   
    ctrl = Controller()
    