#modlülleri import etme
from sympy import *
import math
import sympy
import matplotlib.pyplot as plt
#Symbol variable oluşumu ve x**2'ni nintegrali
x= Symbol ('x')
expr= integrate(x**x, x)
#Bazı sayısal değerler
print(float(15))
print(Rational(0.3).limit_denominator(50))
A= Rational(7,7)
print(A)
print(Integer(7.11))
print(S.Zero)
#sin**2 ve cos**2 (x)'in toplamı ve bazı işlemler
expr2= sin(x)**2 + cos(x)**2
print(expr2)
print(sympify("3/4+7/5"))
y= Symbol('y')
eq= y**3 - 3
print(solve(eq, y))
print(sympy.sqrt(log(10,100)))
#z değişkeninin matplotlib'de parabolü, integral -tekrardan- ve  -oo'nun bulunuşu
z= x**2
plot(z)
print(integrate((x**2)))
print(((oo*-1)))
print(solve(eq**2==3),
#matplotlib'de plot grafik örneği
a1= [1200,1300,1400]
y1=[20,30,40]
a2=a1= [1200,1300,1400]
y2=[20,40,50]
plt.plot(a1,y1, marker=".", markersize="20", markerfacecolor="red" ,linestyle="dashed", markeredgecolor= "blue", linewidth="5", color="yellow")
plt.plot(a2,y2,marker=".", markersize="20", markerfacecolor="red" ,linestyle="dashed", markeredgecolor= "blue", linewidth="5", color="yellow")
plt.show()

