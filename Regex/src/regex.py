import re

# Question 1

aus_phone_number = r'\d{3}-\d{3}-\d{4}'

print('Match' if re.findall(aus_phone_number, '123-456-7890') else 'No Match')
print('Match' if re.fullmatch(aus_phone_number, '123-456-789008') else 'No Match')

print()

# Question 2

email = r'[\w]+@[gmail|yahoo]+\.com'
print('Match' if re.fullmatch(email, 'diranoye@gmail.com') else 'No Match')
print('Match' if re.fullmatch(email, 'emmanuel@yahoo.com') else 'No Match')
print('Match' if re.fullmatch(email, 'baks@hgaf.com') else 'No Match')
print('Match' if re.fullmatch(email, 'djab@gmail.hagsy') else 'No Match')

print()

# Question 3

sentence = "Hello! How are you doing?"
print(sentence.split(" "))
print(re.split(" ", sentence))

print()

# Question 4

sentence_one = "Alice and Bob are Good Friends"
words = re.findall(r'\b[A-Z][a-zA-Z]*\b', sentence_one)

print(words)
print(len(words))