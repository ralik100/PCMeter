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