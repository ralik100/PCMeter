import tkinter as tk


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

        self.check_state_results_to_chart=tk.IntVar()
        self.checkbox_results_to_chart=tk.Checkbutton(self.checkbox_options_frame, text="results to chart", font=("Arial",10), variable=self.check_state_results_to_chart)
        self.checkbox_results_to_chart.grid(row=1,column=2, sticky=tk.W+tk.E)

        #options header
        self.options_header=tk.Label(self.root, text="Select your options", font=("Arial Black",15))
        self.options_header.pack(padx=5, pady=5)

        self.checkbox_options_frame.pack(fill="x", padx=10, pady=10)


        self.start_button=tk.Button(self.root, text="Start reading", font=("Arial Black",20), command=rd.start_reading)
        self.start_button.pack(padx=10, pady=50)

    


    def run(self):
        self.root.mainloop()