import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import functions as fun


class PCMeter_GUI:
    
    def __init__(self):
        
        #main structure
        self.root=tk.Tk()
        self.root.geometry("900x600")
        self.root.title("PCMeter")

        #header
        self.header_label=tk.Label(self.root, text="Welcome to PCMeter!", font=("Arial Black",25))
        self.header_label.pack(padx=5,pady=5)



        #reading checkboxes
        self.checkbox_readings_frame=tk.Frame(self.root)
        self.checkbox_readings_frame.columnconfigure(0,weight=1)
        self.checkbox_readings_frame.columnconfigure(1,weight=1)
        self.checkbox_readings_frame.columnconfigure(2,weight=1)
        self.checkbox_readings_frame.columnconfigure(3,weight=1)



        
        self.check_state_cpu=tk.IntVar()
        self.checkbox_cpu=tk.Checkbutton(self.checkbox_readings_frame, text="read cpu usage", font=("Arial",10), variable=self.check_state_cpu)
        self.checkbox_cpu.grid(row=0,column=0, sticky=tk.W+tk.E)

        self.check_state_gpu=tk.IntVar()
        self.checkbox_gpu=tk.Checkbutton(self.checkbox_readings_frame, text="read gpu usage", font=("Arial",10), variable=self.check_state_gpu)
        self.checkbox_gpu.grid(row=0,column=1, sticky=tk.W+tk.E)

        self.check_state_ram=tk.IntVar()
        self.checkbox_ram=tk.Checkbutton(self.checkbox_readings_frame, text="read ram usage", font=("Arial",10), variable=self.check_state_ram)
        self.checkbox_ram.grid(row=0,column=2, sticky=tk.W+tk.E)

        self.check_state_disc=tk.IntVar()
        self.checkbox_disc=tk.Checkbutton(self.checkbox_readings_frame, text="read disc usage", font=("Arial",10), variable=self.check_state_disc)
        self.checkbox_disc.grid(row=0,column=3, sticky=tk.W+tk.E)


        
        #readings header
        self.readings_header=tk.Label(self.root, text="Select your readings", font=("Arial Black",15))
        self.readings_header.pack(padx=5, pady=5)


        self.checkbox_readings_frame.pack(fill="x", padx=10, pady=10)


        #options checkboxes
        self.checkbox_options_frame=tk.Frame(self.root)
        self.checkbox_options_frame.columnconfigure(0,weight=1)
        self.checkbox_options_frame.columnconfigure(1,weight=1)
        self.checkbox_options_frame.columnconfigure(2,weight=1)
        self.checkbox_options_frame.columnconfigure(3,weight=1)


        self.check_state_log=tk.IntVar()
        self.checkbox_log=tk.Checkbutton(self.checkbox_options_frame, text="custom log file path", font=("Arial",10), variable=self.check_state_log)
        self.checkbox_log.grid(row=0,column=0, sticky=tk.W+tk.E)

        self.check_state_sinfo=tk.IntVar()
        self.checkbox_system_info=tk.Checkbutton(self.checkbox_options_frame, text="show system info in log file", font=("Arial",10), variable=self.check_state_sinfo)
        self.checkbox_system_info.grid(row=0,column=1, sticky=tk.W+tk.E)

        self.check_state_tinterval=tk.IntVar()
        self.checkbox_time_inverval=tk.Checkbutton(self.checkbox_options_frame, text="choose own time interval", font=("Arial",10), variable=self.check_state_tinterval)
        self.checkbox_time_inverval.grid(row=0,column=2, sticky=tk.W+tk.E)

        self.check_state_wtime=tk.IntVar()
        self.checkbox_work_time=tk.Checkbutton(self.checkbox_options_frame, text="choose own work time", font=("Arial",10), variable=self.check_state_wtime)
        self.checkbox_work_time.grid(row=0,column=3, sticky=tk.W+tk.E)

        #options header
        self.options_header=tk.Label(self.root, text="Select your options", font=("Arial Black",15))
        self.options_header.pack(padx=5, pady=5)

        self.checkbox_options_frame.pack(fill="x", padx=10, pady=10)


        self.start_button=tk.Button(self.root, text="Start reading", font=("Arial Black",20), command=self.start_reading)
        self.start_button.pack(padx=10, pady=50)

        self.root.mainloop()
    

    def start_reading(self):
        #main reading function
        if not self.check_state_cpu or self.check_state_disc or self.check_state_gpu or self.check_state_ram:
            self.no_reading_selected_warning="No reading selected"
            self.show_warning(self.no_reading_selected_warning)
            return
        self.log_file=self.create_log_file()

        if self.log_file==0:
            self.show_message("Readings stopped")

        if self.check_state_sinfo:
            self.log_file.write(fun.show_system_info())


        #if work time not defined, it is defined to one iteration only

        if self.check_state_wtime:
            self.work_time=simpledialog.askinteger("","Enter custom work time duration")
        else:
            self.work_time=0

        #if not self.work_time:
            
    def print_to_log_file(self, log_file, message):
        log_file.write(message)

    def create_log_file(self):
        #log file without customized pathing is being created in same path as .exe file


        if self.check_state_log.get() == 1:

            self.custom_path=simpledialog.askstring("","Enter custom log file path")

            if self.custom_path:

                
                if self.custom_path.endswith("\\"):
                    self.log_file_path=self.custom_path+"log.txt"

                else:
                    self.log_file_path=self.custom_path+"\log.txt"                                 


                if os.path.exists(self.log_file_path):
                    self.show_warning("Log file already exists in this path!")
                    return 0
                with open(self.log_file_path,"a") as log:
                    return log

            else:

                self.custom_path_checked_but_no_info="Custom path checked but no path given"
                self.show_message(self.custom_path_checked_but_no_info)




        elif self.check_state_log.get() == 0:

            with open("log.txt","a") as log:
                return log
            
    def show_message(self, message):
        #function used for showing info
        messagebox.showinfo(title="PCMeter", message=message)

    def show_warning(self, warning):
        #function used for showing warnings
        messagebox.showwarning(title="PCMeter", message=warning)

PCMeter_GUI()