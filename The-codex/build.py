import os

def write_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('elements.py', '''
def create_fire() -> str:
    return "Fire element created"


def create_water() -> str:
    return "Water element created"
''')

write_file('alchemy/elements.py', '''
def create_earth() -> str:
    return "Earth element created"


def create_air() -> str:
    return "Air element created"
''')

write_file('alchemy/potions.py', '''
import elements
from . import elements as alch_elements


def healing_potion() -> str:
    earth = alch_elements.create_earth()
    air = alch_elements.create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire = elements.create_fire()
    water = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
''')

write_file('alchemy/transmutation/recipes.py', '''
import elements
from ..elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    air = create_air()
    strength = strength_potion()
    fire = elements.create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and '{strength}' "
        f"mixed with '{fire}'"
    )
''')

write_file('alchemy/transmutation/__init__.py', '''
from . import recipes

__all__ = ["recipes"]
''')

write_file('alchemy/grimoire/__init__.py', '')

write_file('alchemy/grimoire/light_spellbook.py', '''
def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    import alchemy.grimoire.light_validator as lv
    res = lv.validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({res})"
''')

write_file('alchemy/grimoire/light_validator.py', '''
import alchemy.grimoire.light_spellbook as ls


def validate_ingredients(ingredients: str) -> str:
    allowed = ls.light_spell_allowed_ingredients()
    lower_ing = ingredients.lower()
    is_valid = any(ing in lower_ing for ing in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
''')

write_file('alchemy/grimoire/dark_spellbook.py', '''
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    res = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({res})"
''')

write_file('alchemy/grimoire/dark_validator.py', '''
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower_ing = ingredients.lower()
    is_valid = any(ing in lower_ing for ing in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
''')

write_file('alchemy/__init__.py', '''
from .elements import create_air
from . import potions
from .potions import healing_potion as heal
from . import transmutation

__all__ = ["create_air", "potions", "heal", "transmutation"]
''')

write_file('ft_alembic_0.py', '''
import elements


print("=== Alembic 0 ===")
print("Using: 'import ...' structure to access elements.py")
print(f"Testing create_fire: {elements.create_fire()}")
''')

write_file('ft_alembic_1.py', '''
from elements import create_water


print("=== Alembic 1 ===")
print("Using: 'from ... import ...' structure to access elements.py")
print(f"Testing create_water: {create_water()}")
''')

write_file('ft_alembic_2.py', '''
import alchemy.elements


print("=== Alembic 2 ===")
print("Accessing alchemy/elements.py using 'import ...' structure")
print(f"Testing create_earth: {alchemy.elements.create_earth()}")
''')

write_file('ft_alembic_3.py', '''
from alchemy.elements import create_air


print("=== Alembic 3 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print(f"Testing create_air: {create_air()}")
''')

write_file('ft_alembic_4.py', '''
import alchemy


print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="")
print(f"{alchemy.create_earth()}")
''')

write_file('ft_alembic_5.py', '''
from alchemy import create_air


print("=== Alembic 5 ===")
print("Accessing the alchemy module using 'from alchemy import ...'")
print(f"Testing create_air: {create_air()}")
''')

write_file('ft_distillation_0.py', '''
from alchemy import potions


print("=== Distillation 0 ===")
print("Direct access to alchemy/potions.py")
print(f"Testing strength_potion: {potions.strength_potion()}")
print(f"Testing healing_potion: {potions.healing_potion()}")
''')

write_file('ft_distillation_1.py', '''
import alchemy


print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {alchemy.potions.strength_potion()}")
print(f"Testing heal alias: {alchemy.heal()}")
''')

write_file('ft_transmutation_0.py', '''
import alchemy.transmutation.recipes


print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
''')

write_file('ft_transmutation_1.py', '''
import alchemy.transmutation


print("=== Transmutation 1 ===")
print("Import transmutation module directly")
print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
''')

write_file('ft_transmutation_2.py', '''
import alchemy


print("=== Transmutation 2 ===")
print("Import alchemy module only")
print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
''')

write_file('ft_kaboom_0.py', '''
import alchemy.grimoire.light_spellbook


print("=== Kaboom 0 ===")
print("Using grimoire module directly")
res = alchemy.grimoire.light_spellbook.light_spell_record(
    'Fantasy', 'Earth, wind and fire'
)
print(f"Testing record light spell: {res}")
''')

write_file('ft_kaboom_1.py', '''
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
import alchemy.grimoire.dark_spellbook  # noqa: F401
''')

print("Success")
