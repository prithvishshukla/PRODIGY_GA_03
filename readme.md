# Markov Chain Text Generator

A Python implementation of a Markov Chain text generator that creates coherent text based on statistical patterns learned from training data.

## Features

- Configurable order (n-gram size) for different text generation styles
- Training on custom text input
- Automatic capitalization and punctuation handling
- Simple and extensible design

## Usage

```python
from markov_generator import MarkovChainTextGenerator

# Create generator with order 2 (considers 2 words for context)
generator = MarkovChainTextGenerator(order=2)

# Train on your text
text = "Your training text goes here..."
generator.train(text)

# Generate text
generated_text = generator.generate(length=50)
print(generated_text)
```

## Parameters

- `order`: Number of words used as context (default: 1)
- `length`: Number of words to generate (default: 100)

## Requirements

- Python 3.x
- No external dependencies (uses only built-in libraries)

## How it Works

1. **Training**: Analyzes input text to build a statistical model of word transitions
2. **Generation**: Uses the learned patterns to generate new text that follows similar structure
3. **Post-processing**: Capitalizes first word and ensures proper sentence ending

## Example Output

Input training text about Markov chains produces coherent sentences following similar patterns and vocabulary.
