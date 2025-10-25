import popup
import tkinter

def any_readings_checked(readings):
    if  readings.count(1)==0:
        no_reading_selected_warning="No reading selected"
        popup.show_warning(no_reading_selected_warning)
        return False
    return True

def check_state_clear_log_file():
    return check_state_clear