import time

print("Это игра с боями. Тебе надо будет нажимать на разные буквы чтобы отаковать врага. Надеюсь все понял :)")
time.sleep(3)
print(
    "Одним очень солнечным днем ты шёл домой. Когда ты был рядом с домом ты почувствовал себя плохо и ты отключился и упал на землю.")
time.sleep(6)
print(
    "Так ты и попал в другой мир.\nКогда ты очнулся то ты увидел короля людей. Вокруг тебя также стояли маги которые тебя призвали.")
time.sleep(6)
print(
    "Король тебе рассказал все об этом мире.\nНа данный момент у тебя есть лишь одна цель \"Одолеть короля троллей\" это он сказал перед тем как ты внезапно очутился перед троллем.")
time.sleep(8)
print(
    "Тебе нечего не оставалось кроме того чтобы бежать.\nТы убежал но увидел маленького мальчика и ты начал сражаться с противным троллем.")
time.sleep(6)
print("\n1 уровень. \nОдин тролль")

import random

ataka1 = 10
ataka2 = 15
hp = 100
hptroll = 50
t1 = 3
t2 = 0
troll1 = 1

while troll1 >= 1:

    hop = input("\nВаша атака будет \n z-атака кулаком \n x-атака ногой \n ")

    if hop == "z":
        hptroll = hptroll - ataka1
        print("Ты нанес " + str(ataka1) + " урона, у тролля осталось " + str(hptroll) + " здоровья")
    if hop == "x":
        a = random.randint(0, 100)
        if a >= 70:
            print("Ты к сожалению промахнулся")
        if a <= 69:
            hptroll = hptroll - ataka2
            print("Ты нанес " + str(ataka2) + " урона, у тролля осталось " + str(hptroll) + " здоровья")
    t1 = 0
    t2 = 3

    if hptroll <= 0:
        troll1 = troll1 - 1
        print("Ты убил тролля! Но...")

    at1 = random.randint(0, 1)

    if at1 == 0:
        hp = hp - ataka1
        time.sleep(1)
        print("Тролль нанес тебе " + str(ataka1) + " урона, у тебя осталось " + str(hp) + " здоровья")
    if at1 == 1:
        a = random.randint(0, 100)
        if a >= 70:
            time.sleep(1)
            print("Тролль к счастью промахнулся")
        if a <= 69:
            time.sleep(1)
            hp = hp - ataka2
            print("Тролль нанес тебе " + str(ataka2) + " урона, у тебя осталось " + str(hp) + " здоровья")

time.sleep(2)
print("Ты спас мальчика и отправился к замку людей.")
time.sleep(6)
print(
    "Тебе там дали доспех и меч и сказали что эти странные телепортации из-\nза ауры короля троллей и так уже пропали более 100 человек включая этого мальчика.")
time.sleep(6)
print("Так ты захотел остановить эти телепортации и маги тебя телепортировали к королю троллей.")
time.sleep(6)
print("Ты оказался возле двух элитных троллей охраняющих главного злодея.")
time.sleep(3)
print("Уровень 2. Два тролля")

hp = 150
ataka3 = 20
hptroll = 100
troll2 = 2

while troll2 >= 1:

    hop = input("\nВаша атака будет \n z-атака кулаком \n x-атака ногой \n c-атака мечом \n ")

    if hop == "z":
        hptroll = hptroll - ataka1
        print("Ты нанес " + str(ataka1) + " урона, у тролля осталось " + str(hptroll) + " здоровья")
    if hop == "x":
        a = random.randint(0, 100)
        if a >= 70:
            print("Ты к сожалению промахнулся")
        if a <= 69:
            hptroll = hptroll - ataka2
            print("Ты нанес " + str(ataka2) + " урона, у тролля осталось " + str(hptroll) + " здоровья")
    if hop == "c":
        a = random.randint(0, 100)
        if a >= 50:
            print("Ты к сожалению промахнулся")
        if a <= 49:
            hptroll = hptroll - ataka3
            print("Ты нанес " + str(ataka3) + " урона, у тролля осталось " + str(hptroll) + " здоровья")
    t1 = 0
    t2 = 3

    if hptroll <= 0:
        troll2 = troll2 - 1
        hptroll = 100
        print("Ты убил тролля! Но...")
    if hp <= 0:
        print("К сожалению ты умер. Больше нечего сказать...")
        time.sleep(2)
        print("Хотя ты можешь начать с самого начала ведь это просто игра...")
        time.sleep(3)
        print("Ведь так...")
        time.sleep(1)
        print("До нового старта человек сидящий за экраном.")
        time.sleep(2)
        quit()

    at1 = random.randint(0, 2)

    if at1 == 0:
        hp = hp - ataka1
        time.sleep(1)
        print("Тролль нанес тебе " + str(ataka1) + " урона, у тебя осталось " + str(hp) + " здоровья")
    if at1 == 1:
        a = random.randint(0, 100)
        if a >= 70:
            time.sleep(1)
            print("Тролль к счастью промахнулся")
        if a <= 69:
            time.sleep(1)
            hp = hp - ataka2
            time.sleep(1)
            print("Тролль нанес тебе " + str(ataka2) + " урона, у тебя осталось " + str(hp) + " здоровья")
    if at1 == 2:
        a = random.randint(0, 100)
        if a >= 50:
            time.sleep(1)
            print("Тролль к счастью промахнулся")
        if a <= 49:
            time.sleep(1)
            hp = hp - ataka3
            print("Тролль нанес тебе " + str(ataka3) + " урона, у тебя осталось " + str(hp) + " здоровья")

print("У тебя осталось довольно мало здоровья.\nУ тебя было от магов волшебное зелье которое тебя могло немного но вылечить.")
time.sleep(5)
hp = hp + 85
print("Ты его выпил и теперь у тебя " + str(hp) + " здоровья.")
time.sleep(3)
print("Ты открываешь дверь к королю троллей. Он тебя замечает и ты вступаешь с ним в бой.")

hptroll = 500
troll3 = 1

while troll3 >= 1:

    hop = input("\nВаша атака будет \n z-атака кулаком \n x-атака ногой \n c-атака мечом \n ")

    if hop == "z":
        hptroll = hptroll - ataka1
        print("Ты нанес " + str(ataka1) + " урона, у короля троллей осталось " + str(hptroll) + " здоровья")
    if hop == "x":
        a = random.randint(0, 100)
        if a >= 70:
            print("Ты к сожалению промахнулся")
        if a <= 69:
            hptroll = hptroll - ataka2
            print("Ты нанес " + str(ataka2) + " урона, у короля троллей осталось " + str(hptroll) + " здоровья")
    if hop == "c":
        a = random.randint(0, 100)
        if a >= 50:
            print("Ты к сожалению промахнулся")
        if a <= 49:
            hptroll = hptroll - ataka3
            print("Ты нанес " + str(ataka3) + " урона, у короля троллей осталось " + str(hptroll) + " здоровья")
    t1 = 0
    t2 = 3

    if hptroll <= 0:
        troll3 = troll3 - 1
        hptroll = 100
        print("Ты убил тролля! Но...")
    if hp <= 0:
        print("К сожалению ты умер...")
        time.sleep(2)
        print("Хотя ты можешь начать с самого начала ведь это просто сон...")
        time.sleep(3)
        print("А ты сейчас...")
        time.sleep(1)
        print("Находишся в больничной койке.")
        time.sleep(2)
        print("Ты получил солнечный удар и поэтому ты пролижал тут 1 день.")
        time.sleep(3)
        print("Ты опять ходишь в школу...")
        time.sleep(2)
        print("Ты снова идешь домой...")
        time.sleep(2)
        print("Но уже с кепкой...")
        time.sleep(2)
        print("И ты совсем не помнишь что было с тобой пока ты спал..")
        time.sleep(3)
        print("Ведь ты тогда и правда был в другом мире.")
        time.sleep(3)
        print("До встречи страник миров.")
        time.sleep(2)
        quit()


    at1 = random.randint(0, 2)

    if at1 == 0:
        hp = hp - ataka1
        time.sleep(1)
        print("Король троллей нанес тебе " + str(ataka1) + " урона, у тебя осталось " + str(hp) + " здоровья")
    if at1 == 1:
        a = random.randint(0, 100)
        if a >= 70:
            time.sleep(1)
            print("Король троллей к счастью промахнулся")
        if a <= 69:
            time.sleep(1)
            hp = hp - ataka2
            time.sleep(1)
            print("Король троллей нанес тебе " + str(ataka2) + " урона, у тебя осталось " + str(hp) + " здоровья")
    if at1 == 2:
        a = random.randint(0, 100)
        if a >= 50:
            time.sleep(1)
            print("Король троллей к счастью промахнулся")
        if a <= 49:
            time.sleep(1)
            hp = hp - ataka3
            print("Король троллей нанес тебе " + str(ataka3) + " урона, у тебя осталось " + str(hp) + " здоровья")
