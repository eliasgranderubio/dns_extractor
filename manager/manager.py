from asyncio import Queue
from threading import Lock
from threading import Semaphore


class Manager:

    # -- Public methods

    # Manager Constructor
    def __init__(self):
        super(Manager, self).__init__()
        self.input_queue = Queue()
        self.output_queue = Queue()
        self.lock = Lock()
        self.reader_worker_count = 0
        self.dns_worker_count = 0
        self.max_fly_queries = Semaphore(value=40000)

    # Acquire fly queries semaphore
    def fly_queries_acquire(self):
        self.max_fly_queries.acquire()

    # Release fly queries semaphore
    def fly_queries_release(self):
        self.max_fly_queries.release()

    # Is the read finished
    def is_the_read_finished(self):
        with self.lock:
            return self.reader_worker_count == 0 and self.input_queue.empty()

    # Is read extractor empty
    def is_dns_extractor_empty(self):
        with self.lock:
            return self.reader_worker_count == 0 and self.dns_worker_count == 0 and \
                   self.input_queue.empty() and self.output_queue.empty()

    # Increment reader worker count
    def increment_reader_worker(self):
        with self.lock:
            self.reader_worker_count += 1

    # Decrease reader worker count
    def decrease_reader_worker(self):
        with self.lock:
            self.reader_worker_count -= 1

    # Increment dns worker count
    def increment_dns_worker(self):
        with self.lock:
            self.dns_worker_count += 1

    # Decrease dns worker count
    def decrease_dns_worker(self):
        with self.lock:
            self.dns_worker_count -= 1

    # -- Getters

    # Get input queue
    def get_input_queue(self):
        return self.input_queue

    # Get output queue
    def get_output_queue(self):
        return self.output_queue
