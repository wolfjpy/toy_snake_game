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

from direction import Direction
from figure import Figure


class TestDirection:

    def test_up_offset(self):
        fg = Figure(2, 3, 5, 'red')
        obj = Direction(fg).up_offset()
        assert obj == Figure(0, -5, 5, 'red')

    def test_down_offset(self):
        fg = Figure(2, 3, 5, 'red')
        obj = Direction(fg).down_offset()
        assert obj == Figure(0, 5, 5, 'red')

    def test_left_offset(self):
        fg = Figure(2, 3, 5, 'red')
        obj = Direction(fg).left_offset()
        assert obj == Figure(-5, 0, 5, 'red')

    def test_right_offset(self):
        fg = Figure(2, 3, 5, 'red')
        obj = Direction(fg).right_offset()
        assert obj == Figure(5, 0, 5, 'red')
