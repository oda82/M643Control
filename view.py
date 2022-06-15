import tkinter as tk


class M643_view(tk.Frame):
    
    def __init__(self, window, ctrl):
        super().__init__(window)
        self.WIDTH = 10
        
        self.ctrl = ctrl #контроллет
        self.add_widgets()
        
    def add_widgets(self):
        
        #row 0 label
        self.lbl_status = tk.Label(self, text='Output I \n Out V \n Limit')
        self.lbl_status.grid(row=0, column=0)
                
        #row5 button connect disconnect
        self.btn_connect = tk.Button(self, text='Connect', width = self.WIDTH)
        self.btn_connect.grid(row=5, column=0)
        
        self.btn_disconnect = tk.Button(self, text='Disconnect', width=self.WIDTH) #, state='disabled'
        self.btn_disconnect.grid(row=5, column=1)
        #row6 Set ramp
        self.btn_set_ramp = tk.Button(self, text='Ramp Rate', width=self.WIDTH)
        self.btn_set_ramp.grid(row=6, column=0)
        
        self.ent_ramp = tk.Entry(self, width=self.WIDTH)
        self.ent_ramp.grid(row=6, column=1)
        #row7 Set I
        self.btn_set_i = tk.Button(self, text='Set I', width=self.WIDTH)
        self.btn_set_i.grid(row=7, column=0)
        
        self.ent_i = tk.Entry(self, width=self.WIDTH)
        self.ent_i.grid(row=7, column=1)
        #row8 Set zero stop
        self.btn_set_zero = tk.Button(self, text='Set zero', width=self.WIDTH)
        self.btn_set_zero.grid(row=8, column=0)
        
        self.btn_stop = tk.Button(self, text='Stop', width=self.WIDTH)
        self.btn_stop.grid(row=8, column=1)
        
     


if __name__ == '__main__':
    window = tk.Tk()
    M643_view(window,None).pack()
    window.mainloop()