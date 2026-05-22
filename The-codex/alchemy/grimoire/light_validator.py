import alchemy.grimoire.light_spellbook as ls


def validate_ingredients(ingredients: str) -> str:
    allowed = ls.light_spell_allowed_ingredients()
    lower_ing = ingredients.lower()
    is_valid = any(ing in lower_ing for ing in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
