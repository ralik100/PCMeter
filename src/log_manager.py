  

def clear_log_file(self, log_file):
        log_file.seek(0)
        log_file.truncate()

def log_close(self, log_file):
        if log_file:
            self.print_to_log_file(log_file, "Readings finished successfully!\n")
            log_file.close()
        sys.exit(0)

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
        

    #basic function for printing readings to log file
    def print_readings(self, readings, log_file, cpu_interval):


        functions=[fun.cpu_usage(cpu_interval), fun.gpu_usage(), fun.ram_usage(), fun.disc_usage()]
        for i in range(4):
            if readings[i]==1:
                x=functions[i]
                y=x
                self.print_to_log_file(log_file, str(y)+"\n")



    def print_to_log_file(self,log_file, message):
        #basic log writing method

        log_file.write(message)
