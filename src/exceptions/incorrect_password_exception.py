class IncorrectPasswordException(Exception):
    """Exception raised when the password is incorrect."""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)