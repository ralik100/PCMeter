import functions as fun
import log_manager as logger
import checker
import popup
import get_values as getter
import time

def start_reading(self):
        #main reading function

        if not checker.any_readings_checked():
            return
        




        #creating logfile
        log_file=logger.create_log_file()

        




        #if creating log file went wrong, stop readings
        if log_file==0:
            popup.show_message("Readings stopped")
            return



        #clearing log file if checked
        if checker.check_state_clear_log_file.get():
            logger.clear_log_file(log_file)



        #showing system info
        if checker.check_state_sinfo.get():
            logger.print_to_log_file(log_file=log_file, message=fun.show_system_info())






        #list for checked readings, later necessary
        checked_readings=[checker.check_state_cpu.get(), checker.check_state_gpu.get(), checker.check_state_ram.get(), checker.check_state_disc.get()]





        



        #getting interval for cpu reading
        if checker.check_state_tinterval.get():
            cpu_time_interval=getter.get_custom_cpu_clock_interval()
            if not cpu_time_interval:
                logger.log_close(log_file)
        else:
            cpu_time_interval=1



        #without customized work time - designed to work once
        if  not self.check_state_wtime.get():
            self.print_readings(checked_readings, log_file, cpu_time_interval)





        #with customized work time
        elif self.check_state_wtime.get():

            work_time=self.get_custom_work_time()
            if not work_time:
                self.log_close(log_file)
                    

            if self.check_state_reading_interval.get():
                reading_interval=self.get_custom_reading_interval()
                if reading_interval==False:
                    self.log_close(log_file)

            else:
                reading_interval=1

            #blocking bigger interval than worktime situation
            if reading_interval>work_time:
                self.show_warning("Reading interval should be less or equal to work time")
                return    
            



            #main loop for readings with customized work time
            start=time.time()
            
            while True:
                end=time.time()
                time_passed=end-start
                if time_passed>=work_time:
                    break
                
                self.print_readings(checked_readings, log_file, cpu_time_interval)

                time.sleep(reading_interval)

           
                    

        #close logfile
        self.log_close(log_file)
