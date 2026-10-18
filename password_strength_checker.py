import string

password = input("Enter a password: ")
checks = [
	len(password) >= 8,
	any(char.islower() for char in password),
	any(char.isupper() for char in password),
	any(char.isdigit() for char in password),
	any(char in string.punctuation for char in password),
]

score = sum(checks)
strength = "Weak" if score < 3 else "Medium" if score < 5 else "Strong"
print(f"Password strength: {strength}")
