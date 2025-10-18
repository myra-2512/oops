class a:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
            if(self.a<other.a):
                return ("ob1 is less than ob2")
            else:
              return ("ob1 is greater than ob2")
    def __eq__(self,other):
        if(self.a==other.a):
            return ("ob1 is equal to ob2")
        else:
            return ("ob1 is not equal to ob2")

ob1=a(2)
ob2=a(3)
print(ob1<ob2)

ob1=a(4)
ob2=a(4)
print(ob1==ob2)