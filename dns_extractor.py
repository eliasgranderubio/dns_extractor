from manager.manager import Manager
from worker.dns_worker import DnsWorker
from worker.input_worker import InputWorker
from worker.output_worker import OutputWorker
from util.cli_parser import CLIParser


# Start the output worker and wait for it
def start_output_worker_and_wait_for(manager, output_filename):
    w = OutputWorker(manager, output_filename)
    w.start()
    w.join()


# Start the dns workers
def start_dns_workers(manager, total_workers):
    for i in range(total_workers):
        DnsWorker(manager).start()


# Start the input worker
def start_input_worker(manager, domain, resolvers_filename, subdomains_filename, include_auth_ns):
    InputWorker(domain, manager, resolvers_filename, subdomains_filename, include_auth_ns).start()


# Main function
def main(parsed_args):
    manager = Manager()
    start_input_worker(manager, parsed_args.get_domain(), parsed_args.get_resolvers_filename(),
                       parsed_args.get_subdomains_filename(), parsed_args.include_auth_ns())
    start_dns_workers(manager, parsed_args.get_workers())
    start_output_worker_and_wait_for(manager, parsed_args.get_output_filename())

if __name__ == "__main__":
    main(CLIParser())
