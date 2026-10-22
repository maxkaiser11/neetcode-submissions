def remove_fourth_character(word: str) -> str:
    first = word[:3]
    new = word[4:]
    return first + new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
