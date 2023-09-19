class MyTelegramBotException(Exception):
    """Базовое исключение для ошибок, связанных с вашей библиотекой."""

class InvalidChatIdError(MyTelegramBotException):
    """Исключение, возникающее при недопустимом идентификаторе чата."""

class SendMessageError(MyTelegramBotException):
    """Исключение, возникающее при ошибке отправки сообщения."""
