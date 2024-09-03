def Star(n):
        if n==0:
            return
        print("*"*n)
        return Star(n-1)

n=4
star=Star(n)   