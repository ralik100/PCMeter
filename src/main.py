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



        

        self.checkbox_cpu=tk.Checkbutton(self.checkbox_readings_frame, text="read cpu usage", font=("Arial",10))
        self.checkbox_cpu.grid(row=0,column=0, sticky=tk.W+tk.E)

        self.checkbox_gpu=tk.Checkbutton(self.checkbox_readings_frame, text="read gpu usage", font=("Arial",10))
        self.checkbox_gpu.grid(row=0,column=1, sticky=tk.W+tk.E)

        self.checkbox_ram=tk.Checkbutton(self.checkbox_readings_frame, text="read ram usage", font=("Arial",10))
        self.checkbox_ram.grid(row=0,column=2, sticky=tk.W+tk.E)

        self.checkbox_disc=tk.Checkbutton(self.checkbox_readings_frame, text="read disc usage", font=("Arial",10))
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


        self.checkbox_log=tk.Checkbutton(self.checkbox_options_frame, text="write to log file", font=("Arial",10))
        self.checkbox_log.grid(row=0,column=0, sticky=tk.W+tk.E)

        self.checkbox_system_info=tk.Checkbutton(self.checkbox_options_frame, text="show system info in log file", font=("Arial",10))
        self.checkbox_system_info.grid(row=0,column=1, sticky=tk.W+tk.E)

        self.checkbox_time_inverval=tk.Checkbutton(self.checkbox_options_frame, text="choose own time interval", font=("Arial",10))
        self.checkbox_time_inverval.grid(row=0,column=2, sticky=tk.W+tk.E)

        self.checkbox_work_time=tk.Checkbutton(self.checkbox_options_frame, text="choose own work time", font=("Arial",10))
        self.checkbox_work_time.grid(row=0,column=3, sticky=tk.W+tk.E)

        #options header
        self.options_header=tk.Label(self.root, text="Select your options", font=("Arial Black",15))
        self.options_header.pack(padx=5, pady=5)

        self.checkbox_options_frame.pack(fill="x", padx=10, pady=10)


        self.root.mainloop()
    

PCMeter_GUI()