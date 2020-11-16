import re

from pytest_canon import assert_equals_ref, Config, set_global_config

from my_tested_library import generate_words


def my_assert(v1, v2):
    assert v1 == v2


set_global_config(Config(
    dir_path='tests/dumps',  # can be commented out
    env_var='PLS_UPDATE_REFS',  # can be commented out
    assert_func=my_assert,  # can be commented out
    # cast_func=hide_addresses, # can be uncommented
))


def hide_addresses(text):
    return re.sub(r'( at 0x)\w+', r'\1...',  text)


def test_generate_words():
    assert_equals_ref(
        value=generate_words(n=10000),
        name='test_generate_words',
        config=Config(
            # dir_path='tests/dumps',  # can be uncommented
            # env_var='PLS_UPDATE_REFS',  # can be uncommented
            # assert_func=my_assert,  # can be uncommented
            cast_func=hide_addresses,  # can be commented out
        )
    )


