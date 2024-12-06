import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name ,power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def  run(self):
        yyy = 0
        enemy = 100
        print("\n", f"{self.name}, на нас напали!", "\n")

        yyy = round(enemy / self.power)

        for i in range(yyy):

            sleep(1)
            enemy -= self.power
            print("\n", f"{self.name} сражается {i+1} дней, осталось {enemy} врагов", "\n")
        print("\n", f"{self.name} одержал победу спустя {yyy} дней(дня)!", "\n")

ttt = Knight("СВЯТОЗАРОВИЧЬ", 50)
rrr = Knight("OLEG", 25)
ttt.start()
rrr.start()