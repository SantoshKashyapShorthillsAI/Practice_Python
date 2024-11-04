from threading import Thread
import time

def replace(filename , old , new):
    with open(filename, 'r') as f:
        content = f.read()

    content=content.replace(old,new)

    with open(filename,'w') as f:
        f.write(content)

def main():
    filenames=[]

    Threads=[Thread(target=replace , args=(file,'id','ids')) for file in filenames]
    
    for threads in Threads:
        threads.start()

    for threads in Threads:
        threads.join()

if __name__=='__main__':
    start_time=time.perf_counter()
    main()
    end_time=time.perf_counter()
    print(end_time-start_time)
