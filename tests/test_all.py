import os
import uuid
from contextlib import contextmanager

import pytest

from pytest_canon import (
    assert_equals_ref,
    set_global_dir_path,
    set_global_env_var,
    set_global_cast_func,
    set_global_assert_func,
    global_dir_path,
    global_env_var,
    global_assert_func,
    global_cast_func,
)


def test_read_correct():
    assert_equals_ref('value1', 'name1')


def test_read_incorrect():
    with pytest.raises(AssertionError):
        assert_equals_ref('new_value', 'name1')


def test_read_new():
    with pytest.raises(FileNotFoundError):
        assert_equals_ref('new_value', 'new_name')


def test_write(tmp_path):
    with temp_env_var() as env_var:
        assert_equals_ref('new value', 'new_name', dir_path=tmp_path, env_var=env_var)
    assert_equals_ref('new value', 'new_name', dir_path=tmp_path, env_var=env_var)


def test_dir_path(tmp_path):
    with pytest.raises(FileNotFoundError):
        assert_equals_ref('value1', 'name1', dir_path=tmp_path)


def test_env_var(tmp_path):
    with temp_env_var() as env_var:
        assert_equals_ref('new value', 'new_name', dir_path=tmp_path, env_var=env_var)


def test_assert_func():
    assert_equals_ref('VALUE1', 'name1', assert_func=custom_assert)
    with pytest.raises(AssertionError):
        assert_equals_ref('NEW VALUE1', 'name1', assert_func=custom_assert)


def test_cast_func():
    assert_equals_ref('VALUE1', 'name1', cast_func=lambda s: s.lower())
    with pytest.raises(AssertionError):
        assert_equals_ref('NEW VALUE1', 'name1', cast_func=lambda s: s.lower())


def test_set_global_dir_path(tmp_path):
    with temp_global(set_global_dir_path, tmp_path, global_dir_path):
        with pytest.raises(FileNotFoundError):
            assert_equals_ref('value1', 'name1')


def test_set_global_env_var(tmp_path):
    with temp_env_var() as env_var:
        with temp_global(set_global_env_var, env_var, global_env_var):
            assert_equals_ref('new value', 'new_name', dir_path=tmp_path)


def test_set_global_assert_func():
    with temp_global(set_global_assert_func, custom_assert, global_assert_func):
        assert_equals_ref('VALUE1', 'name1')
        with pytest.raises(AssertionError):
            assert_equals_ref('NEW VALUE1', 'name1')


def test_set_global_cast_func():
    with temp_global(set_global_cast_func, lambda s: s.lower(), global_cast_func):
        assert_equals_ref('VALUE1', 'name1')
        with pytest.raises(AssertionError):
            assert_equals_ref('NEW VALUE1', 'name1')


def test_dir_path_and_set_global_dir_path(tmp_path):
    with temp_global(set_global_dir_path, tmp_path, global_dir_path):
        assert_equals_ref('value1', 'name1', dir_path=global_dir_path)


def test_env_var_and_set_global_env_var(tmp_path):
    with temp_env_var() as env_var:
        with temp_global(set_global_env_var, env_var + '_', global_env_var):
            assert_equals_ref('new value', 'new_name', dir_path=tmp_path, env_var=env_var)


def test_assert_func_and_set_global_assert_func():
    with temp_global(set_global_assert_func, None, global_assert_func):
        assert_equals_ref('VALUE1', 'name1', assert_func=custom_assert)
        with pytest.raises(AssertionError):
            assert_equals_ref('NEW VALUE1', 'name1', assert_func=custom_assert)


def test_cast_func_and_set_global_cast_func():
    with temp_global(set_global_cast_func, None, global_cast_func):
        assert_equals_ref('VALUE1', 'name1', cast_func=lambda s: s.lower())
        with pytest.raises(AssertionError):
            assert_equals_ref('NEW VALUE1', 'name1', cast_func=lambda s: s.lower())


def custom_assert(s1: str, s2: str) -> None:
    assert s1.lower() == s2.lower()


@contextmanager
def temp_env_var():
    env_var = 'PYTEST_UPDATE_REFS_' + uuid.uuid4().hex.upper()[:10]
    os.environ[env_var] = '1'
    yield env_var
    del os.environ[env_var]


@contextmanager
def temp_global(set_global, value, old_value):
    set_global(value)
    yield
    set_global(old_value)
