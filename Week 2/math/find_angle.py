import math

AB = int(input())
BC = int(input())
temp = math.atan2(AB,BC)
temp = round(math.degrees(temp))
print(temp,chr(176),sep="")