![Example](https://raw.githubusercontent.com/andy-landy/pytest-canon/master/header.png)

<h2 align="center">???????? Python ???? Testing ????? Canonization ??????</h2>
<p align="center">???? It is good, use it and enjoy ????</p>

<p align="center">
<a href="https://github.com/andy-landy/pytest-canon/actions"><img alt="Actions Status" src="https://github.com/andy-landy/pytest-canon/workflows/Tests/badge.svg"></a>
<a href="https://codecov.io/gh/andy-landy/pytest-canon"><img alt="Codecov" src="https://codecov.io/gh/andy-landy/pytest-canon/branch/master/graph/badge.svg"></a>
<a href="https://github.com/andy-landy/pytest-canon/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/andy-landy/pytest-canon?color=informational"></a>
<a href="https://pypi.org/project/pytest-canon/"><img alt="PyPI" src="https://img.shields.io/pypi/v/pytest-canon"></a>
<a href="https://pypi.org/project/pytest-canon/"><img alt="PyPI" src="https://img.shields.io/badge/python-3.5+-blue.svg"></a>
<img title="type hints everywhere" alt="Annotations coverage" src="https://img.shields.io/badge/type--hints-100%25-blueviolet.svg">
<img title="no obscure objects, only transparent functions and dataclass objects" alt="No-OOP coverage" src="https://img.shields.io/badge/no OOP-100%25-blueviolet.svg">
<a href="https://github.com/andy-landy/pytest_canon/blob/master/setup.py"><img alt="Dependencies" src="https://img.shields.io/badge/dependencies-0-blueviolet.svg"></a>
<a href="https://gitter.im/andy-landy/pytest-canon"><img alt="Gitter" src="https://img.shields.io/gitter/room/andy-landy/pytest-canon?color=blueviolet"></a>
<!--
<a href="https://lgtm.com/projects/g/andy-landy/pytest_canon/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/andy-landy/pytest_canon.svg?logo=lgtm&logoWidth=18"/></a>
<a href="https://pepy.tech/project/pytest_canon"><img alt="Downloads" src="https://pepy.tech/badge/pytest_canon"></a>
<a href="https://anaconda.org/conda-forge/pytest_canon/"><img alt="conda-forge" src="https://img.shields.io/conda/dn/conda-forge/pytest_canon.svg?label=conda-forge"></a>
-->
</p>
<br/>

> “???? I really needed it ???? ” 
> <em>– Somebody except me I hope</em>

???? Tired of useless job? Fix it ????

---

_Contents:_ **[Installation](#installation)** | **[Quick Start](#quick-start)**
| **[How does it save my time?](#how-does-it-save-my-time)** | 
**[Examples and recipes](#examples-and-recipes)** | **[Reference](#reference)**

---

### Installation

```
pip install pytest-canon
```

### Quick Start

<a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/simplest_usage.py">Simplest usage</a>, a single line:
```python
    def test_case_1:
        assert_equals_ref(tested_func(...), 'test_case_1')
```

<a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/scenario.sh">Run tests</a>:
```bash
    pytest  # that's it :)
```

<a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/scenario.sh">Update tests</a>:
```bash
    PYTEST_UPDATE_REFS=1 pytest
```

Set <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_global_test.py">different dump location</a>:
```python
    set_global_config(Config(dir_path='other_dir'))
```

Set <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_global_test.py">different string comparison</a>:
```python
    set_global_config(Config(cast_func=lambda s: s.lower()))
```

Customize <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_global_test.py">a single test</a>:
```python
    def test_case_1():
        assert_equal_ref(tested_func(...), 'test_case_1', Config(cast_func = lambda s: s.lower()))
```

### How does it save my time?

* Reason 1

    ??????

* Reason 2

    ?????

* Reason 3

    ??????
     

### Examples and recipes

* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/simplest_usage.py">simplest usage</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/scenario.sh">typical real life scenario</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_single_test.py">customize a simple usage</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_globally.py">customize globally</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_single_test_and_globally.py">customize a simple usage and globally</a>


### Reference


#### <a href="https://github.com/andy-landy/pytest-canon/tree/master/pytest-canon/__init__.py">`assert_equals_ref(value: str, name: str, [config: Config])`</a>
Reads and compares a string value from a corresponding dump file, or writes it

---

#### <a href="https://github.com/andy-landy/pytest-canon/tree/master/pytest-canon/__init__.py">`set_global_config(config: Config)`</a>
Sets global config. It's values are overrided by values of a config passed to `assert_equal_refs`.

---

#### <a href="https://github.com/andy-landy/pytest-canon/tree/master/pytest-canon/__init__.py">`Config`</a>

    `dir_path`: `str` or `Path`, dir with dumps, default=`'tests/dumps'`
    `env_var`: `str` ,env variable activating tests updates, default=`'PYTEST_UPDATE_REFS'`
    `assert_func`: assert function (string1, string2) -> NoReturn
    `cast_func`: casting function string -> string
