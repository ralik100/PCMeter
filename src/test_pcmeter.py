import gui
import functions as fun
import time
import io
import os



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
    app=gui.PCMeter_GUI()
    file=app.create_log_file()
    file.close()
    assert isinstance(file, io.TextIOWrapper)
    


def test_custom_log_file_path_no_backslash_given():
    app=gui.PCMeter_GUI()
    app.checkbox_log.select()
    app.custom_path="C:\\PCMeter"
    file=app.create_log_file()
    file.close()
    app.custom_path+="\\"
    assert os.path.isfile(os.path.join(app.custom_path, "log.txt"))

def test_custom_log_file_path_with_backslash_given():
    app=gui.PCMeter_GUI()
    app.checkbox_log.select()
    app.custom_path="C:\\PCMeter\\"
    file=app.create_log_file()
    file.close()
    assert os.path.isfile(os.path.join(app.custom_path, "log.txt"))

    