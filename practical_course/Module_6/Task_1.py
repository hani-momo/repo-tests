import threading
import time

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


for i in range(5):
    thread_name = (f'Thread №{i+1}')
    thread = threading.Thread(target=get_thread, args=(thread_name,))
    
    thread.start()
