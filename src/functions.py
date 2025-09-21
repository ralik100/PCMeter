import psutil

def cpu_usage(interval):

    return psutil.cpu_times_percent(interval)

def ram_usage():

    
    return psutil.virtual_memory().percent

def disc_usage():

    return psutil.disk_usage('/').percent
