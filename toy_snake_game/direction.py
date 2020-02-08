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


"""This module provides Direction class definition.

Direction generates offset-Figures.
"""

from dataclasses import dataclass
from figure import Figure


@dataclass
class Direction:
    """Direction class definition

    Direction generates an offset-Figure to be used when calculating the 
    next new Figure.

    Attributes:
        fg: base Figure to be used to generate an offset-Figure.
    """

    fg: Figure

    def up_offset(self) -> Figure:
        """Generate the offset for up direction.

        Returns:
            Figure: generated offset-Figure object
        """
        return Figure(0, -self.fg.size, self.fg.size, self.fg.color)

    def down_offset(self) -> Figure:
        """Generate the offset for down direction.

        Returns:
            Figure: generated offset-Figure object
        """
        return Figure(0, self.fg.size, self.fg.size, self.fg.color)

    def left_offset(self) -> Figure:
        """Generate the offset for left direction.

        Returns:
            Figure: generated offset-Figure object
        """
        return Figure(-self.fg.size, 0, self.fg.size, self.fg.color)

    def right_offset(self) -> Figure:
        """Generate the offset for right direction.

        Returns:
            Figure: generated offset-Figure object
        """
        return Figure(self.fg.size, 0, self.fg.size, self.fg.color)
