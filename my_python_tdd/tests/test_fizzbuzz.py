# tests/test_fizzbuzz.py

import pytest
# これから fizzbuzz.py から関数をインポートする予定ですが
# まだ fizzbuzz.py は書いていないので、この段階ではコメントアウトなどしておく

from fizzbuzz import fizzbuzz

def test_fizzbuzz_return_number():
    # 例えば、1 を渡したら "1" という文字列が返ってくるはずだ、
    # というテストを書きます
    assert fizzbuzz(1) == "1"

def test_fizzbuzz_return_fizz():
    # 3の倍数なら "Fizz"
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz_return_buzz():
    # 5の倍数なら "Buzz"
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz_return_fizzbuzz():
    # 15の倍数なら "FizzBuzz"
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_return_bazz():
    assert fizzbuzz(7) == "Bazz"
