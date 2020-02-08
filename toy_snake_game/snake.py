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


"""This module provides Snake class definition.

Snake defines snake entity.
"""

from typing import List, Set

from block import Block, SnakeBlock
from builder import Builder
from dataclasses import dataclass, field


@dataclass
class Snake:
    """Snake class definition

    Snake defines snake entity.

    Attributes:
        width_n:  Horizontal world size in number of units.
        height_n: Vertical world size in number of units.
        size:     Size of the basic unit.
        body:     list of SnakeBlock objects.
        stamp:    the latest footprint of snake.
    """

    width_n: int
    height_n: int
    size: int
    body: List[SnakeBlock] = field(default_factory=list)
    stamp: SnakeBlock = None

    def __post_init__(self):
        """Populate the Snake body with default initialization if not given.
        """

        if not self.body:  # if not explicitly given
            self.body = [SnakeBlock(
                int(self.width_n/2)*self.size, int(self.height_n/2)*self.size, self.size)]

    @property
    def head(self) -> SnakeBlock:
        """Snake's head getter method

        Returns:
            SnakeBlock: the head
        """

        return self.body[0]

    @property
    def set_body(self) -> Set[SnakeBlock]:
        """Snake's set of body getter method

        Returns:
            Set[SnakeBlock]: set of Snake body
        """

        return set(self.body)

    def _del_stamp(self):
        """Delete last tail and update as stamp."""

        self.stamp = self.body.pop(-1)

    def _move_update(self, new_block: SnakeBlock):
        """Update snake body after move.

        Arguments:
            new_block (SnakeBlock): new head after move
        """

        self.body.insert(0, new_block)  # prepend new block before head
        self._del_stamp()  # remove stamp

    def move_up(self):
        """Snake moves up."""

        new_block = Builder(self.head).next_fig(
            'UP')  # generate new head after move up
        self._move_update(new_block)  # generate new head after move up

    def move_down(self):
        """Snake moves down."""

        # generate new head after move down
        new_block = Builder(self.head).next_fig('DOWN')
        self._move_update(new_block)  # generate new head after move down

    def move_left(self):
        """Snake moves left."""

        # generate new head after move left
        new_block = Builder(self.head).next_fig('LEFT')
        self._move_update(new_block)  # generate new head after move left

    def move_right(self):
        """Snake moves right."""

        # generate new head after move right
        new_block = Builder(self.head).next_fig('RIGHT')
        self._move_update(new_block)  # generate new head after move right

    def eat(self):
        """Snake eats food, increase body length by adding stamp back."""

        self.body.append(self.stamp)  # add stamp back after eating

    def __contains__(self, key: Block) -> bool:
        """Magic method of "in"

        Check if a Block in the Snake body by coordinate (x, y) 

        Arguments:
            key (Block): a Block object

        Returns:
            bool: True if key's coordinate in Snake body, otherwise, False
        """

        # check tails only
        return any(key.x == b.x and key.y == b.y for b in self.body[1:])
