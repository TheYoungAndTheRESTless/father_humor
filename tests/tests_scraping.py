import pytest
from src.father_humor_pip_package.main import dad_jokes

@pytest.mark.skip("testing proof of life")
def test_proof_of_life():
    sum = 1+1
    expected = 2
    assert sum == expected


# @pytest.mark.skip("testing proof of life")
def test_proof_of_life():
    sum = 1+1
    expected = 2
    assert sum == expected

# @pytest.mark.skip("testing proof of life")
def test_dad_jokes():
    url = "https://scraping-test-site.brendonlh.repl.co/"
    actual = dad_jokes(url)
    expected = '\'here is a fancy joke1 that is made of "li"tags'
    assert actual == expected

@pytest.mark.skip("testing proof of life")
def test_star_wars():
    sum = 1+1
    expected = 2
    assert sum == expected

@pytest.mark.skip("testing proof of life")
def test_programming():
    sum = 1+1
    expected = 2
    assert sum == expected