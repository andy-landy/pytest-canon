import os
from pathlib import Path
from typing import Union, Callable, Optional


__version__ = '1.0.0'


class Config:
    def __init__(
        self,
        dir_path: Union[str, Path] = '',
        env_var: str = '',
        assert_func: Optional[Callable[[str, str], None]] = None,
        cast_func: Optional[Callable[[str], str]] = None,
    ):
        self.dir_path: Path = dir_path if isinstance(dir_path, Path) else Path(dir_path)
        self.env_var = env_var
        self.assert_func = assert_func
        self.cast_func = cast_func
        
    def merge(self, other: Optional['Config']) -> 'Config':
        return Config(
            dir_path=other.dir_path or self.dir_path,
            env_var=other.env_var or self.env_var,
            assert_func=other.assert_func or self.assert_func,
            cast_func=other.cast_func or self.cast_func,
        ) if other else self


global_config = Config(
    dir_path=Path('tests/dumps'),
    env_var='PYTEST_UPDATE_REFS',
)


def set_global_config(config):
    global global_config
    global_config = config.merge(global_config)


def assert_equals_ref(value: str, name: str, config: Optional[Config] = None) -> None:
    config_: Config = global_config.merge(config)

    path = config_.dir_path / '{}.txt'.format(name)

    if os.getenv(config_.env_var, ''):
        path.write_text(value)
        return

    expected = path.read_text()

    if config_.cast_func:
        value = config_.cast_func(value)
        expected = config_.cast_func(expected)

    if config_.assert_func:
        config_.assert_func(value, expected)
    else:
        assert value == expected
