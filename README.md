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
    usage: dns_extractor.py [-h] -d DOMAIN -r FILE -s FILE [-om {csv,json}]
                            [-o FILE] [--no_auth_ns] [-w WORKERS] [-v]

    DNS brute force application.

    optional arguments:
      -h, --help            show this help message and exit
      -d DOMAIN, --domain DOMAIN
                            input domain for searching
      -r FILE, --resolvers FILE
                            input file containing newline delimited list of
                            resolvers
      -s FILE, --subdomains FILE
                            input file containing newline delimited list of
                            subdomains
      -om {csv,json}, --output_mode {csv,json}
                            output format. By default csv mode is set
      -o FILE, --output FILE
                            output file for writing results. By default, results
                            will be shown on stdout
      --no_auth_ns          the authoritative dns for the domain searched will be
                            excluded from resolvers if it was not included in
                            resolvers input file. By default, the authoritative
                            dns for the domain searched is added to resolvers list
                            if it was not included yet
      -w WORKERS, --workers WORKERS
                            number of workers for execution. By default, the
                            workers number is set to 50
      -v, --version         show the version message and exit
```

Fulfilling with the described usage, a usage example would be the next one:
```
	./dns_extractor.py -w 50 -d microsoft.com -r ./resolvers_example.txt -s subdomains_example.txt
```

A expected output example is shown below:
```
    mail.microsoft.com,157.58.197.10
    mail.microsoft.com,167.220.71.19
    www.microsoft.com,23.62.124.108
    ftp.microsoft.com,134.170.188.232
    blog.microsoft.com,64.4.6.233
    blog.microsoft.com,65.55.39.12
    sftp.microsoft.com,65.55.39.12
    sftp.microsoft.com,64.4.6.233
    files.microsoft.com,65.55.39.12
    files.microsoft.com,64.4.6.233
```

Another expected output example with `--output_mode json` is shown below:
```
    {"hostname": "mail.microsoft.com", "ip": "157.58.197.10"}
    {"hostname": "mail.microsoft.com", "ip": "167.220.71.19"}
    {"hostname": "www.microsoft.com", "ip": "23.62.124.108"}
    {"hostname": "ftp.microsoft.com", "ip": "134.170.188.232"}
    {"hostname": "blog.microsoft.com", "ip": "64.4.6.233"}
    {"hostname": "blog.microsoft.com", "ip": "65.55.39.12"}
    {"hostname": "sftp.microsoft.com", "ip": "65.55.39.12"}
    {"hostname": "sftp.microsoft.com", "ip": "64.4.6.233"}
    {"hostname": "files.microsoft.com", "ip": "65.55.39.12"}
    {"hostname": "files.microsoft.com", "ip": "64.4.6.233"}
```

## Bugs and Feedback
For bugs, questions and discussions please use the [Github Issues](https://github.com/eliasgranderubio/dns_extractor/issues) or ping me on Twitter (@3grander).
