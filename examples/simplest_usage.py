from pytest_canon import assert_equals_ref

from my_tested_library import generate_long_text


def test_generate_long_text():
    assert_equals_ref(generate_long_text(n=10000), 'test_generate_long_text')