##   Log Generation Function   ##

def generate_log_positions(pond_position, pond_size, log_size):
    pond_x, pond_y = pond_position
    pond_width, pond_height = pond_size
    log_width, log_height = log_size

    log_x = pond_x + (pond_width - log_width) // 2

    log_positions = [
        (log_x, y) for y in range(pond_y, pond_y + pond_height, log_height) if y + log_height <= pond_y + pond_height
    ]

    return log_positions

#----------------------------------------------------------------------------------------------------------------------#