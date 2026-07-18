import re
from enum import StrEnum, auto


def _split_words(member: str) -> list[str]:
    """
    Split a CamelCase or PascalCase member name into words, keeping acronyms together.

    Examples:
        "DatabaseLoadingManagerObject" -> ["Database", "Loading", "Manager", "Object"]
        "HTTPRequestHandler" -> ["HTTP", "Request", "Handler"]
        "FFXIVRPVenueBot" -> ["FFXIV", "RP", "Venue", "Bot"]
    """
    return re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z][a-z]+|[A-Z]+|\d+", member)


class FroggeEnum(StrEnum):
    """
    A string enum whose members double as their own wire-format value - so they validate,
    serialize, and store identically to a plain str - plus a proper_name property that turns
    a PascalCase member name into a human-readable label, e.g. PartiallyRedeemed -> "Partially Redeemed".

    Values are auto-derived (snake_case of the member name) rather than typed out, so there's
    no separate literal to keep in sync when adding a member.
    """

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
        return "_".join(part.lower() for part in _split_words(name))

    @property
    def proper_name(self) -> str:
        return " ".join(_split_words(self.name))


class Repeatability(FroggeEnum):
    Monthly = auto()
    Renewable = auto()
    OneTime = auto()


class RedemptionLevel(FroggeEnum):
    FullyRedeemed = auto()
    PartiallyRedeemed = auto()
    NotRedeemed = auto()


class DisplayType(FroggeEnum):
    Roster = auto()
    Perks = auto()


class VIPMessageTemplateType(FroggeEnum):
    Welcome = auto()
    Warning = auto()
    Expiry = auto()


class ElementType(FroggeEnum):
    Address = auto()
    Theme = auto()
    Syncshell = auto()
    PartyFinder = auto()
    ShoutRun = auto()
    Greeting = auto()
    VenueShout = auto()
    DJInfo = auto()
    Miscellaneous = auto()
