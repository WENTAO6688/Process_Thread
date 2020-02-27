import time
import multiprocessing

# the function for the child process
def run(child):
    time.sleep(2)
    print(child)

# for loop for five child process
for i in range(5):
# create the instance of child process
    p = multiprocessing.Process(target=run, args=(i,))
# run the child process
    p.start()
