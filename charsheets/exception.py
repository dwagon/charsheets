"""Exceptions relating to charsheets"""


class UnhandledException(Exception):
    """That option isn't handled yet"""

    pass


class NotDefined(Exception):
    """Charsheet needs to define something that they haven't"""

    pass


class InvalidOption(Exception):
    """Charsheet has defined something incorrectly"""

    pass


# EOF
