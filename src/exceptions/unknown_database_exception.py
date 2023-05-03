class UnknownDatabaseException(Exception):
    """Exception raised when the database is unknown."""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)