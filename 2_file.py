number=int(input ("Введите число"))
numbers = {0:"",1: "один", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять"}
ten = {0:"",10: "десять",11:"одиннадцать", 12:"двенадцать",13: "тринадцать", 14:"четырнадцать", 15:"пятнадцать",
            16: "шестнадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать"}
tens = {0:"", 1:"десять", 2:"двадцать", 3:"тридцать", 4:"сорок", 5:"пятьдесят", 6:"шестьдесят",
           7: "семьдесят", 8:"восемьдесят", 9:"девяносто"}
hundreds = {0:"", 1:"сто", 2:"двести", 3:"триста", 4:"четыреста", 5:"пятьсот", 6:"шестьсот",
                7:"семьсот", 8:"восемьсот", 9:"девятьсот"}
while number<1 or number>999:
    number=int(input("enter number from 1 to 999"))

k1=number//100

k1 = hundreds.get(k1)

k2=number%100

if k2 in ten.keys():
    k2 =ten.get(k2)
    print(k1 + ' ' + k2)
else:
    k2=k2//10
    k2 = tens.get(k2)
    k3=number%10
    k3=numbers.get(k3)
    print(k1 + " "+ k2+ " "+ k3)