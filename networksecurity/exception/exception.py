import sys
from networksecurity.logging import logger





class networksecurityexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()


        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (f"error occured in file {self.file_name} in line number {self.lineno} error message {self.error_message}")



if __name__=="__main__":
    try:
        1/0

    except Exception as e:
        logger.logging.info("fuck ye")
        
        raise(networksecurityexception(e,sys))



    

