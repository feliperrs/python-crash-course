from pathlib import Path

path = Path('10-cap_10\pi_digits.txt')
contents = path.read_text()
print(contents)
