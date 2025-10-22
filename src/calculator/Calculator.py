import math

class Calculator:
    def __init__(self):
        self.maps = self._make_maps()

    def _make_maps(self):
        """Map numbers in multiple languages and numeral systems."""
        return {
            # digits
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            # English
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
            # German
            "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4,
            "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
            # Spanish
            "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
            "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
            # Russian
            "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
            "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
            # Chinese
            "零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
            # Roman numerals
            "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
            "VI": 6, "VII": 7, "VIII": 8, "IX": 9
        }

    def _to_number(self, x):
        """Convert input to number, handling text, roman, etc."""
        if isinstance(x, (int, float)):
            return x
        if isinstance(x, str):
            x = x.strip()
            if x.lower() in self.maps:
                return self.maps[x.lower()]
            if x.upper() in self.maps:
                return self.maps[x.upper()]
            try:
                return float(x)
            except ValueError:
                raise ValueError(f"Cannot convert '{x}' to number")
        raise TypeError(f"Unsupported type: {type(x)}")

    def add(self, a, b):
        return self._to_number(a) + self._to_number(b)

    def sub(self, a, b):
        return self._to_number(a) - self._to_number(b)

    def mul(self, a, b):
        return self._to_number(a) * self._to_number(b)

    def div(self, a, b):
        return self._to_number(a) / self._to_number(b)

    def factorize(self, n):
        """Return prime factors of n."""
        num = int(self._to_number(n))
        if num < 2:
            return [num]
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors

