import re


def log_parser(log_file_path):
    with open(log_file_path,"r") as f:
        for line in f:
            line.strip()
            usage=re.search("^:*%$",line)
            print(usage)



log_parser("log.txt")