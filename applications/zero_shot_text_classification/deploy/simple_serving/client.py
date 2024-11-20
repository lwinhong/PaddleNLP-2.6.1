# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
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

import json
from pprint import pprint

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:8190/taskflow/utc"

    headers = {"Content-Type": "application/json"}

    texts = ["中性粒细胞比率偏低", "男性小腹疼痛是什么原因？"]

    data = {"data": {"text": texts}}
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    datas = json.loads(r.text)
    pprint(datas)
