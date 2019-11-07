import enum


@enum.unique
class EntityTexture(enum.Enum):
    """Represent the set of sprites for an entity."""
    MAN = 0
    WOMAN = 1
