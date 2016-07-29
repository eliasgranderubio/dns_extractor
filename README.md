# dns_extractor
dns_extractor is a community driven project with the goal of creating the fastest subdomain enumeration tool.

## Prerequisites
Before dns_extractor usage, you must have installed Python >= 3.4.3 and the requirements:
```
    pip install -r requirements.txt
```

## Usage
Below, the help when you type `./dns_extractor.py -h` is shown:

```
    usage: dns_extractor.py [-h] -d DOMAIN -r RESOLVERS -s SUBDOMAINS [-w WORKERS]
                            [-o OUTPUT]

    DNS brute force application.

    optional arguments:
      -h, --help            show this help message and exit
      -d DOMAIN, --domain DOMAIN
                            Input domain for searching.
      -r RESOLVERS, --resolvers RESOLVERS
                            Input file containing newline delimited list of
                            resolvers.
      -s SUBDOMAINS, --subdomains SUBDOMAINS
                            Input file containing newline delimited list of
                            subdomains.
      -w WORKERS, --workers WORKERS
                            Number of workers for execution. By default, the
                            workers number is set to 50.
      -o OUTPUT, --output OUTPUT
                            Output file for writing results. By default, results
                            will be shown on stdout.
```

Fulfilling with the described usage, a usage example would be the next one:
```
	./dns_extractor.py -w 50 -d microsoft.com -r ./resolvers_example.txt -s subdomains_example.txt
```

A expected output example is shown below:
```
  mail.microsoft.com,157.58.197.10
  mail.microsoft.com,167.220.71.19
  ftp.microsoft.com,134.170.188.232
  www.microsoft.com,23.62.124.108
  www.microsoft.com,2.17.234.96
```

## Bugs and Feedback
For bugs, questions and discussions please use the [Github Issues](https://github.com/eliasgranderubio/dns_extractor/issues) or ping me on Twitter (@3grander).
