# -> Abstraction : Exposing only what users need and hiding the internal details

#     -> You define a Contract(What Must Be Done) and 
#         then let the different classes implement the details(How It's Done)
    
#     -> Abstraction Allows Developers to focus on What an Object Does, instead of how it does

# -> If we apply Abstraction

#     -> Hide The Complexity : Callers(Users) will rely on a simple interface 

#     -> Enforce Contracts : Subclasses must implement required functionalities 

# -> Taking Laptops As Scenario 

# -> To Implement Abstraction 

#     -> When we want python to enforce Subclasses implement certain functionalities/Contracts

#         -> We use Abstract Base Class (abc module)
#         -> We Define Abstract Methods using @abstractmethod

#     -> NOTE : To achieve Abstraction use abc module

# NO Abstraction - We used regular / concrete classes
class Laptop():
    def usb_slot(self):
        pass
    def hdmi_slot(self):
        pass
    def c_port(self):
        pass

class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo USB Slot")
    def hdmi_slot(self):
        print("Lenovo HDMI Slot")

class Dell(Laptop):
    def usb_slot(self):
        print("Lenovo USB Slot")
    def c_port(self):
        print("Lenovo C Slot")
    
# User 
print("User Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.usb_slot()
lenovo.hdmi_slot()

print("User Buying Dell Laptop")
dell = Dell()
dell.usb_slot()
dell.c_port()