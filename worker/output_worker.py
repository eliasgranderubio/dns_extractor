from threading import Thread
import hashlib
import sys


class OutputWorker(Thread):

    # -- Public methods

    # OutputWorker Constructor
    def __init__(self, manager, filename):
        super(OutputWorker, self).__init__()
        self.manager = manager
        self.filename = filename
        self.records = set()

    # Run output worker
    def run(self):
        # Prepare output stream
        if self.filename != '':
            f = open(self.filename, 'w')
        else:
            f = sys.stdout
        # Print output
        while not self.manager.is_dns_extractor_empty():
            if not self.manager.get_output_queue().empty():
                info = self.manager.get_output_queue().get_nowait()
                output_record = info['hostname'] + ',' + info['ip']
                if self.__is_new_record(output_record):
                    print(output_record, file=f, flush=True)
                self.manager.get_output_queue().task_done()

    # -- Private methods

    # Check if record is new
    def __is_new_record(self, record):
        m = hashlib.md5()
        m.update(str(record).encode('utf-8'))
        digest = m.hexdigest()
        if digest in self.records:
            return False
        else:
            self.records.add(digest)
            return True
