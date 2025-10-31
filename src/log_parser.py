import re


def log_parser(log_file_path):
    with open(log_file_path,"r") as f:
        for line in f:
            line.strip()
            res=re.search(r"CPU usage:\s*([0-9.]+)%", line)
            if res:
                usage=float(res.group(1))
                print(usage)



log_parser("log.txt")