"""
PRACTICAL CHALLENGE: TypedDict Structured Output Schema (LC-H1-P08)
=====================================================
ID: LC-H1-P08
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Define a `TypedDict` schema `MovieInfo` and a parsing function `validate_movie_dict(data)`
that ensures mandatory keys ('title', 'year', 'genres') and types exist.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from typing import TypedDict, List

class MovieInfo(TypedDict):
    title: str
    year: int
    genres: List[str]

def validate_movie_dict(data: dict) -> MovieInfo:
    if not isinstance(data.get("title"), str):
        raise TypeError("Title must be a string")
    if not isinstance(data.get("year"), int):
        raise TypeError("Year must be an integer")
    if not isinstance(data.get("genres"), list) or not all(isinstance(g, str) for g in data["genres"]):
        raise TypeError("Genres must be a list of strings")
    return MovieInfo(title=data["title"], year=data["year"], genres=data["genres"])

def test_typeddict_validation():
    data = {"title": "Inception", "year": 2010, "genres": ["Sci-Fi", "Action"]}
    result = validate_movie_dict(data)
    assert result["title"] == "Inception"
    assert result["year"] == 2010
    assert len(result["genres"]) == 2

if __name__ == '__main__':
    test_typeddict_validation()
    print("✓ Task 08 passed!")
