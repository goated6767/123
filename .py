import random
import string

def generate_password(length=12):
    """Generates a secure random password of a given length."""
    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_characters = letters + digits + symbols
    
    # Ensure the password has at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
        
    # Shuffle the list to make it unpredictable
    random.shuffle(password)
    
    # Join the list into a single string
    return "".join(password)

if __name__ == "__main__":
    # Example usage: Generate a 16-character password
    secure_password = generate_password(16)
    print(f"Generated Password: {secure_password}")
