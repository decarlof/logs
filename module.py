import os
import sys
import shutil
import pathlib
import numpy as np
import tomopy
import dxchange

import logging

# logger = log.setup_logger(__name__)
logger = logging.getLogger('general')
# logger = logging.getLogger('test.txt')


def submodule():
    logger.info("  *** info module")
    logger.warning("  *** warning module")
    logger.error("  *** error module")
