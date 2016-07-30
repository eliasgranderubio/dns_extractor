import argparse
import sys
import tldextract


class CLIParser:

    # -- Public methods

    # CLIParser Constructor
    def __init__(self):
        super(CLIParser, self).__init__()
        self.parser = argparse.ArgumentParser(prog='dns_extractor.py', description='DNS brute force application.')
        self.parser.add_argument('-d', '--domain', required=True, help='input domain for searching')
        self.parser.add_argument('-r', '--resolvers', required=True, type=argparse.FileType('r'),
                                 metavar='FILE', help='input file containing newline delimited list of resolvers')
        self.parser.add_argument('-s', '--subdomains', required=True, type=argparse.FileType('r'),
                                 metavar='FILE', help='input file containing newline delimited list of subdomains')
        self.parser.add_argument('-om', '--output_mode', choices=['csv', 'json'], default='csv',
                                 help='output format. By default csv mode is set')
        self.parser.add_argument('-o', '--output', metavar='FILE',
                                 help='output file for writing results. By default, results will be shown on stdout')
        self.parser.add_argument('--no_auth_ns', action='store_true',
                                 help='the authoritative dns for the domain searched will be excluded from resolvers '
                                      'if it was not included in resolvers input file. By default, the authoritative '
                                      'dns for the domain searched is added to resolvers list if it was not included '
                                      'yet')
        self.parser.add_argument('-w', '--workers', default=50, type=int,
                                 help='number of workers for execution. By default, the workers number is set to 50')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0',
                                 help='show the version message and exit')
        self.args = self.parser.parse_args()

    # -- Getters

    # Get output mode
    def get_output_mode(self):
        return self.args.output_mode

    # Get if authoritative ns will be included
    def include_auth_ns(self):
        if self.args.no_auth_ns:
            return False
        else:
            return True

    # Get number of workers
    def get_workers(self):
        workers = self.args.workers
        if not workers > 0:
            self.parser.print_usage(file=sys.stderr)
            print(self.parser.prog + ': error: argument -w/--workers: The number of workers must be greater than 0.',
                  file=sys.stderr)
            sys.exit(2)
        return workers

    # Get domain
    def get_domain(self):
        ext = tldextract.extract(self.args.domain)
        if ext.domain == '' or ext.suffix == '':
            self.parser.print_usage(file=sys.stderr)
            print(self.parser.prog + ': error: argument -d/--domain: The domain name must be well formed.',
                  file=sys.stderr)
            sys.exit(2)
        return str(ext.domain + '.' + ext.suffix).strip()

    # Get resolvers filename
    def get_resolvers_filename(self):
        return self.args.resolvers.name

    # Get subdomains filename
    def get_subdomains_filename(self):
        return self.args.subdomains.name

    # Get output filename
    def get_output_filename(self):
        if self.args.output is None:
            output_filename = ''
        else:
            output_filename = self.args.output
        return output_filename
