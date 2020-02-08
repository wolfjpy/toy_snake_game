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


"""This module provides Logic class definition.

Logic defines the logic of updating world state.
"""

from collision import Collision
from dataclasses import dataclass
from world import World


@dataclass
class Logic:
    """Logic class definition

    Logic defines the logic of updating World state.

    Attributes:
        wd: World object
    """

    wd: World

    def update(self, key='LEFT') -> str:
        """Update World next state (Snake, Food) 
        according current state and keystrokes.

        Keyword Arguments:
            key (str): keystroke signal (default: 'LEFT')

        Returns:
            str: World state signal ('QUIT', 'DONE', 'CONT')
        """

        if key == 'LEFT':
            self.wd.snake_.move_left()
        elif key == 'RIGHT':
            self.wd.snake_.move_right()
        elif key == 'UP':
            self.wd.snake_.move_up()
        elif key == 'DOWN':
            self.wd.snake_.move_down()
        elif key == 'EXIT':  # quit game
            return 'QUIT'
        else:
            pass

        coll = Collision(self.wd)  # init Collision object
        head_collide = coll.check_snake_head()  # check snake head collision

        if head_collide[0]:  # eat tails
            return 'DONE'
        if head_collide[1]:  # eat food
            self.wd.snake_.eat()  # update snake state after eating
            self.wd.food_.spawn_new()  # spawn a new food
            while any(coll.check_new_food()):  # spawn new food w/t collision
                self.wd.food_.spawn_new()
        if head_collide[2]:  # hit wall
            return 'DONE'

        return 'CONT'  # continue game
