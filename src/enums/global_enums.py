from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal to expected'
    WRONG_ELEMENT_NEXT_PAGE = 'Not expected text field'
    NO_ELEMENT = 'No such element'
