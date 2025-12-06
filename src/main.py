from dotenv import load_dotenv
import os

print('Hello from repository')

def print_author():
    load_dotenv()
    author = os.getenv('AUTHOR')
    return author

print(f"Автор проекта: {print_author()}")

