from tkinter import simpledialog
import sys
import os
import popup
import functions as fun

def clear_log_file(log_file):
        log_file.seek(0)
        log_file.truncate()

def log_close(log_file):
        if log_file:
            print_to_log_file(log_file, "Readings finished successfully!\n")
            log_file.close()
        sys.exit(0)

def create_log_file(log_check_state):
        if log_check_state:
            custom_path = simpledialog.askstring("", "Enter custom log file path")

            if custom_path:
                log_file_path = os.path.join(custom_path, "log.txt")

                os.makedirs(custom_path, exist_ok=True)

                return open(log_file_path, "a")
            else:
                custom_path_checked_but_no_info = "Custom path checked but no path given"
                popup.show_warning(custom_path_checked_but_no_info)
                return None

        elif log_check_state == 0:
            log_file_path = "log.txt"
            return open(log_file_path, "a")
        

    #basic function for printing readings to log file
def print_readings(readings, log_file, cpu_interval):


        functions=[fun.cpu_usage(cpu_interval), fun.gpu_usage(), fun.ram_usage(), fun.disc_usage()]
        for i in range(4):
            if readings[i]==1:
                x=functions[i]
                y=x
                print_to_log_file(log_file, str(y)+"\n")



def print_to_log_file(log_file, message):
        #basic log writing method

        log_file.write(message)
