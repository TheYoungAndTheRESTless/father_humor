import pytest
import os
import random
import requests
from src.father_humor_pip_package.scraper import dad_jokes, star_wars, programming


# @pytest.mark.skip("testing proof of life")
def test_proof_of_life():
    sum = 1 + 1
    expected = 2
    assert sum == expected


# @pytest.mark.skip("testing proof of life")
def test_dad_jokes_scrape():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    actual = dad_jokes(url)
    expected = '\'here is a fancy joke that is made of "li"tags'
    assert actual == expected


# @pytest.mark.skip("test_dad_jokes_text")
def test_dad_jokes_text():
    with open('dad_jokes.text') as dj:
        rand_joke = dj.readlines()
    actual = rand_joke[0]
    expected = '\'here is a fancy joke that is made of "li"tags\n'
    assert actual == expected


# @pytest.mark.skip("test_star_wars_scrape")
def test_star_wars_scrape():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    actual = star_wars(url)
    expected = '\'here is a fancy joke that is made of "p"tags'
    assert actual == expected


# @pytest.mark.skip("test_star_wars_text")
def test_star_wars_text():
    with open('star_wars.text') as sw:
        rand_joke = sw.readlines()
    actual = rand_joke[0]
    expected = '\'here is a fancy joke that is made of "p"tags\n'
    assert actual == expected


# @pytest.mark.skip("test_programming_scrape")
def test_programming_scrape():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    actual = programming(url)
    expected = '\'here is a fancy joke that is made of "li"tags'
    assert actual == expected


# @pytest.mark.skip("test_programming_text")
def test_programming_text():
    with open('programming.text') as pr:
        rand_joke = pr.readlines()
        actual = rand_joke[0]
        expected = '\'here is a fancy joke that is made of "li"tags\n'
        assert actual == expected


# @pytest.mark.skip("test_file_exist_dad_jokes")
def test_file_exist_dad_jokes():
    actual = os.path.exists("dad_jokes.text")
    expected = True
    assert actual == expected


# @pytest.mark.skip("test_file_exist_starwars")
def test_file_exist_starwars():
    actual = os.path.exists("star_wars.text")
    expected = True
    assert actual == expected


# @pytest.mark.skip("test_file_exist_programming")
def test_file_exist_programming():
    actual = os.path.exists("programming.text")
    expected = True
    assert actual == expected
