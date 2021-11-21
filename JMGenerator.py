from sys import argv
from src.Generation.Generator import Generator

if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage:')
        print('python3 JMGenerator.py ./ApiConfigFolder')
        exit(1)
    generator = Generator(argv[1])
    generator.run()
    exit(0)