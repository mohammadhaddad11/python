def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    import alchemy.grimoire.light_validator as lv
    res = lv.validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({res})"
