from math import degrees

import numpy
import numpy as np
#Tehtävät 1.1, s 8-9
#1 a) ja b)
a = 2.493
b = 0.911
print("Teht. 1 a) ja b)")
print(np.degrees(a))
print(np.degrees(b))
print("--" * 15)

#2 a) ja b)
print("Teht. 2 a) ja b)")
print(np.radians(137.7))
print(np.radians(62.3))
print("--" * 15)

print("Teht. 3")
#3 taulukko
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
for i in A:
    print(np.radians(i))
print("--" * 15)

#Tehtävät 2.2.1, s.20
#1
print("Teht. 2.1")
c = 1.6
d = 2.3
print(numpy.hypot(c, d))