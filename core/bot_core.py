from abc import ABC, abstractmethod
from typing import Union

from telegram.ext import Updater, CommandHandler, MessageHandler
import logging

logger = logging.getLogger(__name__)


class TelegramBot(ABC):
    token: str

    def __init__(self):
        self.updater = Updater(self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.init_event()

    def start(self):
        logger.warning(f"Bot {self.__class__.__name__} is started!")
        self.updater.start_polling()

    def add_handler(self, func: Union[CommandHandler, MessageHandler]):
        self.dispatcher.add_handler(func)
        return self

    @abstractmethod
    def init_event(self):
        raise NotImplementedError
