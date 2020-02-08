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


class TestBlock:

    def test_init(self):
        bl = Block(0, 2, 3, 'red')
        assert bl == Block(0, 2, 3, 'red')


class TestSnakeBlock:

    def test_init(self):
        obj = SnakeBlock(0, 2, 3)
        assert (obj.x, obj.y, obj.size, obj.color) == (0, 2, 3, 'red')


class TestFoodBlock:

    def test_init(self):
        obj = FoodBlock(0, 2, 3)
        assert (obj.x, obj.y, obj.size, obj.color) == (0, 2, 3, 'blue')


class TestWallBlock:

    def test_init(self):
        obj = WallBlock(0, 2, 3)
        assert (obj.x, obj.y, obj.size, obj.color) == (0, 2, 3, 'white')
