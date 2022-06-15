class Model643:
    def command(self, text):
        print('fake command Model643:'+text)
        
    def query(self, text):
        print('fake query Model643:'+text)
        return text+','+text
    
    def disconnect_usb(self):
        pass
    