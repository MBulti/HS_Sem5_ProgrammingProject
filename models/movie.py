from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Movie:
    id: int
    title: str