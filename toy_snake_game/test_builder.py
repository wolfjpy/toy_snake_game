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

from block import Block, FoodBlock, SnakeBlock, WallBlock
from builder import Builder
from figure import Figure


class TestBuilder:

    def test_next_(self):
        base = Figure(3, 4, 1, 'red')
        assert Builder(base).next_fig('UP') == Figure(3, 3, 1, 'red')
        assert Builder(base).next_fig('DOWN') == Figure(3, 5, 1, 'red')
        assert Builder(base).next_fig('LEFT') == Figure(2, 4, 1, 'red')
        assert Builder(base).next_fig('RIGHT') == Figure(4, 4, 1, 'red')

    def test_next_block(self):
        base = Block(3, 4, 1, 'red')
        assert Builder(base).next_fig('UP') == Block(3, 3, 1, 'red')
        base = SnakeBlock(3, 4, 1, 'red')
        assert Builder(base).next_fig('UP') == SnakeBlock(3, 3, 1, 'red')
        base = FoodBlock(3, 4, 1, 'red')
        assert Builder(base).next_fig('UP') == FoodBlock(3, 3, 1, 'red')
        base = WallBlock(3, 4, 1, 'red')
        assert Builder(base).next_fig('UP') == WallBlock(3, 3, 1, 'red')
