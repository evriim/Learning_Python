"""Remove vowels and rewrite the word"""
vowels = {"A","a","E","e","I","i","O","o","U","u"}

def main():
    """Retrieving data from the user and printing it"""
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    """Vowels are removed."""
    for _ in word:
        for i in vowels:
            if _ == i :
                word= word.replace(_,"")
            else:
                continue
    return word

if __name__ == "__main__":
    main()
