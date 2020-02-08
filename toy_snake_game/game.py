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


"""This module provides Game class definition and entry point.
"""


from time import sleep

from asciimatics.screen import Screen

from logic import Logic
from painter import Painter
from world import World


class Game:
    """Wire models, view, and controller together.

    Main class and entry point for game.
    """

    def __init__(self):
        """Contructor method

        Attributes:
            _ev_key (dict): event-signal map. Modify if wants 
                                to change control keystrokes.
        """

        # valid key strokes
        self._ev_key = {ord('Q'): 'EXIT', ord('q'): 'EXIT',
                        ord('I'): 'UP', ord('i'): 'UP',
                        ord('K'): 'DOWN', ord('k'): 'DOWN',
                        ord('J'): 'LEFT', ord('j'): 'LEFT',
                        ord('L'): 'RIGHT', ord('l'): 'RIGHT'}

    def run(self, screen):
        """Main event loop, need to bind to rendering engine.

        Arguments:
            screen: screen instance for rendering engine.
        """

        wd = World()  # init a World, default: (width_n=60, height_n=30, size=1)
        brush = Painter(wd, screen)  # init a Painter
        lg = Logic(wd)  # init a Logic
        prev_ev = ord('j')  # init move
        while True:  # game main event loop
            screen.clear()  # clear screen before drawing
            brush.draw()  # draw all current game elements
            ev = screen.get_key()  # listen a keystroke

            if ev is None:  # no key pressed
                # update world state by previous keystroke
                status = lg.update(self._ev_key[prev_ev])
            else:  # key pressed
                if ev in self._ev_key:  # valid key
                    # update world state by current keystroke
                    status = lg.update(self._ev_key[ev])
                    prev_ev = ev  # update previous keystroke by current one
                else:  # invalid key
                    # update world state by previous keystroke
                    status = lg.update(self._ev_key[prev_ev])

            screen.refresh()  # render screen

            if status == 'QUIT':  # user quit
                return
            if status == 'DONE':  # game over
                brush.gameover()  # draw gameover banner
                screen.refresh()  # render screen
                sleep(5)  # sleep 5 seconds before quit
                return


# game main entry point
if __name__ == '__main__':
    Screen.wrapper(Game().run)  # bind event loop to screen rendering
