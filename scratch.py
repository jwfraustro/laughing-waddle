from multiprocessing import Process
import time

def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()

def p1():
    time.sleep(2)
    print("p1")

def p2():
    time.sleep(5)
    print("p2")

if __name__ == '__main__':
    print("start")
    runInParallel(p1,p2)
    print("continue")
