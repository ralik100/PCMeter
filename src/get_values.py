from tkinter import simpledialog
import popup

def get_custom_cpu_clock_interval(self):
        cpu_time_interval=simpledialog.askfloat("","Enter customized interval for CPU readings.")
        if cpu_time_interval==None or cpu_time_interval<=0 :
            popup.show_warning("CPU reading interval should be more than 0!")
            return False
        
        return cpu_time_interval

def get_custom_work_time(self):

        work_time=simpledialog.askinteger("","Enter custom work time duration in seconds")

        if work_time==None or work_time<2:
                popup.show_warning("Custom work time should be more or equal 2")
                return False
        
        return work_time

def get_custom_reading_interval(self):
            #get reading time interval

        reading_interval=simpledialog.askinteger("","Enter reading interval in seconds")

        #reading time interval should be more or equal 1
        if reading_interval==None or reading_interval<1:
            popup.show_warning("Reading interval should be more or equal to 1 second")
            return False
        
        return reading_interval