import re

def log_parser(log_file_path):
    result=[]
    f=open(log_file_path, "r")
    if f:
        for line in f:
            line.strip()
            log_timestamp=re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)", line)
            res=re.search(r"CPU usage:\s*([0-9.]+)%", line)
            if log_timestamp:
                words=line.split(" ")
                timestamp=str(log_timestamp.group(1))
                metric=words[3]
                usage=get_usage(line,metric)
                if usage:
                    result.append({"Metric": metric, "Usage": usage, "Time":timestamp})
                else:
                    continue
        return result

def get_usage(line, metric):
    match metric:
        case "CPU":
            res=re.search(r"CPU usage:\s*([0-9.]+)%", line)
            return float(res.group(1))
        case "GPU":
            res=re.search(r"GPU usage:\s*([0-9.]+)%", line)
            return float(res.group(1))
        case "Disc":
            res=re.search(r"Disc usage:\s*([0-9.]+)%", line)
            return float(res.group(1))
        case "RAM":
            res=re.search(r"RAM usage:\s*([0-9.]+)%", line)
            return float(res.group(1))
        case _:
            pass