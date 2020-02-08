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


"""This module provides Painter class definition.

Painter draws elements on the screen.
"""


from typing import Any

from dataclasses import dataclass
from drawable import Drawable
from world import World


@dataclass
class Painter(Drawable):
    """Painter class definition

    Painter implements Drawable inferface and draws elements on the screen.

    Attributes:
        wd:  a World object
        scr: a Screen object
    """

    wd: World
    scr: Any

    def draw(self, snake_=True, food_=True, wall_=True):
        """draw snake, food, and wall.

        Arguments:
            snake_ (bool): turn on/off drawing snake (default: True)
            food_ (bool):  turn on/off drawing food (default: True)
            wall_ (bool):  turn on/off drawing wall (default: True)
        """

        if snake_:  # draw snake
            [self.scr.print_at('#', skbl.x, skbl.y, colour=self.scr.COLOUR_RED)
             for skbl in self.wd.snake_.body]
        if food_:  # draw food
            [self.scr.print_at('*', fdbl.x, fdbl.y, colour=self.scr.COLOUR_BLUE)
             for fdbl in self.wd.food_.body]
        if wall_:  # draw wall
            [self.scr.print_at('@', wlbl.x, wlbl.y, colour=self.scr.COLOUR_WHITE)
             for wlbl in self.wd.wall_.body]

        # draw authorship banne
        self.scr.print_at(f"Jerry Design by \u2764", int(2*self.wd.width_n/3)*self.wd.size,
                          (self.wd.height_n+1)*self.wd.size, colour=self.scr.COLOUR_YELLOW)

        # draw instruction
        self.scr.print_at(f"I: Up, K: Down, J: Left, L: Right", 0,
                          (self.wd.height_n+1)*self.wd.size, colour=self.scr.COLOUR_CYAN)

    def gameover(self):
        """draw GAMEOVER banner."""

        self.scr.print_at('GAME OVER', int(self.wd.width_n/2)*self.wd.size,
                          int(self.wd.height_n/2)*self.wd.size, colour=self.scr.COLOUR_YELLOW)
