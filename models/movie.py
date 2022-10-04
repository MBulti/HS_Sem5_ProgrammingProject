from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Movie:
    id: int
    release_year: str
    title: str
