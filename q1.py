import sys

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = [str(i) for i in range(1, 10)]
words_digits = words + digits
words2digit = {w: str(i + 1) for i, w in enumerate(words)}

def line_to_digit(line: str, right: bool) -> str:
    def find(word):
        fn = line.rfind if right else line.find
        idx = fn(word)
        if idx < 0:
            return float('inf')
        return -idx if right else idx

    num = min(words_digits, key=find)
    return words2digit.get(num, num)

def calibration_value(line: str) -> int:
    first = line_to_digit(line, False)
    last = line_to_digit(line, True)
    return int(first + last)

print(sum(calibration_value(line) for line in sys.stdin))
