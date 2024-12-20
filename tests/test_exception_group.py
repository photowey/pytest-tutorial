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


def f1():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError(),
        ],
    )


def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as ex:
        f1()
        assert ex.group_contains(RuntimeError)
        assert not ex.group_contains(TypeError)


def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as ex:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )

        assert ex.group_contains(RuntimeError, depth=1)
        assert ex.group_contains(TypeError, depth=2)
        assert not ex.group_contains(RuntimeError, depth=2)
        assert not ex.group_contains(TypeError, depth=1)


def test_exception_in_group_match():
    with pytest.raises(ExceptionGroup) as ex:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError("Exception 123 raised"),
            ],
        )
    assert ex.group_contains(RuntimeError, match=r".* 123 .*")
    assert not ex.group_contains(TypeError)
