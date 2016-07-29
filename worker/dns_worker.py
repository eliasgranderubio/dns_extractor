from threading import Thread
import dns.resolver


class DnsWorker(Thread):

    # -- Public methods

    # DnsWorker Constructor
    def __init__(self, manager):
        super(DnsWorker, self).__init__()
        self.manager = manager

    # Run dns worker
    def run(self):
        while not self.manager.is_the_read_finished():
            if not self.manager.get_input_queue().empty():
                info = self.manager.get_input_queue().get_nowait()
                # Increment dns workers
                self.manager.increment_dns_worker()
                # Prepare A query
                dns_resolver = dns.resolver.Resolver()
                dns_resolver.timeout = 2
                dns_resolver.lifetime = 2
                dns_resolver.nameservers = [info['ns']]
                try:
                    answers = dns_resolver.query(info['hostname'], 'A', raise_on_no_answer=False)
                    # Process the answers
                    if type(answers) is not None and type(answers) is not TypeError:
                        for answer in answers:
                            data = {}
                            data['hostname'] = info['hostname']

                            data['ip'] = str(answer)
                            self.manager.get_output_queue().put_nowait(data)
                except:
                    # No matter
                    pass
                # Task done
                self.manager.fly_queries_release()
                # Decrease dns workers
                self.manager.decrease_dns_worker()
