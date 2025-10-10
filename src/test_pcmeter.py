import gui
import functions as fun
import time
import io
import os
from unittest.mock import patch


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
    


def test_custom_log_file_path(tmp_path):
    app=gui.PCMeter_GUI()
    app.check_state_log.set(1)
    with patch("tkinter.simpledialog.askstring", return_value=str(tmp_path)):
        file=app.create_log_file()
        file.close()
    
    expected = os.path.join(str(tmp_path), "log.txt")
    assert os.path.isfile(expected)

def test_custom_work_time():
    app=gui.PCMeter_GUI()
    
    
    with patch("tkinter.simpledialog.askinteger", return_value=int(4)):
        
        app.check_state_wtime.set(1)
        app.check_state_disc.set(1)
        start=time.perf_counter()
        app.start_reading()
        end=time.perf_counter()    
    time_passed=end-start
    
    assert 4.1>=time_passed>=3.9

def test_clear_log_file(tmp_path):

    app=gui.PCMeter_GUI()
    app.check_state_log.set(1)
    with patch("tkinter.simpledialog.askstring", return_value=str(tmp_path)):
        file=app.create_log_file()

    file.write("Test_message")
    
    app.clear_log_file(file)
    file.close()

    assert os.path.getsize(app.log_file_path)==0


def test_show_message():
    app=gui.PCMeter_GUI()
    with patch("tkinter.messagebox.showinfo") as mock_message:
        app.show_message("Test")

        mock_message.assert_called_once_with(title="PCMeter", message="Test")

    