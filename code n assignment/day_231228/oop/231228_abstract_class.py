from abc import ABC,abstractmethod
# ABC: Abstract Base Class
class BankPins(ABC):
    pin1 = 1234
    pin2 = 3434

    @abstractmethod
    def policies(self): # abstract method
        pass

    def RBI_rules(self): # non-abstract method
        pass
#b = BankPins()
# we are not allowed to create
# object of an abstract class