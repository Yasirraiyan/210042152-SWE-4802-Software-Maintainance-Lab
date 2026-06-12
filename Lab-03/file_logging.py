from loguru import logger
logger.add("a.log", format="{time} | {level} | {message}",) 
logger.info("User logged in")
logger.error("Login Failed")