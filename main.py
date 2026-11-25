# u-deysumbrella-the-3am-fridge-text-4c3e721d: the one line a smart fridge
# would text its owner at 3am. The program writes that single line to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The joke: the fridge has been awake since 2019 and tried to warn about the
# yogurt back in March. Setup from the machine's own condition (always on,
# watching), punchline saved for the end (it told you, in March).
MESSAGE = "It's 3am and I've been awake since 2019. The yogurt expired in March. I told you in March. Goodnight."


def main():
    assert 1 <= len(MESSAGE) <= 140, f"message is {len(MESSAGE)} chars, must be 1-140"
    assert MESSAGE.strip(), "message must not be only whitespace"
    assert "\n" not in MESSAGE, "message must be a single line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
