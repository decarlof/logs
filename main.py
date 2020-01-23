#!/usr/bin/env python

import os
import pathlib
from datetime import datetime

import log
import module

# log file name
logs_home = os.path.join(str(pathlib.Path.home()), 'logs')
# make sure logs directory exists
if not os.path.exists(logs_home):
    os.makedirs(logs_home)
lfname = os.path.join(logs_home, 'test_' + datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S") + '.log')

log.setup_custom_logger(lfname)
logger = log.logger

logger.info("  *** info main")
logger.warning("  *** warning main")
logger.error("  *** error main")

module.submodule()



