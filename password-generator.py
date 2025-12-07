import random
import string

def generate_password(length) :
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter password length: "))
        
        if length < 5:
            print("Password length must be greater than 4.")
            return
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
