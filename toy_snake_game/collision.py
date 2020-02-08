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


"""This module provides Collision class definition.

Collision detects collision among world elements.
"""

from typing import Tuple

from dataclasses import dataclass
from world import World


@dataclass
class Collision:
    """Collision class definition

    Collision detects collision among world elements.

    Attributes:
        wd: World object
    """

    wd: World

    def check_snake_head(self) -> Tuple[bool]:
        """Check if Snake's head collide Snake tails, Food, Wall.

        Returns:
            Tuple[bool]: True if collide. Otherwise, False.
        """

        head = self.wd.snake_.head
        snake_ = self.wd.snake_
        food_ = self.wd.food_
        wall_ = self.wd.wall_
        return head in snake_, head in food_, head in wall_

    def check_new_food(self) -> Tuple[bool]:
        """Check if Food collide Snake tails and Wall.

        Returns:
            Tuple[bool]: True if collide. Otherwise, False.
        """

        new_food = list(self.wd.food_.body)[0]
        return new_food in self.wd.snake_, new_food in self.wd.wall_
