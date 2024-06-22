import threading
import time

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)

# parallelism
start_time = time.time()
threads = []
for i in range(10):
    thread_name = (f'Thread-{i+1}')
    thread = threading.Thread(target=get_thread, args=(thread_name,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
end_time = time.time()

difference_parallel = end_time - start_time
print(f'Time of done parallel task: {end_time - start_time} sec.')


# synchronous
start_time = time.time()
for i in range(10):
    thread_name = (f'Thread-{i+1}')
    get_thread(thread_name)
end_time = time.time()

difference_synchronous = end_time - start_time
print(f'Time of done synchronous task: {end_time - start_time} sec.')


difference = difference_synchronous - difference_parallel
print(f'Difference between time results is {difference} sec. Synchronous is faster')
