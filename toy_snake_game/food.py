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


"""This module provides Food class definition.

Food defines food entity.
"""


from random import randint
from typing import Set

from block import Block, FoodBlock
from dataclasses import dataclass, field


@dataclass
class Food:
    """Food class definition

    Food defines food entity Snake can eat.

    Attributes:
        width_n:  Horizontal world size in number of units.
        height_n: Vertical world size in number of units.
        size:     Size of the basic unit.
        body:     set of FoodBlock objects.
    """

    width_n: int
    height_n: int
    size: int
    body: Set[FoodBlock] = field(default_factory=set)

    def __post_init__(self):
        """Populate the Food body with default initialization if not given.
        """

        if not self.body:  # if not explicitly given
            self.body = set([FoodBlock(int(self.width_n/4)*self.size,
                                       int(self.height_n/4)*self.size, self.size)])

    def spawn_new(self):
        """Randomly set a new coordinate (x, y) of Food.
        """

        self.body = set([FoodBlock(randint(0, self.width_n),
                                   randint(0, self.height_n), self.size)])

    def __contains__(self, key: Block):
        """Magic method of "in"

        Check if a Block in the Food body by coordinate (x, y) 

        Arguments:
            key (Block): a Block object

        Returns:
            bool: True if key's coordinate in Food body, otherwise, False
        """

        return any(key.x == b.x and key.y == b.y for b in self.body)
