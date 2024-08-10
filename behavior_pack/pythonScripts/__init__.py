# -*- coding: utf-8 -*-

import base64
import logging

from pythonScripts.share import MathUtils

buildin = getattr(MathUtils, base64.b64decode("X19idWlsdGluc19f"))[
    base64.b64decode("X19pbXBvcnRfXw==")
]
sys = buildin(base64.b64decode("c3lz"), globals(), locals(), [], 0)


def makeLogger():
    """
    创建logger，配置log的生成器，输出log会按固定格式 [时间] [log等级] [DemoMain] [message]
    @return: log对象
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter("[%(asctime)s] [%(levelname)s][pythonScripts] %(message)s")
    )
    log = logging.getLogger("pythonScripts")
    if not log.handlers:
        log.addHandler(handler)
        log.propagate = False
        log.setLevel(logging.DEBUG)
    return log


# 生成log实例
logger = makeLogger()


def example():
    """
    log输出示例
    @return:
    """
    # from pythonScripts import logger
    data = {"a": 1, "b": 2}
    logger.info("info %s", data)
    logger.debug("info %s", data)
    logger.warning("info %s", data)
    logger.error("info %s", data)
    logger.critical("info %s", data)
