import tkinter as tk
from model import Model
from main_window import MainWindow


class Controller:
    def __init__(self, model, view):
        #подключение моделей устройств
        self.model = model
        self.model.update_data = self.update_view # оппределить калбэк при обновлении модели
        #подключение отображений
        self.view = view 

        #связать управление в отображении
        self.bind_view()

    
    def bind_view(self):
        self.view.btn_connect.bind("<Button-1>", self.connect)
        self.view.btn_disconnect.bind("<Button-1>", self.disconnect)
        self.view.btn_set_i.bind("<Button-1>", self.set_i)
        self.view.btn_set_zero.bind("<Button-1>", self.set_zero)
        self.view.btn_stop.bind("<Button-1>", self.set_stop)     
        self.view.btn_set_ramp.bind("<Button-1>",self.set_ramp)
        
        self.view.btn_set_limit_i.bind("<Button-1>", self.set_limit_i)
        self.view.btn_set_limit_rate.bind("<Button-1>", self.set_limit_rate)
        
        pass
    
    def connect(self, event):
        self.view.btn_disconnect.config(state ='normal')
        self.view.btn_connect.config(state='disabled')
        
        self.model.connect_m643(start_thread = True)
  
    def disconnect(self, event):
        self.view.btn_disconnect.config(state ='disabled')
        self.view.btn_connect.config(state='normal')
        
        print('set disconnect')
        self.model.disconnect_m643()
        print('disconnected')
    
    def set_i(self, event):
        i = float(self.view.var_cbox_set_i.get())
        self.model.set_i(i)
        
    def set_zero(self, event):
        self.model.set_zero()
        
    def set_ramp(self, event):
        i = float(self.view.var_cbox_ramp.get())
        self.model.set_rate_i(i)

    def set_stop(self, event):
        #print('controller set_stop')
        self.model.set_stop()
    
    def set_limit_i(self, event):
        limit_i, limit_rate = self.model.get_limit()
        limit_i = self.view.var_cbox_limit_i.get()
        self.model.set_limit(limit_i, limit_rate)

    def set_limit_rate(self, event):
        limit_i, limit_rate = self.model.get_limit()
        limit_rate = self.view.var_cbox_limit_rate.get()
        self.model.set_limit(limit_i, limit_rate)




    def update_view(self):
        #Вывести состояние прибора на окно
#         s = ''
#         for key, value in self.model.m643_data.items():
#             s = s + key + ' : ' + value + '\n'
#         print(s)
        items = self.model.m643_data

        self.view.var_firmware_version.set(items['Firmware Version'])
        self.view.var_serial_number.set(items['Serial Number'])
        self.view.var_model_number.set(items['Model Number'])
        self.view.var_out_i.set(items['Output I'])
        self.view.var_out_v.set(items['Output V'])
        self.view.var_set_i.set(items['Set I'])
        self.view.var_rate.set(items['Rate'])
        self.view.var_limit_i.set(items['Limit I'])
        self.view.var_limit_rate.set(items['Limit Rate'])
        self.view.var_state.set(items['state'])
        self.view.var_ramp.set('')
        pass
        



if __name__ == '__main__':
    #подключение моделей устройств
    model = Model()
    #подключение отображений
    root = tk.Tk()
    root.title('Model 643 Controller')
    view = MainWindow(root)
    
    ctrl = Controller(model, view)
    
    root.mainloop()