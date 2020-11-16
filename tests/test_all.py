import pytest

from pytest_canon import assert_equals_ref, Config, set_global_config


def test_read_correct():
    assert_equals_ref('value1', 'name1')


def test_read_incorrect():
    with pytest.raises(AssertionError):
        assert_equals_ref('value2', 'name1')


def test_read_new():
    with pytest.raises(FileNotFoundError):
        assert_equals_ref('value', 'new_name')


def test_local_config():
    assert_equals_ref('value1xxx', 'name1', Config(cast_func=lambda s: s.replace('x', '')))


def test_global_config():
    pass


def test_global_and_local_config():
    pass


def test_write():
    pass
