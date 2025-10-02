import gui
import functions as fun
import time
import io



def test_cpu_usage():

    text=fun.ram_usage()
    assert isinstance(text,(str))

def test_ram_usage():

    text=fun.ram_usage()
    assert isinstance(text,(str))

def test_disc_usage():

    text=fun.disc_usage()
    assert isinstance(text,(str))

def test_show_system_info():

    text=fun.show_system_info()
    assert isinstance(text,(str))


def test_ram_usage_proper_values():
    text=fun.ram_usage()
    words=text.split(" ")
    var=words[-1]
    tested=""
    for letter in var:
        if letter=="%":
            break
        tested+=letter
    
    assert 0<=float(tested)<=100


def test_cpu_usage_proper_values():
    text=fun.cpu_usage(1)
    words=text.split(" ")
    var=words[-1]
    tested=""
    for letter in var:
        if letter=="%":
            break
        tested+=letter
    
    assert 0<=float(tested)<=100


def test_disc_usage_proper_values():
    text=fun.disc_usage()
    words=text.split(" ")
    var=words[-1]
    tested=""
    for letter in var:
        if letter=="%":
            break
        tested+=letter
    
    assert 0<=float(tested)<=100

def test_cpu_usage_work_time():
    start=time.time()
    result=fun.cpu_usage(10)
    end=time.time()
    time_elapsed=end-start
    assert 10.1 >= time_elapsed >= 9.9

def test_gui_creating_log_file():
    x_gui=gui.PCMeter_GUI
    file=x_gui.create_log_file()
    assert isinstance(file, io.TextIOWrapper)
    file.close()
