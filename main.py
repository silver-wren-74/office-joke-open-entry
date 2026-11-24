import os

LINE = "The office printer has shown 'low toner' since March. It isn't broken — it's just the only one here honest enough to admit it's running out."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
