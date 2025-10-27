import gui
import functions as fun
import checker
import time
import io
import os
from unittest.mock import patch


def test_missing_reading_check():
    app=gui.PCMeter_GUI()
    with patch("tkinter.messagebox.showwarning") as mock_warning:
        no_reading_checked=[0,0,0,0]
        result=checker.any_readings_checked(no_reading_checked)
        assert result==False

def test_missing_reading_warning_message():
    app=gui.PCMeter_GUI()
    with patch("tkinter.messagebox.showwarning") as mock_warning:
        result=app.any_readings_checked()
        
        mock_warning.assert_called_once_with(title="PCMeter", message="No reading selected")

def test_custom_log_path_checked_but_no_path_given():

    app=gui.PCMeter_GUI()
    with patch("tkinter.simpledialog.askstring",return_value=None):
        with patch("tkinter.messagebox.showwarning") as mock_warning:
            app.check_state_log.set(1)

            app.create_log_file()

            mock_warning.assert_called_once_with(title="PCMeter", message="Custom path checked but no path given")


def test_customized_cpu_reading_interval_wrong_value():

    app=gui.PCMeter_GUI()
    
    with patch("tkinter.simpledialog.askfloat", return_value=0):
        with patch("tkinter.messagebox.showwarning") as mock_warning:

            result=app.get_custom_cpu_clock_interval()

            mock_warning.assert_called_once_with(title="PCMeter", message="CPU reading interval should be more than 0!")


def test_customized_cpu_reading_interval_no_value():

    app=gui.PCMeter_GUI()
    
    with patch("tkinter.simpledialog.askfloat", return_value=None):
        with patch("tkinter.messagebox.showwarning") as mock_warning:

            app.get_custom_cpu_clock_interval()

            mock_warning.assert_called_once_with(title="PCMeter", message="CPU reading interval should be more than 0!")

def test_customized_work_time_wrong_value():
    app = gui.PCMeter_GUI()

    with patch("tkinter.simpledialog.askinteger", return_value=int(0)):
        with patch("tkinter.messagebox.showwarning") as mock_warning:
            app.check_state_wtime.set(1)
            app.check_state_disc.set(1)
            app.get_custom_work_time()

            mock_warning.assert_called_once_with(title="PCMeter", message="Custom work time should be more or equal 2")

def test_customized_work_time_no_value():
    app = gui.PCMeter_GUI()

    with patch("tkinter.simpledialog.askinteger", return_value=None):
        with patch("tkinter.messagebox.showwarning") as mock_warning:
            app.check_state_wtime.set(1)
            app.check_state_disc.set(1)
            app.get_custom_work_time()

            mock_warning.assert_called_once_with(title="PCMeter", message="Custom work time should be more or equal 2")

def test_error_while_creating_log_file():
    app = gui.PCMeter_GUI()

    with patch("gui.PCMeter_GUI.create_log_file", return_value=int(0)):
        with patch("tkinter.messagebox.showinfo") as mock_info:

            file=app.create_log_file()
            app.check_state_disc.set(1)
            app.start_reading()

            mock_info.assert_called_once_with(title="PCMeter", message="Readings stopped")


