###
# Class to calculate CG based on Binay Mask

class Mechanic_Calc():
    name = "Mechanic Calculator"

    def __init__(self):
        pass

    # CG Calculator function
    def cg_calc_function(self, pixel_raster):
        # Go through Pixel List
        # Pixel must be a tuple of [x_pos, weight]
        # x_pos being the Position in either x or y
        # weight being 1 or 0 

        # Sum Values
        x_sum = 0
        y_sum = 0
        # Count all pixels with value -> 1
        count = 0

        # Position tracker
        x = 1
        y = 1
        
        for row in pixel_raster:
            for pixel in row:
                if pixel >= 1:
                    x_sum += x
                    y_sum += y
                    count += 1
                    
                # Increase X Position by 1
                x += 1
            
            # Reset X and move Y by 1
            x = 1
            y += 1

        # Now calculate the actual formula
        # Also checking if more than one pixel was available
        if count != 0:
            x_cg = x_sum / count
            y_cg = y_sum / count
        else:
            x_cg = 0
            y_cg = 0

        return x_cg, y_cg