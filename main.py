import logging
from log import info

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("hello world")
    info({"hello": "world"})


if __name__ == "__main__":
    main()
