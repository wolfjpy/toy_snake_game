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


"""This module provides Builder class definition.

Builder creates next new Figure based on direction and current Figure.
"""

from typing import Any

from dataclasses import dataclass
from direction import Direction
from figure import Figure


@dataclass
class Builder:
    """Builder class definition.

    Builder creates next new Figure based on direction and current Figure.

    Attributes:
        base: Figure object
    """

    base: Figure

    def next_fig(self, direct: str) -> Any:
        """Dynamically generate next Figure.

        Arguments:
            direct (str): direction ('UP', 'DOWN', 'LEFT', 'RIGHT')

        Returns:
            Any: Figure or a subclass of Figure object
        """

        if direct == 'UP':
            offset = Direction(self.base).up_offset()  # up offset-Figure
        elif direct == 'DOWN':
            offset = Direction(self.base).down_offset()  # down offset-Figure
        elif direct == 'LEFT':
            offset = Direction(self.base).left_offset()  # left offset-Figure
        elif direct == 'RIGHT':
            offset = Direction(self.base).right_offset()  # right offset-Figure
        else:
            # TODO more elegant handler
            print(f'warning: received invalid {direct}')
        next_one = self.base + offset  # calculate next Figure
        # dynamically geneate next Figure or subclass of Figure object
        return type(self.base)(next_one.x, next_one.y, next_one.size, next_one.color)
