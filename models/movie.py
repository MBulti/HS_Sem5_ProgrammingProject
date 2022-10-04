from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Movie:
    id: str
    release_year: str
    title: str
