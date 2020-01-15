#!/usr/bin/env python

import os
import re
import sys
import argparse
import time
import shutil
import pathlib
from datetime import datetime


import log
import module

# # log file name
# logs_home = os.path.join(str(pathlib.Path.home()), 'logs')
# # make sure logs directory exists
# if not os.path.exists(logs_home):
#     os.makedirs(logs_home)
# lfname = os.path.join(logs_home, 'tomopy_' + datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S") + '.log')

lfname = 'test.txt'
logger = log.setup_old_logger(lfname)
# logger = log.setup_custom_logger(lfname)

logger.info("  *** info main")
logger.warning("  *** warning main")
logger.error("  *** error main")

module.submodule()

# def main():

#     parser = argparse.ArgumentParser()
#     parser.add_argument('--config', **config.SECTIONS['general']['config'])
#     parser.add_argument('--version', action='version',
#                         version='%(prog)s {}'.format(__version__))

#     tomo_params = config.RECON_PARAMS
#     find_center_params = config.RECON_PARAMS

#     cmd_parsers = [
#         ('init',        init,            (),                             "Create configuration file"),
#         ('recon',       run_rec,         tomo_params,                    "Run tomographic reconstruction"),
#         ('segment',     run_seg,         tomo_params,                    "Run segmentation on reconstured data"),
#         ('find_center', run_find_center, find_center_params,             "Find rotation axis location for all hdf files in a directory"),
#     ]

#     subparsers = parser.add_subparsers(title="Commands", metavar='')

#     for cmd, func, sections, text in cmd_parsers:
#         cmd_params = config.Params(sections=sections)
#         cmd_parser = subparsers.add_parser(cmd, help=text, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#         cmd_parser = cmd_params.add_arguments(cmd_parser)
#         cmd_parser.set_defaults(_func=func)

#     args = config.parse_known_args(parser, subparser=True)

#     # create logger
#     logs_home = args.logs_home

#     # make sure logs directory exists
#     if not os.path.exists(logs_home):
#         os.makedirs(logs_home)

#     # lfname = os.path.join(logs_home, 'tomopy_' + datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S") + '.log')
 
#     # logger.setup_logger(lfname)
#     # logger.info("Saving log at %s" % lfname)

#     try:
#         config.log_values(args)
#         args._func(args)
#     except RuntimeError as e:
#         logger.error(str(e))
#         sys.exit(1)


# if __name__ == '__main__':
#     main()

