weather=(0,1,0,0,1,1)
rainy=0
sunny=0
for i in weather:
    if i==1:
        rainy+=1
    else:
        sunny+=1
print("Chance for raining is",rainy)
print("Chance for sunny is",sunny)
if sunny>rainy:
    print("the chance of the day being sunny is higher than rainy.")
elif rainy>sunny:
    print("the chance of the day being rainy is higher than sunny.")
else:
    print("The chances are equal,")
        