import tkinter as tk

class MainWindow:
    
    def __init__(self, root, ctrl=None):
        
        self.root = root #ссылка на основное окно     
        self.ctrl = ctrl #контроллет
        
        self.add_monitor_widgets()
        self.add_control_widgets()
 
    def add_monitor_widgets(self):
        self.frm_monitor = tk.Frame(self.root)#, bg='yellow'
        self.frm_monitor.pack(fill='x', padx=3, pady=3)
        self.frm_monitor.columnconfigure(0, weight=1)
        self.frm_monitor.columnconfigure(1, weight=1)       
        tk.Label(self.frm_monitor, text='Firmware Version:').grid(row=0, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Serial number:').grid(row=1, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Model number:').grid(row=2, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Output I:').grid(row=3, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Output V:').grid(row=4, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Set I:').grid(row=5, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Rate:').grid(row=6, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Limit I:').grid(row=7, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Limit Rate:').grid(row=8, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='State:').grid(row=9, column=0, sticky='e')
        tk.Label(self.frm_monitor, text='Ramp:').grid(row=10, column=0, sticky='e')
        
        self.var_firmware_version = tk.StringVar()
        self.var_serial_number = tk.StringVar()
        self.var_model_number = tk.StringVar()
        self.var_out_i = tk.StringVar()
        self.var_out_v = tk.StringVar()
        self.var_set_i = tk.StringVar()
        self.var_rate = tk.StringVar()
        self.var_limit_i = tk.StringVar()
        self.var_limit_rate = tk.StringVar()
        self.var_state = tk.StringVar()
        self.var_ramp = tk.StringVar()
        
        tk.Label(self.frm_monitor, textvariable=self.var_firmware_version).grid(row=0, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_serial_number).grid(row=1, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_model_number).grid(row=2, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_out_i).grid(row=3, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_out_v).grid(row=4, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_set_i).grid(row=5, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_rate).grid(row=6, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_limit_i).grid(row=7, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_limit_rate).grid(row=8, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_state).grid(row=9, column=1, sticky='w')
        tk.Label(self.frm_monitor, textvariable=self.var_ramp).grid(row=10, column=1, sticky='w')        
    
    def add_control_widgets(self):
        self.frm_control = tk.Frame(self.root)#, bg='red'
        self.frm_control.pack( fill='x', padx=3, pady=3)
        self.frm_control.columnconfigure(0, weight=1)
        self.frm_control.columnconfigure(1, weight=1)
        
        #row0 button connect disconnect
        self.btn_connect = tk.Button(self.frm_control, text='Connect')
        self.btn_connect.grid(row=0, column=0, sticky='ew', padx=3, pady=3)
        
        self.btn_disconnect = tk.Button(self.frm_control, text='Disconnect', state='disabled') #, state='disabled'
        self.btn_disconnect.grid(row=0, column=1, sticky='ew', padx=3, pady=3)
        
        #row1 Set I
        self.btn_set_i = tk.Button(self.frm_control, text='Set I')
        self.btn_set_i.grid(row=1, column=0, sticky='ew', padx=3, pady=3)
        
        self.var_cbox_set_i = tk.StringVar()
        values_set_i = ('0','1','2','3','4','5','6','7','8','9','10','15','20','25','30','40','50')
        self.cbox_set_i = tk.ttk.Combobox(self.frm_control, width=5, textvariable= self.var_cbox_set_i, values=values_set_i)
        self.cbox_set_i.current(0)
        self.cbox_set_i.grid(row=1, column=1, sticky='ew', padx=3, pady=3)
        
        #row2 Set zero stop
        self.btn_set_zero = tk.Button(self.frm_control, text='Set zero')
        self.btn_set_zero.grid(row=2, column=0, sticky='ew', padx=3, pady=3)
        
        self.btn_stop = tk.Button(self.frm_control, text='Stop')
        self.btn_stop.grid(row=2, column=1, sticky='ew', padx=3, pady=3)
        
        #row3 Set ramp
        self.btn_set_ramp = tk.Button(self.frm_control, text='Ramp Rate')
        self.btn_set_ramp.grid(row=3, column=0, sticky='ew', padx=3, pady=3)
        
        self.var_cbox_ramp = tk.StringVar()
        values_ramp = ('1','2','3','4','5','6','7','8','9','10')
        self.cbox_ramp = tk.ttk.Combobox(self.frm_control, width=5, textvariable= self.var_cbox_ramp, values=values_ramp)
        self.cbox_ramp.current(0)
        self.cbox_ramp.grid(row=3, column=1, sticky='ew', padx=3, pady=3)
        
        #row4 set limit i 
        self.btn_set_limit_i = tk.Button(self.frm_control, text='Set Limit I')
        self.btn_set_limit_i.grid(row=4, column=0, sticky='ew', padx=3, pady=3)
        
        self.var_cbox_limit_i = tk.StringVar()
        values_limit_i = ('10','20','30','40','50','60','70')
        self.cbox_limit_i = tk.ttk.Combobox(self.frm_control, width=5, textvariable= self.var_cbox_limit_i, values= values_limit_i)
        self.cbox_limit_i.current(0)
        self.cbox_limit_i.grid(row=4, column=1, sticky='ew', padx=3, pady=3)
        
        #row5 set limit rate 
        self.btn_set_limit_rate = tk.Button(self.frm_control, text='Set Limit rate')
        self.btn_set_limit_rate.grid(row=5, column=0, sticky='ew', padx=3, pady=3)
        
        self.var_cbox_limit_rate = tk.StringVar()
        values_limit_rate = ('1','2','3','4','5','6','7')
        self.cbox_limit_rate = tk.ttk.Combobox(self.frm_control, width=5, textvariable= self.var_cbox_limit_rate, values= values_limit_rate)
        self.cbox_limit_rate.current(0)
        self.cbox_limit_rate.grid(row=5, column=1, sticky='ew', padx=3, pady=3)
        
 
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Model 643 Controller')
    main_window = MainWindow(root)
    root.mainloop()

