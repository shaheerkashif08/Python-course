import threading
import time

def workers(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)     # simulate some work
    print(f"Thread {num}: Finishing")

threads = []
for i in range(3):
    thread = threading.Thread(target = workers, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()     # wait for all threads to finish
print("All thread completed.")