import time
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f'task{id} start')
    time.sleep(1)
    print(f'task{id} stop')

start=time.perf_counter()

with ThreadPoolExecutor() as executor:
    f1=executor.submit(task,1)
    f2=executor.submit(task,2)
    results=executor.map(task,[1,2])


f1.result()
f2.result()

for result in results:
    result

finish=time.perf_counter()

print(finish-start)