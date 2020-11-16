import re

from pytest_canon import *

from my_tested_library import generate_long_text


def my_assert(v1, v2):
    assert v1.lower() == v2.lower()


set_global_dir_path('tests/dumps')  # optional
set_global_env_var('PLS_UPDATE_REFS')  # optional
set_global_assert_func(my_assert)  # optional
set_global_cast_func(lambda s: s.upper())  # optional


def test_generate_long_text():
    assert_equals_ref(
        generate_long_text(n=10000),
        'test_generate_long_text',
        dir_path='tests/dumps',  # optional
        env_var='PLS_UPDATE_REFS',  # optional
        assert_func=my_assert,  # optional
        cast_func=lambda s: s.upper(),  # optional
    )


