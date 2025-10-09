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