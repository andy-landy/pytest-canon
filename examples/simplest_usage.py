from pytest_canon import assert_equals_ref

from my_tested_library import generate_words


def test_generate_words():
    assert_equals_ref(generate_words(n=10000), 'test_generate_words')