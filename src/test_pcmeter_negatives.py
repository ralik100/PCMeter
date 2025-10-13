import gui
import functions as fun
import time
import io
import os
from unittest.mock import patch


def test_missing_reading_check():
    app=gui.PCMeter_GUI()
    with patch("tkinter.messagebox.showwarning") as mock_warning:
        app.start_reading()

        mock_warning.assert_called_once_with(title="PCMeter",message="No reading selected")

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

            app.check_state_cpu.set(1)
            app.check_state_tinterval.set(1)

            app.start_reading()

            mock_warning.assert_called_once_with(title="PCMeter", message="CPU reading interval should be more than 0!")

def test_customized_cpu_reading_interval_no_value():

    app=gui.PCMeter_GUI()
    
    with patch("tkinter.simpledialog.askfloat", return_value=None):
        with patch("tkinter.messagebox.showwarning") as mock_warning:

            app.check_state_cpu.set(1)
            app.check_state_tinterval.set(1)

            app.start_reading()

            mock_warning.assert_called_once_with(title="PCMeter", message="CPU reading interval should be more than 0!")

def test_customized_work_time_wrong_value():
    app = gui.PCMeter_GUI()

    with patch("tkinter.simpledialog.askinteger", return_value=int(0)):
        with patch("tkinter.messagebox.showwarning") as mock_warning:
            app.check_state_wtime.set(1)
            app.check_state_disc.set(1)
            app.start_reading()

            mock_warning.assert_called_once_with(title="PCMeter", message="Custom work time should be more or equal 2")

def test_customized_work_time_no_value():
    app = gui.PCMeter_GUI()

    with patch("tkinter.simpledialog.askinteger", return_value=None):
        with patch("tkinter.messagebox.showwarning") as mock_warning:
            app.check_state_wtime.set(1)
            app.check_state_disc.set(1)
            app.start_reading()

            mock_warning.assert_called_once_with(title="PCMeter", message="Custom work time should be more or equal 2")

