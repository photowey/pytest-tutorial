# -*- coding:utf-8 -*-


#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import pytest


def f():
    return 3


def test_function():
    assert f() == 4, "value was not equal to 4"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as ex:
        def f():
            f()

        f()
    assert "maximum recursion" in str(ex.value)


def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as ex:
        foo()

    assert ex.type is RuntimeError


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match_exception_message():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


def hello_func(x):
    if x <= 0:
        raise ValueError("x needs to be larger than zero")


def test_raises_legacy():
    pytest.raises(ValueError, hello_func, x=-1)


def xfail_func():
    raise IndexError()


@pytest.mark.xfail(raises=IndexError)
def test_xfail_func():
    xfail_func()
