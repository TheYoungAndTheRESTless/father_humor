import pytest
import os
from src.father_humor_pip_package.main import dad_jokes, star_wars, programming

url = "https://scraping-test-site.brendonlh.repl.co/"


# @pytest.mark.skip("testing proof of life")
def test_proof_of_life():
    sum = 1 + 1
    expected = 2
    assert sum == expected


# @pytest.mark.skip("testing proof of life")
def test_dad_jokes():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    if os.path.exists("dad_jokes.text"):
        os.remove("dad_jokes.text")
        actual = dad_jokes(url)
        expected = '\'here is a fancy joke1 that is made of "li"tags'
        assert actual == expected
    else:
        actual = dad_jokes(url)
        expected = '\'here is a fancy joke1 that is made of "li"tags'
        assert actual == expected


# @pytest.mark.skip("testing proof of life")
def test_star_wars():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    if os.path.exists("star_wars.text"):
        os.remove("star_wars.text")
        actual = star_wars(url)
        expected = '\'here is a fancy joke1 that is made of "p"tags'
        assert actual == expected
    else:
        actual = star_wars(url)
        expected = '\'here is a fancy joke1 that is made of "p"tags'
        assert actual == expected


# @pytest.mark.skip("testing proof of life")
def test_programming():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    if os.path.exists("programming.text"):
        os.remove("programming.text")
        actual = programming(url)
        expected = '\'here is a fancy joke1 that is made of "li"tags'
        assert actual == expected
    else:
        actual = programming(url)
        expected = '\'here is a fancy joke1 that is made of "li"tags'
        assert actual == expected

# @pytest.mark.skip("File Test")

# def file_test
