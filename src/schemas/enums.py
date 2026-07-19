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

    Subclasses may override `_proper_name_overrides()` for the rare member whose correct display
    name can't be mechanically derived from PascalCase splitting (e.g. an apostrophe, a hyphen, or
    a lowercase mid-phrase article) - every existing subclass that doesn't override it keeps the
    plain auto-derived behavior unchanged. A classmethod, not a plain class-body dict, because
    Enum's metaclass otherwise tries to turn a plain dict attribute into a member itself.
    """

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
        return "_".join(part.lower() for part in _split_words(name))

    @classmethod
    def _proper_name_overrides(cls) -> dict[str, str]:
        return {}

    @property
    def proper_name(self) -> str:
        if override := self._proper_name_overrides().get(self.name):
            return override
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


class Race(FroggeEnum):
    Aura = auto()
    Elezen = auto()
    FantasiaAddict = auto()
    Hrothgar = auto()
    Hyur = auto()
    Lalafell = auto()
    Miqote = auto()
    Roegadyn = auto()
    Viera = auto()
    Custom = auto()

    @classmethod
    def _proper_name_overrides(cls) -> dict[str, str]:
        return {"Aura": "Au Ra", "Miqote": "Miqo'te"}


class Clan(FroggeEnum):
    Dunesfolk = auto()
    Duskwight = auto()
    Helion = auto()
    Hellsguard = auto()
    Highlander = auto()
    KeeperOfTheMoon = auto()
    Midlander = auto()
    Plainsfolk = auto()
    Raen = auto()
    Rava = auto()
    SeaWolf = auto()
    SeekerOfTheSun = auto()
    TheLost = auto()
    Veena = auto()
    Wildwood = auto()
    Xaela = auto()
    Custom = auto()
    NA = auto()

    @classmethod
    def _proper_name_overrides(cls) -> dict[str, str]:
        return {"KeeperOfTheMoon": "Keeper of the Moon", "SeekerOfTheSun": "Seeker of the Sun"}


class Gender(FroggeEnum):
    Male = auto()
    Female = auto()
    NonBinary = auto()
    Custom = auto()

    @classmethod
    def _proper_name_overrides(cls) -> dict[str, str]:
        return {"NonBinary": "Non-Binary"}


class Pronoun(FroggeEnum):
    # 15 individually-selectable values (multi-select), deliberately not pre-grouped into
    # "He/Him/His" triads - matches v6's actual shape, and it lets someone pick any combination,
    # including neopronoun/mixed sets. No Custom option.
    He = auto()
    Him = auto()
    His = auto()
    She = auto()
    Her = auto()
    Hers = auto()
    They = auto()
    Them = auto()
    Theirs = auto()
    Ze = auto()
    Hir = auto()
    Per = auto()
    Pers = auto()
    It = auto()
    Its = auto()


class Orientation(FroggeEnum):
    Aromantic = auto()
    Asexual = auto()
    Bisexual = auto()
    Demiromantic = auto()
    Demisexual = auto()
    Gay = auto()
    Lesbian = auto()
    Pansexual = auto()
    Straight = auto()
    Custom = auto()


class DataCenter(FroggeEnum):
    Aether = auto()
    Crystal = auto()
    Dynamis = auto()
    Primal = auto()
    Light = auto()
    Chaos = auto()
    Materia = auto()
    Elemental = auto()
    Gaia = auto()
    Mana = auto()
    Meteor = auto()


class ApprovalStatus(FroggeEnum):
    Draft = auto()
    PendingApproval = auto()
    Approved = auto()
    Rejected = auto()


class ReactionRoleMessageType(FroggeEnum):
    Normal = auto()
    Unique = auto()
    Verify = auto()

    @property
    def description(self) -> str:
        return {
            ReactionRoleMessageType.Normal: "Clicking a role button toggles that role on or off.",
            ReactionRoleMessageType.Unique: "Clicking clears any other role from this panel first.",
            ReactionRoleMessageType.Verify: "Clicking adds the role; only an admin can remove it.",
        }[self]


class CardRarity(FroggeEnum):
    Common = auto()
    Uncommon = auto()
    Rare = auto()
    UltraRare = auto()
    Legendary = auto()

    @classmethod
    def _proper_name_overrides(cls) -> dict[str, str]:
        return {"UltraRare": "Ultra Rare"}

    @property
    def rank(self) -> int:
        """Ordinal position (0=Common..4=Legendary) for sorting/threshold comparisons - members
        aren't int-valued the way an IntEnum would be, so this is the explicit ordering hook."""
        return list(CardRarity).index(self)

    @property
    def accent_color(self) -> int:
        """Plain int hex - Schemas has zero framework dependencies beyond Pydantic. Bot-side
        code wraps this in discord.Colour(...) at render time."""
        return {
            CardRarity.Common: 0x808080,
            CardRarity.Uncommon: 0x00FF00,
            CardRarity.Rare: 0x0000FF,
            CardRarity.UltraRare: 0x800080,
            CardRarity.Legendary: 0xFFA500,
        }[self]

    @property
    def icon(self) -> str:
        return {
            CardRarity.Common: "⚪",
            CardRarity.Uncommon: "🟢",
            CardRarity.Rare: "🔵",
            CardRarity.UltraRare: "🟣",
            CardRarity.Legendary: "🟠",
        }[self]


class ComparableStat(FroggeEnum):
    """The 3 stats a Cards battle round can reveal for comparison (Phase 3). FLAW is
    deliberately not a member here - it's checked separately every round, never the revealed
    comparison stat."""
    Charm = auto()
    Wit = auto()
    Presence = auto()


class CardArrangement(FroggeEnum):
    """A curated, fixed set of card-art layouts a venue picks from per series - not a fully
    free-form per-venue coordinate system. The compositor always draws at the same pixel zones
    for a given arrangement, regardless of whose frame art is used."""
    ClassicBanner = auto()
    FullBleedScrim = auto()
    SidePanel = auto()
