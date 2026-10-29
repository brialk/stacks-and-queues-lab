def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())
    stack = []

    for char in s:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

if __name__ == "__main__":
    samples = ["()", "{[()]}", "([]{})", "(", "([)]", "(()"]
    print("=== Parentheses Validator (Stack) ===")
    for sample in samples:
        verdict = "VALID" if is_valid_parentheses(sample) else "INVALID"
        print(f"{sample!r:12} -> {verdict}")