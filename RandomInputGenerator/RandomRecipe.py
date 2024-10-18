import random
import string

class RandomRecipe:
    def __init__(self, letter_count, number_count):
        self.letter_count = letter_count
        self.number_count = number_count

    def generate_random_string(self):
        letters = ''.join(random.choices(string.ascii_letters, k=self.letter_count))  # Generate random letters
        numbers = ''.join(random.choices(string.digits, k=self.number_count))          # Generate random digits
        return letters + numbers

    def generate_multiple_strings(self, count):
        return [self.generate_random_string() for _ in range(count)]

# Example usage:
generator = RandomRecipe(4,4)
random_strings = generator.generate_multiple_strings(10)
for s in random_strings:
    print(s)
