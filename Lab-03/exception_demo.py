from loguru import logger
@logger.catch(level="CRITICAL",message="Not Good")
def funcl(a,b):
    return a/b
funcl(2,0)