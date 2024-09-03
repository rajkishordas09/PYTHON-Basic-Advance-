class myClass():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
          x=self.a
          self.a+=2
          return x

i=myClass()
myIter=iter(i)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
