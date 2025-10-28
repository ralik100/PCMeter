import functions as fun
import log_manager as logger
import checker
import gui
import popup
import get_values as getter
import time

def start_reading(app):
        #main reading function


        #list for checked readings, later necessary, format = [CPU,GPU,RAM,DISC]
        checked_readings=[
            app.get_cpu_check_state(), 
            app.get_gpu_check_state(), 
            app.get_ram_check_state(), 
            app.get_disc_check_state()]

        if not checker.any_readings_checked(checked_readings):
            return
        




        #creating logfile
        log_file=logger.create_log_file(app.get_custom_log_path_check_state())

        




        #if creating log file went wrong, stop readings
        if log_file==0:
            popup.show_message("Readings stopped")
            return



        #clearing log file if checked
        if app.get_log_clear_check_state():
            logger.clear_log_file(log_file)



        #showing system info
        if app.get_system_info_check_state():
            logger.print_to_log_file(log_file=log_file, message=fun.show_system_info())






        



        #getting interval for cpu reading
        if app.get_cpu_custom_clock_interval_check_state():
            cpu_time_interval=getter.get_custom_cpu_clock_interval()
            if not cpu_time_interval:
                logger.log_close(log_file)
        else:
            cpu_time_interval=1



        #without customized work time - designed to work once
        if  not app.get_custom_work_time_check_state():
            logger.print_readings(checked_readings, log_file, cpu_time_interval)





        #with customized work time
        elif app.get_custom_work_time_check_state():

            work_time=getter.get_custom_work_time()
            if not work_time:
                logger.log_close(log_file)
                    

            if  app.get_custom_reading_interval_check_state():
                reading_interval=getter.get_custom_reading_interval()
                if reading_interval==False:
                    logger.log_close(log_file)

            else:
                reading_interval=1

            #blocking bigger interval than worktime situation
            if reading_interval>work_time:
                popup.show_warning("Reading interval should be less or equal to work time")
                return    
            



            #main loop for readings with customized work time
            start=time.time()
            
            while True:
                end=time.time()
                time_passed=end-start
                if time_passed>=work_time:
                    break
                
                logger.print_readings(checked_readings, log_file, cpu_time_interval)

                time.sleep(reading_interval)

           
                    

        #close logfile
        logger.log_close(log_file)
