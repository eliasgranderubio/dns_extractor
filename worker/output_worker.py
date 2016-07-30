from threading import Thread
import hashlib
import sys
import json


class OutputWorker(Thread):

    # -- Public methods

    # OutputWorker Constructor
    def __init__(self, manager, filename, output_mode):
        super(OutputWorker, self).__init__()
        self.manager = manager
        self.filename = filename
        self.records = set()
        self.output_mode = output_mode

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
                output_record = OutputWorker.__get_output_record(info['hostname'], info['ip'], self.output_mode)
                if self.__is_new_record(output_record):
                    print(output_record, file=f, flush=True)

    # -- Private methods

    # Get output record
    @staticmethod
    def __get_output_record(hostname, ip, output_format):
        if output_format == 'csv':
            return str(hostname + ',' + ip)
        else:
            data = {}
            data['hostname'] = hostname
            data['ip'] = ip
            return str(json.dumps(data))

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
