import time
from threading import Thread

def task(id):
    print(f"starting a task {id}" )
    time.sleep(1)
    print(f"done {id}")

start_time=time.perf_counter()

threads=[]
for i in range(10):
    t=Thread(target=task , args=(i,))
    threads.append(t)
    t.start()
    


for t in threads:
    t.join()

end_time=time.perf_counter()

print(end_time-start_time)