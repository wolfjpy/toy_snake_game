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


"""This module provides Figure class definition.

Figure defines basic game entity.
"""

from dataclasses import dataclass


@dataclass
class Figure:
    """Figure class definition

    Figure defines basic game entity.

    Attributes:
        x:     Horizontal coordinate in number of units.
        y:     Vertical coordinate in number of units.
        size:  Size of the basic unit.
        color: entity color.
    """

    x: int
    y: int
    size: int
    color: str

    def __add__(self, other):
        """Magic method of "+"

        Add a Figure object on another Figure object by coordinate (x, y)

        Arguments:
            other (Figure): a Figure object

        Returns:
            Figure: a new Figure after coordinate addition
        """

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Figure(new_x, new_y, self.size, self.color)
