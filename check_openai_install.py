import openai

try:
    print(openai.__version__)
except ImportError:
    print("openai library is not installed. Please install it using 'pip install openai'")