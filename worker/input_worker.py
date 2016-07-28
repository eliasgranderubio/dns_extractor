from threading import Thread
from threading import Timer
import os
import traceback
import sys


class InputWorker(Thread):

    # -- Public methods

    # InputWorker Constructor
    def __init__(self, domain, manager, resolvers_file, names_file):
        super(InputWorker, self).__init__()
        self.domain = domain
        self.manager = manager
        self.resolvers_file = resolvers_file
        self.names_file = names_file

    # Run input worker
    def run(self):
        # Increment reader workers
        self.manager.increment_reader_worker()
        # Read resolvers file
        name_servers = self.__file_to_list(self.resolvers_file)
        # Read names file
        names = self.__file_to_list(self.names_file)
        # Expand brute force tree
        for subdomain in names:
            for ns in name_servers:
                data = {}
                data['hostname'] = subdomain + '.' + self.domain
                data['ns'] = str(ns).strip()
                self.manager.fly_queries_acquire()
                self.manager.get_input_queue().put_nowait(data)
        # Decrease reader workers
        self.manager.decrease_reader_worker()

    # -- Private methods

    # File to array
    @staticmethod
    def __file_to_list(filename):
        try:
            with open(filename) as f:
                lines = [x.strip('\n') for x in f.readlines()]
            return lines
        except:
            # Fatal error, the input file can not be read, so the parent thread is stopped
            print(traceback.format_exc(0).splitlines()[1], file=sys.stderr)
            t = Timer(1, os._exit(1), [0])
            raise
