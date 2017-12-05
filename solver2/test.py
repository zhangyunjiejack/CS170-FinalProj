from multiprocessing import Process, Lock
from threading import Thread

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [0, 1, 0, 1, 0, 1, 0, 1, 0]



def f():
    a = sum(lst1) + sum(lst2)
    print(a)

def g():
    b = sum(lst2)
    print(b)

threadA = Thread(target = f, )
threadB = Thread(target = g, )
threadA.start()
threadB.start()
# Do work indepedent of loopA and loopB
# threadA.join()
# threadB.join()
# threadC.join()
