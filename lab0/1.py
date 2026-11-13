def format_initials(full_name: str) -> str:
    name_parts = full_name.split()
    last_name = name_parts[0].capitalize()
    first_initial = name_parts[1][0].upper()
    second_initial = name_parts[2][0].upper()
    return f"{last_name} {first_initial}.{second_initial}."



if __name__ == "__main__":
    name = input("Введите имя: ").strip().lower()
    print(format_initials(name))