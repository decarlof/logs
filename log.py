'''
    Log Lib for Sector 2-BM 
    
'''
import logging

# Logging defines
__GREEN = "\033[92m"
__RED = '\033[91m'
__YELLOW = '\033[33m'
__ENDC = '\033[0m'


info_extra={'endColor': __ENDC, 'color': __GREEN}
warn_extra={'endColor': __ENDC, 'color': __YELLOW}
error_extra={'endColor': __ENDC, 'color': __RED}


def info(msg):
    logger = logging.getLogger('general')
    # logger.info(msg, extra=info_extra)
    logger.info(info_extra['color']+ msg + info_extra['endColor'])

def error(msg):
    logger = logging.getLogger('general')
   # logger.error(msg, extra=error_extra)
    logger.error(error_extra['color']+ msg + error_extra['endColor'])

def warning(msg):
    logger = logging.getLogger('general')
    # logger.warning(msg, extra=warn_extra)
    logger.warning(warn_extra['color']+ msg + warn_extra['endColor'])


def setup_logger(lfname):
    logger = logging.getLogger('general')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    fhandler = logging.FileHandler(lfname)
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)

    chandler = logging.StreamHandler()
    chandler.setFormatter(formatter)
    chandler.setLevel(logging.DEBUG)
    logger.addHandler(chandler)

    return logger

def setup_old_logger(lfname, stream_to_console=True):

    logger = logging.getLogger('general')
    fHandler = logging.FileHandler(lfname)
    logger.setLevel(logging.DEBUG)
    # formatter = logging.Formatter("%(asctime)s %(info_extra['color'])s  %(message)s %(info_extra['endColor'])s")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fHandler.setFormatter(formatter)
    logger.addHandler(fHandler)
    if stream_to_console:
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        ch.setLevel(logging.DEBUG)
        logger.addHandler(ch)
    return logger

