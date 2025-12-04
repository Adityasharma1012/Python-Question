# Weather given number is prime or not
import sympy
a=list(map(int,input("Enter numbers separated by commas: ").split(",")))
d={}
for ch in a:
    if sympy.isprime(ch):
        d[ch]="prime"
    else:
        d[ch]="not prime"
print(d)
