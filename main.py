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


import os

import pytest


def clean_tmp_dir(target_path):
    """
    clean tmp dir
    """

    if os.path.exists(target_path):
        sub_files = os.listdir(target_path)
        for i in sub_files:
            sub_file = os.path.join(target_path, i)
            if os.path.isdir(sub_file):
                clean_tmp_dir(sub_file)
            else:
                print('remove the file:{}'.format(sub_file))
                os.remove(sub_file)


if __name__ == '__main__':
    # warning::it's dangerous
    clean_tmp_dir('./tmp')

    pytest.main()
    os.system('allure generate ./tmp -o ./report --clean')
