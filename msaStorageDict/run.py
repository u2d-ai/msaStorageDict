# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 SWelcker
"""
from loguru import logger

if __name__ == "__main__":
    from msaStorageDict import main

    logger.info("Starting msaStorageDict Services...")
    main.run()
