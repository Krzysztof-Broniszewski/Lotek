# lotto.py
from __future__ import annotations
import random
from dataclasses import dataclass
from typing import Iterable, Set

POOL_START, POOL_END = 1, 49        # zakres 1..49 włącznie
DRAW_COUNT = 6

@dataclass(frozen=True)
class LottoResult:
    drawn: Set[int]
    hits: Set[int]

    @property
    def hit_count(self) -> int:
        return len(self.hits)

def polish_plural_liczba(n: int) -> str:
    """
    Zwraca poprawny dopełniacz biernika słowa 'liczba':
    1 -> 'liczbę', 2-4 (z wyjątkiem 12-14) -> 'liczby', reszta (w tym 0, 5-21, 12-14) -> 'liczb'
    """
    if n == 1:
        return "liczbę"
    if 12 <= n % 100 <= 14:
        return "liczb"
    if n % 10 in (2, 3, 4):
        return "liczby"
    return "liczb"

def validate_user_numbers(nums: Iterable[int]) -> Set[int]:
    s = set(nums)
    if len(s) != DRAW_COUNT:
        raise ValueError(f"Podaj dokładnie {DRAW_COUNT} unikalnych liczb (otrzymano {len(s)}).")
    if not all(POOL_START <= n <= POOL_END for n in s):
        raise ValueError(f"Wszystkie liczby muszą być w zakresie {POOL_START}..{POOL_END}.")
    return s

def lotto_draw(user_numbers: Iterable[int], *, seed: int | None = None) -> LottoResult:
    user = validate_user_numbers(user_numbers)
    rng = random.Random(seed)
    drawn = set(rng.sample(range(POOL_START, POOL_END + 1), DRAW_COUNT))
    hits = user & drawn
    return LottoResult(drawn=drawn, hits=hits)

if __name__ == "__main__":
    # przykładowe moje liczby:
    my_numbers = {6, 11, 18, 23, 32, 48}

    result = lotto_draw(my_numbers)  # możesz dodać seed=1234 dla powtarzalności
    drawn_sorted = sorted(result.drawn)
    hits_sorted = sorted(result.hits)

    numeral = polish_plural_liczba(result.hit_count)

    print(f"Wszystkie liczby (1..49): {list(range(POOL_START, POOL_END+1))}")
    print(f"Wylosowane liczby: {drawn_sorted}")
    print(f"Moje liczby:       {sorted(my_numbers)}")
    print(f"Trafione liczby:   {hits_sorted if hits_sorted else '—'}")
    print(f"Udało Ci się trafić: {result.hit_count} {numeral}{'' if result.hit_count == 0 else ' ' + str(hits_sorted)}")
