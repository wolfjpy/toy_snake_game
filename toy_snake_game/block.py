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


"""This module provides Block class and Block subclasses definitions.

Block class and Block subclasses define the basic elements to build Snake, Food, Wall.
"""

from dataclasses import dataclass
from figure import Figure


@dataclass(unsafe_hash=True)
class Block(Figure):
    """Block, a subclass of Figure, definition."""

    pass


@dataclass(unsafe_hash=True)
class SnakeBlock(Block):
    """SnakeBlock, a subclass of Block, definition."""

    color: str = 'red'


@dataclass(unsafe_hash=True)
class FoodBlock(Block):
    """FoodBlock, a subclass of Block, definition."""

    color: str = 'blue'


@dataclass(unsafe_hash=True)
class WallBlock(Block):
    """WallBlock, a subclass of Block, definition."""

    color: str = 'white'
