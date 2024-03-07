"""Converting the word received from the user to pig latin format"""
def vowel(letter):
    """To find out if it starts with a vowel"""
    letter =letter.lower()
    vowels =("a", "e", "i", "o", "u")
    for i in vowels:
        if i == letter:
            return True
    return False
def main():
    """Translating the word pig latin."""
    verb = input("Say a word! ").strip()
    verb_list = list(verb)
    if vowel(verb_list[0]):
        print("Here is pig latin version: "+ verb + "way")
    else:
        verb_list.append(verb_list[0].lower())
        verb_list.append("ay")
        verb_list.pop(0)
        verb_list= ''.join(verb_list)
        print("Here is pig latin version: " + verb_list)


if __name__ == "__main__":
    main()
