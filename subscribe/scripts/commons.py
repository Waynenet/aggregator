# -*- coding: utf-8 -*-

# @Author  : wzdnzd
# @Time    : 2022-11-12

import json

import push
from logger import logger


def persist(config: push.PushConfig, data: dict, persist: dict, meta: str = "") -> None:
    try:
        pushtool = push.get_instance(config=config)
        if data is None or type(data) != dict or not pushtool.validate(config=persist):
            logger.debug(f"[{meta}] skip persist subscibes because fileid or data is empty")
            return

        pushtool.push_to(content=json.dumps(data), config=persist, group="subscribes")
    except:
        logger.error(f"[{meta}] occur error when persist subscribes")
