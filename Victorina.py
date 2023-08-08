vopros = "Когда создали майнкрафт? (Самая первая версия)"

print(vopros + "\n")

otveti = ["2007", "2011", "2010", "2009"]

print("Пишите не цифру а ответ!\n")

print("1 - " + otveti[0])
print("2 - " + otveti[1])
print("3 - " + otveti[2])
print("4 - " + otveti[3])

verniyotvet = otveti[3]

otvet = str(input("Ответ: "))

if(otvet == verniyotvet):
    print("Верно! Удачи вам!")
else:
    print("Вы не угадали(")
