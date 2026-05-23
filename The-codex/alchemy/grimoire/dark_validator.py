from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower_ing = ingredients.lower()
    is_valid = False

    for ing in allowed:
        if ing in lower_ing:
            is_valid = True
            break

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
