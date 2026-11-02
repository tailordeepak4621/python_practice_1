# Day 4 Solution
def character_counter(text: str) -> dict:
    counts = {}
    for char in text.lower():
        if char.isspace():
            continue
        # If key exists, increment; otherwise initialize at 0 and add 1
        counts[char] = counts.get(char, 0) + 1
    return counts

if __name__ == "__main__":
    sample_text = "Daily Python Practice"
    result = character_counter(sample_text)
    print(f"Character counts for '{sample_text}':\n{result}")
