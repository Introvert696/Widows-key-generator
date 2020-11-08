import string
import random


#   GWJCG-7C73B-JV8MR-F7GWJ-MCYYG  5 символов 5 строк
def randomLater():
    letTemp = random.choice(string.ascii_uppercase)
    return letTemp


def randomKey():
    i=1
    keyArray=[]
    while i < 26:
        tempLet = randomLater()
        keyArray.append(tempLet)
        if i == 5 or i == 10 or i == 15 or i ==20:
            keyArray.append('-')

        i +=1
    goodKey = ''.join(keyArray)
    # print(goodKey)
    return goodKey


def WriteKey():
    f = open('text.txt', 'a')
    quantity = int(input("Введите количество ключей: "))
    b = 0
    while b < quantity:
        # print("hello")
        f.write(randomKey() + '\n')
        b+=1
    f.close()
# lat = randomLater()
# print(lat)
# randomKey()
WriteKey()
