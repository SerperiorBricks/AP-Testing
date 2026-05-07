# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class ChestSanity(Toggle):
    """Make opening each chest a check (NOTE: some may be missable)"""
    display_name = "Chest Sanity"

class EventSanity(DefaultOnToggle):
    """Make each event (glowing squares in each chapter) a check"""
    display_name = "Event Sanity"

class ProgressiveWeapons(DefaultOnToggle):
    """Lock using better weapon ranks behind items (E->D->C->B->A). E is always available. 1 extra by default"""
    display_name = "Progressive Weapons"

class ExtraProgressiveWeapons(Toggle):
    """Add 5 more progressive weapon ranks for each weapon type. Does nothing if progessive_weapons is off"""
    display_name = "Extra Progressive Weapons"

class EarlyGaius(Toggle):
    """Force Gaius into sphere 1 so chests are easier to open"""
    display_name = "Early Gaius"

class EarlyDonnel(Toggle):
    """Force Donnel into sphere 1 so paralogue 1 is accessible earlier"""
    display_name = "Early Donnel"

class FreeSupports(Toggle):
    """Allows the player to grind supports for characters they otherwise can't use. Effectively allows child paralogue access much sooner."""
    display_name = "Free Supports"

class ParalogueGates(DefaultOnToggle):
    """Adds paralogue gating items similar to the main chapter progression items, but individual for each paralogue"""
    display_name = "Paralogue Gating Items"

class GrimaRequiresParentUnits(DefaultOnToggle):
    """Make Grima require all parent units being unlocked to be logically accessible."""
    display_name = "Grima Requires Parent Units"

class GrimaRequiresAllUnits(Toggle):
    """Make Grima require all units to be logically accessible. Overrides Grima Reqires Parent Units"""
    display_name = "Grima Requires All Units"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["free_supports"] = FreeSupports
    options["grima_requires_parent_units"] = GrimaRequiresParentUnits
    options["grima_requires_all_units"] = GrimaRequiresAllUnits
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    options.type_hints["chest_sanity"] = ChestSanity
    options.type_hints["event_sanity"] = EventSanity
    options.type_hints["progressive_weapons"] = ProgressiveWeapons
    options.type_hints["extra_progressive_weapons"] = ExtraProgressiveWeapons
    options.type_hints["early_gaius"] = EarlyGaius
    options.type_hints["early_donnel"] = EarlyDonnel
    options.type_hints["paralogue_gates"] = ParalogueGates

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
