import math

so_lang = -1 
print("before", so_lang)
for num in [21,12,22,1,26,78,90,43,21,11,10,45,39]:
    if num > so_lang:
        so_lang = num
    print(so_lang, num)

print("After", so_lang)

zork = 0 
print("Before", zork)
for things in range(30):
    zork = zork + 1
    print(zork, things)

print("After", zork)

count = 0 
sum = 0 
print("Before", count, sum)
for value in range(20):
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count) 

smallest = None
print("Before")
for num in range(30):
    if smallest is None:
        smallest = num
    elif num < smallest:
        print(smallest, num)
print("After", smallest)

toal = 'banana'
rekn = 0 
for rek in toal:
    if rek == 'a':
        rekn = rekn + 1
print(rekn)

texta = "Malakanamabafaeakalaoana"
tiro = 0 
print("Before")
for tir in texta:
    if tir == 'a':
        tiro = tiro + 1
print(tiro)

