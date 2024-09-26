import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace ellipsis with a period to handle cases like "Woo..."
        cleaned_value = self.value.replace('...', '.')
        # Split on common sentence-ending punctuation
        sentences = [s.strip() for s in re.split('[.!?]+', cleaned_value) if s.strip()]
        return len(sentences)


# Test cases
if __name__ == "__main__":
    # Test basic functionality
    string1 = MyString("This is a string! It has three sentences. Right?")
    print(f"Number of sentences: {string1.count_sentences()}")
    print(f"Is question: {string1.is_question()}")
    print(f"Is sentence: {string1.is_sentence()}")
    print(f"Is exclamation: {string1.is_exclamation()}")

    # Test complex case
    string2 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
    print(f"Number of sentences in complex string: {string2.count_sentences()}")

    # Test empty string
    string3 = MyString()
    print(f"Number of sentences in empty string: {string3.count_sentences()}")

    # Test single sentence with different endings
    print(MyString("This is a sentence.").is_sentence())
    print(MyString("Is this a question?").is_question())
    print(MyString("This is exciting!").is_exclamation())

    # Test invalid input
    MyString(123)  # This should print "The value must be a string."