from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower_ing = ingredients.lower()
    is_valid = any(ing in lower_ing for ing in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
