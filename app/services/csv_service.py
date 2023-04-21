import csv
from io import StringIO

from chardet.universaldetector import UniversalDetector


def detect_encoding(content: bytes) -> str:
    if content is None:
        raise TypeError("Content cannot be None")

    detector = UniversalDetector()
    detector.feed(content)
    detector.close()
    return detector.result["encoding"]


def read_csv(content: bytes, encoding: str) -> list:
    if content is None:
        raise TypeError("Content cannot be None")
    content_str = content.decode(encoding)
    reader = csv.reader(StringIO(content_str), delimiter=",", quotechar='"')
    return [row for row in reader]
