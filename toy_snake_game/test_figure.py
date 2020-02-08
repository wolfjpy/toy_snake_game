#    Copyright 2018 JPY
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from figure import Figure


class TestFigure:

    def test_init(self):
        fg = Figure(0, 10, 2, 'red')
        assert fg == Figure(0, 10, 2, 'red')

    def test_add(self):
        fg1 = Figure(0, 10, 2, 'red')
        fg2 = Figure(2, 5, 3, 'blue')
        assert fg1 + fg2 == Figure(2, 15, 2, 'red')
