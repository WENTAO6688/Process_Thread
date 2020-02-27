from multiprocessing import Queue, Process

# create the child process
def communicate(subqueue):
    subqueue.put('Martin')

if __name__ == "__main__":
    # the process queue
    q = Queue()
    # create the process
    p = Process(target=communicate, args=(q,))
    # run this process
    p.start()
    print(q.get())

