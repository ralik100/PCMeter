import psutil
import datetime
import platform

def cpu_usage(interval):

    time=datetime.datetime.now()
    x=psutil.cpu_percent(interval)

    return f"{time} ||| CPU usage: {x}%."

def ram_usage():

    time=datetime.datetime.now()
    x=psutil.virtual_memory().percent

    return f"{time} ||| RAM usage: {x}%."

def disc_usage():

    time=datetime.datetime.now()
    x=psutil.disk_usage('/').percent

    return f"{time} ||| Disc usage: {x}%."

def show_system_info():

    time=datetime.datetime.now()

    system=platform.system()
    version=platform.version()
    cpu=platform.processor()
    ram=psutil.virtual_memory().total
    disc=psutil.disk_usage('/')
    return f"{time} ||| System information: file system={system} ||| version={version} ||| CPU={cpu} ||| total RAM={ram} ||| total disc={disc}.\n"

def gpu_usage():
    #wip

    time=datetime.datetime.now()


    return "gpu"