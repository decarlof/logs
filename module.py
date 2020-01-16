import logging

import log

logger = logging.getLogger(__name__)


def submodule():
    log.info("  *** info module")
    log.warning("  *** warning module")
    log.error("  *** error module")
