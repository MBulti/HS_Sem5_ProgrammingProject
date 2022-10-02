from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Recommendation:
    movie_id: int
    recommendations: list[int]