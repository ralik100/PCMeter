
    def any_readings_checked(self):
        if  not self.check_state_cpu.get() and not self.check_state_disc.get() and not self.check_state_gpu.get() and not self.check_state_ram.get():
            self.no_reading_selected_warning="No reading selected"
            self.show_warning(self.no_reading_selected_warning)
            return False
        return True