class BudgetError(Exception):
    def __init__(self, message: str, hint: str = "입력값과 --help 안내를 확인하세요.") -> None:
        super().__init__(message)
        self.hint = hint


class DataError(BudgetError):
    pass
