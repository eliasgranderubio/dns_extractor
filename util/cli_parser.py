import argparse
import sys
import tldextract


class CLIParser:

    # -- Public methods

    # CLIParser Constructor
    def __init__(self):
        super(CLIParser, self).__init__()
        self.parser = argparse.ArgumentParser(prog='dns_extractor.py', description='DNS brute force application.')
        self.parser.add_argument('-d', '--domain', required=True, nargs=1,
                                 help='Input domain for searching.')
        self.parser.add_argument('-r', '--resolvers', required=True, nargs=1, type=argparse.FileType('r'),
                                 help='Input file containing newline delimited list of resolvers.')
        self.parser.add_argument('-s', '--subdomains', required=True, nargs=1, type=argparse.FileType('r'),
                                 help='Input file containing newline delimited list of subdomains.')
        self.parser.add_argument('-w', '--workers', default=[50], nargs=1, type=int,
                                 help='Number of workers for execution. By default, the workers number is set to 50.')
        self.parser.add_argument('-o', '--output', nargs=1,
                                 help='Output file for writing results. By default, results will be shown on stdout.')
        self.args = self.parser.parse_args()

    # -- Getters

    # Get number of workers
    def get_workers(self):
        workers = self.args.workers[0]
        if not workers > 0:
            self.parser.print_usage(file=sys.stderr)
            print(self.parser.prog + ': error: argument -w/--workers: The number of workers must be greater than 0.',
                  file=sys.stderr)
            sys.exit(2)
        return workers

    # Get domain
    def get_domain(self):
        ext = tldextract.extract(self.args.domain[0])
        if ext.domain == '' or ext.suffix == '':
            self.parser.print_usage(file=sys.stderr)
            print(self.parser.prog + ': error: argument -d/--domain: The domain name must be well formed.',
                  file=sys.stderr)
            sys.exit(2)
        return str(ext.domain + '.' + ext.suffix).strip()

    # Get resolvers filename
    def get_resolvers_filename(self):
        return self.args.resolvers[0].name

    # Get resolvers filename
    def get_resolvers_filename(self):
        return self.args.resolvers[0].name

    # Get subdomains filename
    def get_subdomains_filename(self):
        return self.args.subdomains[0].name

    # Get output filename
    def get_output_filename(self):
        if self.args.output is None:
            output_filename = ''
        else:
            output_filename = self.args.output[0]
        return output_filename
