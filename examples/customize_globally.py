import re

from pytest_canon import assert_equals_ref, Config, set_global_config


from my_tested_library import generate_words


def my_assert(v1, v2):
    assert v1 == v2


def hide_addresses(text):
    return re.sub(r'( at 0x)\w+', r'\1...',  text)


set_global_config(Config(
    dir_path='tests/dumps',
    env_var='PLS_UPDATE_REFS',
    assert_func=my_assert,
    cast_func=hide_addresses,
))


def test_generate_words():
    assert_equals_ref(generate_words(n=10000), 'test_generate_words')
