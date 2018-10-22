# -*- coding: utf-8 -*-
"""
    pip_services_messaging.build.MemoryMessageQueueFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    MemoryMessageQueueFactory implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services_commons.refer import Descriptor
from pip_services_components.build import Factory
from ..queues.MemoryMessageQueue import MemoryMessageQueue

_Descriptor = Descriptor("pip-services-net", "factory", "message-queue", "memory", "1.0")
MemoryQueueDescriptor = Descriptor("pip-services-net", "message-queue", "memory", "*", "*")

class MemoryMessageQueueFactory(Factory):
    def register(self, locator, factory):
        descriptor = locator
        return MemoryMessageQueue(descriptor.get_name())