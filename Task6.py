"""
Name: Akshad Kolhatkar
Reg No: RA1911003010842

Q]  Modify the provided ReverseHelloMultithreaded file so that it
creates a thread (let’s call it Thread 1). Thread 1 creates another thread
(Thread 2); Thread 2 creates Thread 3; and so on, up to Thread 50. Each
thread should print “Hello from Thread <num>!”, but you should
structure your program such that the threads print their greetings in
reverse order. When complete, ReverseHelloTest should run
successfully. It’s critical to note, though, that passing the test isn’t
sufficient for succeeding at this problem. You could pass the test just by
writing code with a loop to count down. You’ve got to do this correctly
via threading.
"""


import threading, time
def print_time_842(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        threadLock.acquire()
        print ("%s: %s" % (threadName, counter))
        counter -= 1
    threadLock.release()
    threadLock.release()
    threadLock.release()
class myThread_842 (threading.Thread):
    
    def __init__(self, name_842, counter,delay):
        
        threading.Thread.__init__(self)
        self.name = name_842
        self.counter = counter
        self.delay = delay
        
    def run_842(self):

        print_time_842(self.name, self.counter, self.delay)
threadLock = threading.RLock()
threads_842 = []

thread1_842 = myThread_842("Hello from Thread", 1,50)
thread1_842.run_842()

thread1_842.start()

threads_842.append(thread1_842)

for t in threads_842:
    t.join()
print ("Exiting Main Thread")
