def CelToFrh(Cel):
    return cel*(5/9)+32

cel=int(input("Enter celcious : "))
F=CelToFrh(cel)
print(F)