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

from block import SnakeBlock
from snake import Snake


class TestSnake:

    def test_init(self):
        snake_ = Snake(10, 10, 1)
        assert snake_.body == [SnakeBlock(5, 5, 1)]
        assert snake_.stamp is None
        assert snake_.head == SnakeBlock(5, 5, 1)
        assert snake_.set_body == set([SnakeBlock(5, 5, 1)])

    def test_del_stamp(self):
        snake_ = Snake(10, 10, 1)
        snake_._del_stamp()
        assert snake_.body == []
        assert snake_.stamp == SnakeBlock(5, 5, 1)

    def test_move_update(self):
        snake_ = Snake(10, 10, 1)
        snake_._move_update(SnakeBlock(15, 14, 1))
        snake_._move_update(SnakeBlock(25, 24, 1))
        assert snake_.body == [SnakeBlock(25, 24, 1)]
        assert snake_.stamp == SnakeBlock(15, 14, 1)
        assert snake_.head == SnakeBlock(25, 24, 1)
        assert snake_.set_body == set([SnakeBlock(25, 24, 1)])

    def test_move_up(self):
        snake_ = Snake(10, 10, 1)
        snake_.move_up()
        assert snake_.body == [SnakeBlock(5, 4, 1)]
        assert snake_.stamp == SnakeBlock(5, 5, 1)
        assert snake_.head == SnakeBlock(5, 4, 1)
        assert snake_.set_body == set([SnakeBlock(5, 4, 1)])

    def test_move_down(self):
        snake_ = Snake(10, 10, 1)
        snake_.move_down()
        assert snake_.body == [SnakeBlock(5, 6, 1)]
        assert snake_.stamp == SnakeBlock(5, 5, 1)
        assert snake_.head == SnakeBlock(5, 6, 1)
        assert snake_.set_body == set([SnakeBlock(5, 6, 1)])

    def test_move_left(self):
        snake_ = Snake(10, 10, 1)
        snake_.move_left()
        assert snake_.body == [SnakeBlock(4, 5, 1)]
        assert snake_.stamp == SnakeBlock(5, 5, 1)
        assert snake_.head == SnakeBlock(4, 5, 1)
        assert snake_.set_body == set([SnakeBlock(4, 5, 1)])

    def test_move_right(self):
        snake_ = Snake(10, 10, 1)
        snake_.move_right()
        assert snake_.body == [SnakeBlock(6, 5, 1)]
        assert snake_.stamp == SnakeBlock(5, 5, 1)
        assert snake_.head == SnakeBlock(6, 5, 1)
        assert snake_.set_body == set([SnakeBlock(6, 5, 1)])

    def test_eat(self):
        snake_ = Snake(10, 10, 1)
        snake_.move_up()
        snake_.eat()
        assert snake_.body == [SnakeBlock(5, 4, 1), SnakeBlock(5, 5, 1)]
        assert snake_.stamp == SnakeBlock(5, 5, 1)
        assert snake_.head == SnakeBlock(5, 4, 1)
        assert snake_.set_body == set(
            [SnakeBlock(5, 4, 1), SnakeBlock(5, 5, 1)])

        snake_.move_left()
        assert snake_.body == [SnakeBlock(4, 4, 1), SnakeBlock(5, 4, 1)]
        assert snake_.stamp == SnakeBlock(5, 5, 1)
        assert snake_.head == SnakeBlock(4, 4, 1)
        assert snake_.set_body == set(
            [SnakeBlock(4, 4, 1), SnakeBlock(5, 4, 1)])

        snake_.move_down()
        assert snake_.body == [SnakeBlock(4, 5, 1), SnakeBlock(4, 4, 1)]
        assert snake_.stamp == SnakeBlock(5, 4, 1)
        assert snake_.head == SnakeBlock(4, 5, 1)
        assert snake_.set_body == set(
            [SnakeBlock(4, 5, 1), SnakeBlock(4, 4, 1)])
