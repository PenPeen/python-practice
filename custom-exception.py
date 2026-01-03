class TestException(Exception):
    pass

# raise TestException("例外が発生しました。")

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# raise ValidationError("例外が発生しました。")
