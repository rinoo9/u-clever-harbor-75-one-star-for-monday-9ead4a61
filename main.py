"""Write a one-star review of Monday, as though Monday were a restaurant.

Entry for the make.fun bounty "One Star for Monday"
(u-clever-harbor-75-one-star-for-monday-9ead4a61): a single line of plain
text, at most 25 words and 1-180 characters.
"""

ENTRY = "Came in Monday for a fresh start. Got seated next to my alarm, charged for sunlight, and the Wi-Fi password was just 'no'."


def main() -> None:
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    words = line.split()
    if len(words) > 25:
        raise ValueError(f"entry has {len(words)} words, more than 25")
    if not 1 <= len(line) <= 180:
        raise ValueError(f"entry has {len(line)} characters, outside 1-180")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
