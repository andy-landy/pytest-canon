![Example](https://raw.githubusercontent.com/andy-landy/pytest-canon/master/header.png)

<h2 align="center">???????? Python ???? Testing ????? Canonization ??????</h2>
<p align="center">???? It is good, use it and enjoy ????</p>

<p align="center">
<a href="https://github.com/andy-landy/pytest-canon/actions"><img alt="Actions Status" src="https://github.com/andy-landy/pytest-canon/workflows/Tests/badge.svg"></a>
<a href="https://codecov.io/gh/andy-landy/pytest-canon"><img alt="Codecov" src="https://codecov.io/gh/andy-landy/pytest-canon/branch/master/graph/badge.svg"></a>
<a href="https://lgtm.com/projects/g/andy-landy/pytest-canon/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/andy-landy/pytest-canon.svg"/></a>
<a href="https://github.com/andy-landy/pytest-canon/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/andy-landy/pytest-canon?color=informational"></a>
<a href="https://pypi.org/project/pytest-canon/"><img alt="PyPI" src="https://img.shields.io/pypi/v/pytest-canon"></a>
<a href="https://pypi.org/project/pytest-canon/"><img alt="PyPI" src="https://img.shields.io/badge/python-3.5+-blue.svg"></a>
<img title="type hints everywhere" alt="Annotations coverage" src="https://img.shields.io/badge/type--hints-100%25-blueviolet.svg">
<img title="no obscure objects, only transparent functions and dataclass objects" alt="No-OOP coverage" src="https://img.shields.io/badge/no OOP-100%25-blueviolet.svg">
<a href="https://github.com/andy-landy/pytest-canon/blob/master/setup.py"><img alt="Dependencies" src="https://img.shields.io/badge/dependencies-0-blueviolet.svg"></a>
<a href="https://gitter.im/andy-landy/pytest-canon"><img alt="Gitter" src="https://img.shields.io/gitter/room/andy-landy/pytest-canon?color=blueviolet"></a>
<!--
<a href="https://pepy.tech/project/pytest-canon"><img alt="Downloads" src="https://pepy.tech/badge/pytest-canon"></a>
<a href="https://anaconda.org/conda-forge/pytest-canon/"><img alt="conda-forge" src="https://img.shields.io/conda/dn/conda-forge/pytest-canon.svg?label=conda-forge"></a>
-->
</p>
<br/>

> “Doesn't pytest have it out of the box?” 
> <em>– Boris Kovarsky</em>

Surprisingly enough, it does **not**.

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
        ...
        assert_equals_ref(very_long_multiline_string, 'test_case_1')
```

<a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/scenario_for_pytest.sh">Run tests (e.g. with `pytest`)</a>:
```bash
    pytest  # that's it :)
```

<a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/scenario.sh">Update tests (e.g. with `pytest`)</a>:
```bash
    PYTEST_UPDATE_REFS=1 pytest
```

Set <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_global_test.py">different dump location</a>:
```python
    set_global_dir_path('other_dir')
```

Set <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_global_test.py">different string comparison</a>:
```python
    set_global_cast_func(lambda s: s.lower())
```

Customize <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_global_test.py">a single test</a>:
```python
    def test_case_1():
        assert_equal_ref(long_string, 'test_case_1', cast_func=lambda s: s.lower())
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
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/scenario_for_pytest.sh">typical real life scenario</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_single_test.py">customize a simple usage</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_globally.py">customize globally</a>
* <a href="https://github.com/andy-landy/pytest-canon/tree/master/examples/customize_single_test_and_globally.py">customize a simple usage and globally</a>


### Reference

#### <a href="https://github.com/andy-landy/pytest-canon/tree/master/pytest_canon/__init__.py">`assert_equals_ref(value: str, name: str, ...)`</a>
Either compares a string value with a dumped one or dumps it depending on `env_var` value. 

Optional arguments: <br/>
`dir_path`: `str` or `Path`, dir with dumps, default=`'tests/dumps'` <br/>
`env_var`: `str` ,env variable activating tests updates, default=`'PYTEST_UPDATE_REFS'` <br/>
`assert_func`: assert function `(str, str) -> NoReturn` <br/>
`cast_func`: casting function `str -> str` <br/>

---

#### <a href="https://github.com/andy-landy/pytest-canon/tree/master/pytest_canon/__init__.py">`set_global_*`</a>
Global setters for every optional argument of <a href="https://github.com/andy-landy/pytest-canon/tree/master/pytest_canon/__init__.py">`assert_equals_ref`</a>