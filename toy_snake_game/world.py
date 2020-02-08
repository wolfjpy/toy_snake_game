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


"""This module provides World class definition.

World tracks all contents (e.g. Wall, Snake, Food) in the game.
"""


from dataclasses import dataclass, field
from food import Food
from snake import Snake
from wall import Wall


@dataclass
class World:
    """World class definition

    World is the container for game elements, including Wall, Snake,
    Food.

    Attributes:
        width_n:  Horizontal world size in number of units. (default: 60)
        height_n: Vertical world size in number of units. (default: 30)
        size:     Size of the basic unit. (default: 1)
        wall_:    Wall object, not initized with dataclass auto __init__.
                    No need to pass a Wall object when World auto init.
        snake_:   Snake object, not initized with dataclass auto __init__.
                    No need to pass a Snake object when World auto init.
        food_:    Food object, not initized with dataclass auto __init__.
                    No need to pass a Food object when World auto init.
    """

    width_n: int = 60
    height_n: int = 30
    size: int = 1
    wall_: Wall = field(init=False, repr=False)
    snake_: Snake = field(init=False, repr=False)
    food_: Food = field(init=False, repr=False)

    def __post_init__(self):
        """Populate wall_, snake_, food_ fields with a Wall object, 
        a Snake object, a Food object after auto __init__.
        """

        self.wall_ = Wall(self.width_n, self.height_n, self.size)
        self.snake_ = Snake(self.width_n, self.height_n, self.size)
        self.food_ = Food(self.width_n, self.height_n, self.size)
