class Rational:
    
    def __init__(self , n , d):
        self.n = n
        self.d = d
        self.num = n
        self.don = d
        self.__gcd__()
        self.__compact__()
    def __gcd__(self):
        if self.d == 0:
            return self.n
        else:
            temp = self.n
            self.n = self.d
            self.d = temp % self.d
            return self.__gcd__()
    def __str__(self):
        return str(self.num)+"/"+str(self.don)
    def __compact__(self):
        self.num = self.num / self.n
        self.don = self.don / self.n
    
    # def prints(self):
    #     print(self.num , " " , self.don)
    # def prints(self):
    #     print(self.num , " " , self.don)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.don + self.don*otherfraction.num
        newdon = self.don*otherfraction.don
        return Rational(newnum,newdon)
        


a = Rational(10 , 2)
b = Rational(11 , 2)

# a.__gcd__()
# b.__gcd__()
# a.__compact__()
# b.__compact__()

print(a + b)


    

    