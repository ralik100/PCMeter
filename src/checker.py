import popup


def any_readings_checked(readings):
    if  readings.count(1)==0:
        no_reading_selected_warning="No reading selected"
        popup.show_warning(no_reading_selected_warning)
        return False
    return True