import random

my_numbers = {6, 11, 18 , 23, 32 , 48}

drawn_numbers = set()

basic_numbers = set()

counter = 0

numeral = ""

i = int(1)

while i < 50 :
    basic_numbers.add(i)
    i+=1

print("Wszystkie liczby : "+ str(basic_numbers))

while int(len(drawn_numbers) < 6) :
    x = int(random.randrange(1,49))
    drawn_numbers.add(x)

print("Wylosowane liczby : " + str(drawn_numbers))
print("Moje liczby : " + str(my_numbers))

hited = drawn_numbers.intersection(my_numbers)

if len(hited) == 1 :
    numeral = "liczbę"
else :
    numeral = "liczby"

if len(hited) == 0 :
    hited = ""
    numeral = "liczb"

counter = len(hited)
if hited == False :
    counter = 0

print("Trafione liczby : " + str(hited))

print("Udało Ci się trafić : " + str(counter) + " " + numeral + " " + str(hited))
