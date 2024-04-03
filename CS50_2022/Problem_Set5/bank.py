"""Penalty based on greeting type"""
def main():
    """Input and output"""
    text=input("Greeting: ")
    print(value(text))


def value(greeting):
    """#Determine the situations how much it will take based on the answer"""
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return "$0"
    if "h" == greeting[0]:
        return "$20"
    return "$100"


if __name__ == "__main__":
    main()
