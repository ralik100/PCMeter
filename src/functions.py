import psutil
import datetime

def cpu_usage(interval):

    time=datetime.datetime.now()
    x=psutil.cpu_percent(interval)

    return f"{time} ||| CPU usage: {x}%."

def ram_usage():

    
    return psutil.virtual_memory().percent

def disc_usage():

    return psutil.disk_usage('/').percent

def show_system_info():

    return "test"

def gpu_usage():
    #wip
    return "gpu"