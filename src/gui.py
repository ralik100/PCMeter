import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import functions as fun
import time


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
        self.checkbox_time_inverval=tk.Checkbutton(self.checkbox_options_frame, text="choose own cpu time interval", font=("Arial",10), variable=self.check_state_tinterval)
        self.checkbox_time_inverval.grid(row=0,column=2, sticky=tk.W+tk.E)

        self.check_state_wtime=tk.IntVar()
        self.checkbox_work_time=tk.Checkbutton(self.checkbox_options_frame, text="choose own work time", font=("Arial",10), variable=self.check_state_wtime)
        self.checkbox_work_time.grid(row=0,column=3, sticky=tk.W+tk.E)

        self.check_state_reading_interval=tk.IntVar()
        self.checkbox_reading_interval=tk.Checkbutton(self.checkbox_options_frame, text="choose own reading interval", font=("Arial",10), variable=self.check_state_reading_interval)
        self.checkbox_reading_interval.grid(row=1,column=0, sticky=tk.W+tk.E)

        self.check_state_clear_log_file=tk.IntVar()
        self.checkbox_clear_log_file=tk.Checkbutton(self.checkbox_options_frame, text="clear log file if in the same path", font=("Arial",10), variable=self.check_state_clear_log_file)
        self.checkbox_clear_log_file.grid(row=1,column=1, sticky=tk.W+tk.E)

        #options header
        self.options_header=tk.Label(self.root, text="Select your options", font=("Arial Black",15))
        self.options_header.pack(padx=5, pady=5)

        self.checkbox_options_frame.pack(fill="x", padx=10, pady=10)


        self.start_button=tk.Button(self.root, text="Start reading", font=("Arial Black",20), command=self.start_reading)
        self.start_button.pack(padx=10, pady=50)

    


    def run(self):
        self.root.mainloop()

    def start_reading(self):
        #main reading function

        if  not self.check_state_cpu.get() and not self.check_state_disc.get() and not self.check_state_gpu.get() and not self.check_state_ram.get():
            self.no_reading_selected_warning="No reading selected"
            self.show_warning(self.no_reading_selected_warning)
            return
        




        #creating logfile
        self.log_file=self.create_log_file()

        




        #if creating log file went wrong, stop readings
        if self.log_file==0:
            self.show_message("Readings stopped")
            return



        #clearing log file if checked
        if self.check_state_clear_log_file.get():
            self.clear_log_file(self.log_file)



        #showing system info
        if self.check_state_sinfo.get():
            self.print_to_log_file(log_file=self.log_file, message=fun.show_system_info())






        #list for checked readings, later necessary
        self.checked_readings=[self.check_state_cpu.get(), self.check_state_gpu.get(), self.check_state_ram.get(), self.check_state_disc.get()]




        #if work time not defined, it is defined to one iteration only

        if self.check_state_wtime.get():
            self.work_time=simpledialog.askinteger("","Enter custom work time duration in seconds")
        else:
            self.work_time=0



        #getting interval for cpu reading
        if self.check_state_tinterval.get():
            self.cpu_time_interval=simpledialog.askfloat("","Enter customized interval for CPU readings.")
            if self.cpu_time_interval==None or self.cpu_time_interval<=0 :
                self.show_warning("CPU reading interval should be more than 0!")
                return
        else:
            self.cpu_time_interval=1



        #without customized work time - designed to work once
        if not self.work_time:
            self.print_readings(self.checked_readings, self.log_file, self.cpu_time_interval)





        #with customized work time
        elif self.work_time>=1:

            #get reading time interval
            if self.check_state_reading_interval.get():
                self.reading_interval=simpledialog.askinteger("","Enter reading interval in seconds")

            #reading time interval should be more or equal 1
                if self.reading_interval<1:
                    self.show_warning("Reading interval should be more or equal to 1 second")
                    return
                
            
            #if not customized - designed to work every second
            else:
                self.reading_interval=1
                    
            #blocking bigger interval than worktime situation
            if self.reading_interval>self.work_time:
                self.show_warning("Reading interval should be less or equal to work time")
                return
            

            if self.work_time<2:
                self.show_warning("Custom work time should be more or equal 2")
                return
            
            #variable for timetracking
            self.time_passed=0


            #main loop for readings with customized work time
            start=time.time()
            
            while True:
                end=time.time()
                time_passed=end-start
                if time_passed>=self.work_time:
                    break
                
                self.print_readings(self.checked_readings, self.log_file, self.cpu_time_interval)

                time.sleep(self.reading_interval)

           
                    

        #close logfile
        self.log_close(self.log_file)



    #basic function for printing readings to log file
    def print_readings(self, readings, log_file, cpu_interval):


        functions=[fun.cpu_usage(cpu_interval), fun.gpu_usage(), fun.ram_usage(), fun.disc_usage()]
        for i in range(4):
            if readings[i]==1:
                x=functions[i]
                y=x
                self.print_to_log_file(log_file, str(y)+"\n")


    def clear_log_file(self, log_file):
        log_file.seek(0)
        log_file.truncate()

    def log_close(self, log_file):
        if log_file:
            self.print_to_log_file(log_file, "Readings finished successfully!\n")
            log_file.close()

    def print_to_log_file(self,log_file, message):
        #basic log writing method

        log_file.write(message)





    def create_log_file(self):
        if self.check_state_log.get() == 1:
            self.custom_path = simpledialog.askstring("", "Enter custom log file path")

            if self.custom_path:
                self.log_file_path = os.path.join(self.custom_path, "log.txt")

                os.makedirs(self.custom_path, exist_ok=True)

                return open(self.log_file_path, "a")
            else:
                self.custom_path_checked_but_no_info = "Custom path checked but no path given"
                self.show_warning(self.custom_path_checked_but_no_info)
                return None

        elif self.check_state_log.get() == 0:
            self.log_file_path = "log.txt"
            return open(self.log_file_path, "a")



    def show_message(self, message):
        #function used for showing info
        messagebox.showinfo(title="PCMeter", message=message)




    def show_warning(self, warning):
        #function used for showing warnings
        messagebox.showwarning(title="PCMeter", message=warning)
