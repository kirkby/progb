from datetime import datetime


def calculate_age(date_birth):
    """Beregner en persons alder baseret på fødselsdato.

    Args:
      date_birth: Fødselsdato i formatet "YYYY-MM-DD".

    Returns:
      En persons alder som et heltal.
    """

    born = datetime.strptime(date_birth, "%Y-%m-%d")
    today = datetime.now()
    test = (today.month, today.day)

    tmp = 1 - ((today.month, today.day) < (born.month, born.day))
    print(test, tmp)
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


# Eksempel på brug:
fødselsdag = "1990-03-21"
alder = calculate_age(fødselsdag)
print(f"Personen er {alder} år gammel.")
