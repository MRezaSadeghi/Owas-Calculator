import pandas as pd
import numpy as np
from typing import Tuple

from utils.logger import logger
import constants

class OwasCalculator:
    
    def __init__(self):
        # read owas data
        path = constants.OWAS_CAT_DATA_PATH
        self.owas_cat_data = pd.read_csv(path, header=None)
        self.owas_cat_data = np.array(self.owas_cat_data)

    def get_owas_action_category(
        self,
        *digits: Tuple[int, int, int, int]
        ):
        
        """
        digit 1: back
        digit 2: upper limb
        digit 3: lower limb
        digit 4: weight
        """
        
        if len(digits) != 4:
            raise KeyError("It needs only 4 digits to start calculation")
        
        row_index = (digits[0]-1)*3 + digits[2] - 1
        column_index = (digits[2]-1)*3 + digits[3] - 1
        
        logger.debug(f"back: {digits[0]}, upper limb: {digits[1]}")
        logger.debug(f"lower limb: {digits[2]}, weight: {digits[3]}")
        logger.debug(f"row_index: {row_index}, column_index: {column_index}")
        
        owas_cat = self.owas_cat_data[row_index, column_index]
        return owas_cat