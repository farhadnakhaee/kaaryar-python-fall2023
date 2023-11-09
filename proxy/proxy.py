
from typing import Callable
class Proxy:
    last_invoked = ""
    call_history = {}

    def __init__(self, obj):
        self._obj = obj

    def last_invoked_method(self):
        pass

    def count_of_calls(self, method_name):
        pass

    def was_called(self, method_name):
        pass

    def __getattr__(self, name:str):
        print(self.__dir__())
        attr = self._obj.__getattribute__(name)
        if isinstance(attr,Callable):
            print("Its a callable")
        return attr
   
class Radio():   
    def __init__(self):        
        self._channel = None        
        self.is_on = False        
        self.volume = 0        

    def get_channel(self):        
        return self._channel    

    def set_channel(self, value):        
        self._channel = value        

    def power(self):        
        self.is_on = not self.is_on


radio = Radio()
radio_proxy = Proxy(radio)

print(dir(radio))
print(dir(radio_proxy))
# a = radio_proxy.is_on
# print(a)

