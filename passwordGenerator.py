import string
import random

def generate_password(length,use_digits=True,use_uppercase=True,use_lowercase=True,use_special_chars=True):
     # if length is false-> no value
     if not length:
          return 
     else:
          if use_lowercase:
               lower_letters=string.ascii_lowercase
          else:
               lower_letters=""
          # if uppercase is true
          if use_uppercase:
               uppercase_letters=string.ascii_uppercase 
          else:
               uppercase_letters=""     
          if use_digits:
               digits = string.digits if use_digits else ''  
          special_chars = string.punctuation if use_special_chars else ''    

          # combine all characters and numbers
          all_characters=lower_letters+digits+uppercase_letters+special_chars

          if not all_characters:
                raise ValueError("At least one character set must be selected.")
          #  generate the password
          password=[]
          for _ in range(0,length):
               chars=random.choice(all_characters)
               password.append(chars)
          # join all the chars in a single string

          return "".join(password)
     

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
     #    strip=for remving extra space , lower=for coverting in lower and == 'yes' evaluates to True.
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a positive integer for the length.")

# Run the password generator
main()
