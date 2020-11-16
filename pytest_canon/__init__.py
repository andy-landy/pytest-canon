import os
from pathlib import Path
from typing import Union, Callable, Optional


__version__ = '1.0.0'


global_dir_path: Path = Path('tests/dumps')
global_env_var: str = 'PYTEST_UPDATE_REFS'
global_assert_func: Optional[Callable[[str, str], None]] = None
global_cast_func: Optional[Callable[[str], str]] = None


def set_global_dir_path(dir_path: Union[Path, str]) -> None:
    global global_dir_path
    global_dir_path = Path(dir_path)


def set_global_env_var(env_var: str) -> None:
    global global_env_var
    global_env_var = env_var


def set_global_assert_func(assert_func: Optional[Callable[[str, str], None]]) -> None:
    global global_assert_func
    global_assert_func = assert_func


def set_global_cast_func(cast_func: Optional[Callable[[str], str]]) -> None:
    global global_cast_func
    global_cast_func = cast_func


def assert_equals_ref(
    value: str,
    name: str,
    dir_path: Optional[Union[Path, str]] = None,
    env_var: str = '',
    assert_func: Optional[Callable[[str, str], None]] = None,
    cast_func: Optional[Callable[[str], str]] = None,
) -> None:
    dir_path_: Path = (Path(dir_path) if dir_path else None) or global_dir_path
    env_var_ = env_var or global_env_var
    assert_func_ = assert_func or global_assert_func
    cast_func_ = cast_func or global_cast_func

    path = dir_path_ / '{}.txt'.format(name)

    if os.getenv(env_var_, ''):
        path.write_text(value)
        return

    expected = path.read_text()

    if cast_func_:
        value = cast_func_(value)
        expected = cast_func_(expected)

    if assert_func_:
        assert_func_(value, expected)
    else:
        assert value == expected
