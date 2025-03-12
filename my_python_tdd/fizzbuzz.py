# fizzbuzz.py (リファクタ後)
def fizzbuzz(n: int) -> str:
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    if n % 7 == 0:
        result += "Bazz"
    return result or str(n)