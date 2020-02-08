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


"""This module provides Wall class definition.

Wall defines game boundary.
"""

from typing import Set

from block import Block, WallBlock
from dataclasses import dataclass, field


@dataclass
class Wall:
    """Wall class definition

    Wall defines a game boundary where snake can move.

    Attributes:
        width_n:  Horizontal world size in number of units.
        height_n: Vertical world size in number of units.
        size:     Size of the basic unit.
        body:     set of WallBlock objects.
    """

    width_n: int
    height_n: int
    size: int
    body: Set[WallBlock] = field(default_factory=set)

    def __post_init__(self):
        """Populate the wall body with default initialization if not given.
        """

        if not self.body:  # if not explicitly given
            # a set of wall blocks on the top
            top = set(WallBlock(i*self.size, 0, self.size)
                      for i in range(self.width_n))
            # a set of wall blocks on the left
            left = set(WallBlock(0, i*self.size, self.size)
                       for i in range(self.height_n))
            # a set of wall blocks at the bottom
            bottom = set(WallBlock(i*self.size, self.height_n, self.size)
                         for i in range(self.width_n))
            # a set of wall blocks on the right
            right = set(WallBlock(self.width_n, i*self.size, self.size)
                        for i in range(self.height_n))
            self.body = top | left | bottom | right

    def __contains__(self, key: Block) -> bool:
        """Magic method of "in"

        Check if a Block in the Wall body by coordinate (x, y) 

        Arguments:
            key (Block): a Block object

        Returns:
            bool: True if key's coordinate in Wall body, otherwise, False
        """

        return any(key.x == b.x and key.y == b.y for b in self.body)
