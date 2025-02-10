from owas import OwasCalculator
from utils.logger import logger

owas_calc = OwasCalculator()
oac = owas_calc.get_owas_action_category(1, 1, 1, 1)
logger.info(f"Owas Action Category: {oac}")