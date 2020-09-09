#
# Copyright 2013 Quantopian, Inc.
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
from trading_calendars import get_calendar
import pandas as pd


def get_benchmark_returns(symbol):
    """
    Return a data series from 1930 to 2030 with all zero values,
    which will effectively sidestep this web call issue,
    with no negative impact.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.
    """
    cal = get_calendar('NYSE')
    first_date = datetime(1930, 1, 1)
    last_date = datetime(2030, 1, 1)
    dates = cal.sessions_in_range(first_date, last_date)
    data = pd.DataFrame(0.0, index=dates, columns=['close'])
    data = data['close']
    return data.sort_index().iloc[1:]
