class Model643:
    def __init__(self):
        self.firmware_version = 'firmware_version'
        self.serial_number = 'Serial Number'
        self.model_number = 'Model Number'
        
    def command(self, text):
        print('fake command Model643:'+text)
        
    def query(self, text):
        print('fake query Model643:'+text)
        return text+','+text
    
    def disconnect_usb(self):
        pass
    