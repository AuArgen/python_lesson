# a = input("san jaz1 = ")
# b = input("san jaz2 = ")
# print( str(a) ,"+", str(b) ,"=" , str(a+b))

# int - bul butun sandar

# a = int(input("san jaz1 = "))
# b = int(input("san jaz2 = "))
# print( str(a) ,"+", str(b) ,"=" , str(a+b))

#float - bul anyk sandar (1.6, 5.5) 

# a = float(input("san jaz1 = "))
# b = float(input("san jaz2 = "))
# print( str(a) ,"+", str(b) ,"=" , str(a+b))

# МОЙ ВОЗРАСТ. Для заданого 0<=n<=200.Расматриваемого как возраст человека, вывести фразу вида: "Мне 21 год", "Мне 32 года"

n = int (input("Введите возраст: "))
print("мне " , n, end = " ")

if n % 10 == 1:
    print("год")
elif n % 10 >= 1 and n % 10 <= 4:
    print("года")
else:
    print("год")