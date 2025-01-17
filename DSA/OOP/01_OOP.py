def gcd(m, n): #The best-known algorithm for finding the greatest common divisor is Euclid’s algorithm. It states that the greatest common divisor of two integers m and n is n if n divides m evenly. However, if n does not divide m evenly, then the answer is the greatest common divisor of n and the remainder of m divided by n. 
    while m % n != 0:
        m, n = n, m % n # m, n = n, m % n is essentially swapping the values of m and n while also calculating the remainder of m divided by n. 
        # m2 = m
        # m = n
        # n = m2 % n 
      
    return n

class Fraction:
    def __init__(self, top, bottom): #constructor method
            self.num = top
            self.den = bottom
                

    def __str__(self):
        cmmn = gcd(self.num, self.den)
        return f"{self.num//cmmn}/{self.den//cmmn}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        
        return Fraction(new_num , new_den )
    
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num,new_den)
    
    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

x = Fraction(4, 18)
x.show()
y = Fraction(6, 24)
print(y)#same as print(y.__str__())
print(x + y) #same as print(x.__add__(y)). 1/2 is 'self' in __add__, 2/3 is 'other_fraction'
print(x - y) 
print(x * y)
print(x / y)
print(x == y)





class LogicGate:

    def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic() # type: ignore
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter pin A input for gate " + self.get_label() + ": "))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
class NandGate(AndGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class NorGate(OrGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):

    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())

main()

