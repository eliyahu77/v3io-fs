# Copyright 2020 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from datetime import datetime
import pandas as pd
from conftest import test_container, test_dir

csv_data = b'''
name,item,price,quantity
Rick,Vodka,13.2,22
Jerry,Beer,34.2,300
Beth,Lettuce,1.2,13
Summer,M&M,2.2,7
Morty,Twix,1.7,5
'''


def test_pandas(client, new_file):
    file_name = datetime.now().strftime('test-%Y%m%d%H%M.csv')
    file_path = f'/{test_dir}/{file_name}'
    new_file(client, file_path, csv_data)

    df = pd.read_csv(f'v3io://{test_container}{file_path}')
    assert 4 == len(df.columns), '# of columns'
    assert 5 == len(df), '# of rows'
