from enum import Enum, unique

@unique
class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    OK_STATUS = 200