import os
import sys
import shutil
import pathlib
import numpy as np
import tomopy
import dxchange
import logging

import log
# logger = log.setup_logger(__name__)
logger = logging.getLogger('general')
# logger = logging.getLogger('test.txt')


def submodule():
    log.info("  *** info module")
    log.warning("  *** warning module")
    log.error("  *** error module")
