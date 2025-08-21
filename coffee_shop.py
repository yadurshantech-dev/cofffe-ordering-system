class coffee:
    name=""
    price=0
    index=0

green=coffee()
blue=coffee()
red=coffee()
yellow=coffee()


yellow.name="Cold Coffee"
yellow.price=2.50
yellow.index=1

blue.name="Hot Coffee"
blue.price=3.00
blue.index=2


red.name="Coffee"
red.price=4.20
red.index=3


green.name="Tea"
green.price=5.25
green.index=4

print("__________________________")
print("|Index|MENU"+"        |Price|")
print("|-----|------------|-----|")
print("|01   "+str()+"|"+yellow.name+" |"+str(float(yellow.price))+"  |")
print("|02   "+str()+"|"+blue.name+"  |"+str(float(blue.price))+"  |")
print("|03   "+str()+"|"+red.name+"      |"+str(float(red.price))+"  |")
print("|04   "+str()+"|"+green.name+"         |"+str(float(green.price))+" |")
print("--------------------------")
print()
print("Place the order!")
print("Instructions)")
print(">(Enter the index)")
print(">(After Order[Enter 5 to end])")
b=0.0
i=1
a=int(input(str(i)+":"))
while True:
    
    c=int(input("Quantity:"))
    if a==yellow.index:
        b=b+(yellow.price*c)
    elif a==blue.index:
        b=b+(blue.price*c)
    elif a==red.index:
        b=b+(red.price*c)
    elif a==green.index:
        b=b+(green.price*c)
    
    i=i+1
    a=int(input(str(i)+":"))
    if a==5:
        break


print("Total:"+str(b))
        
