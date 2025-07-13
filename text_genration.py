import random
from collections import defaultdict

class MarkovChainTextGenerator:
    def __init__(self, order=1):
        # Initialize the Markov chain with a given order (number of words in the state)
        self.order = order
        # The model stores possible next words for each state (tuple of words)
        self.model = defaultdict(list)

    def train(self, text):
        # Split the input text into words
        words = text.split()
        # Ensure the text is long enough for the chosen order
        if len(words) < self.order:
            raise ValueError("Text is too short for the given order")

        # Build the Markov model by iterating through the words
        for i in range(len(words) - self.order):
            # Create a key as a tuple of 'order' consecutive words
            key = tuple(words[i:i + self.order])
            # The next word following the key
            next_word = words[i + self.order]
            # Add the next word to the list of possible continuations for this key
            self.model[key].append(next_word)

    def generate(self, length=100):
        # Ensure the model has been trained before generating text
        if not self.model:
            raise ValueError("Model has not been trained")

        # Randomly select a starting key (state)
        current_key = random.choice(list(self.model.keys()))
        # Initialize the result with the starting key words
        result = list(current_key)

        # Generate words until the desired length is reached
        for _ in range(length - self.order):
            if current_key in self.model:
                # Randomly choose the next word from possible continuations
                next_word = random.choice(self.model[current_key])
                result.append(next_word)
                # Update the current key to the last 'order' words
                current_key = tuple(result[-self.order:])
            else:
                # Stop if there are no continuations for the current key
                break

        # Capitalize the first word
        result[0] = result[0].capitalize()
        # Ensure the last word ends with a sentence-ending punctuation
        if result[-1][-1] not in '.!?':
            result[-1] += '.'

        # Join the words into a single string and return
        return ' '.join(result)

# Example usage
if __name__ == "__main__":
    # Sample training text
    text = ("Markov chains are mathematical systems that undergo transitions "
            "from one state to another within a finite state space. They are named "
            "after Andrey Markov, a Russian mathematician. Markov chains are used "
            "in various fields, including statistics, economics, and computer science.")

    # Create a Markov chain generator with order 2 (bigrams)
    generator = MarkovChainTextGenerator(order=2)
    # Train the model with the sample text
    generator.train(text)
    # Generate and print a sequence of 50 words
    print(generator.generate(length=50))
