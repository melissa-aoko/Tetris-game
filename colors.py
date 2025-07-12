class Colors:
    
    dark_grey   = (26, 31, 40)
    cyan        = (163, 216, 244) 
    yellow      = (255, 246, 165)  
    purple      = (217, 184, 255)  
    mint_green  = (182, 245, 216)  
    coral_pink  = (255, 181, 181)  
    peach       = (255, 209, 164)  
    rose        = (255, 183, 227)  
    white       = (255,255,255)
    blush_pink= (255, 233, 236)
    light_blue= (59, 85,162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey,cls.cyan, cls.yellow, cls.purple, cls.mint_green, cls.coral_pink, cls.peach, cls.rose]
