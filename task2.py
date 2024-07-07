from collections import deque


def is_palindrome(s):
    s = s.lower().replace(" ", "")

    char_queue = deque()

    for char in s:
        char_queue.append(char)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True
