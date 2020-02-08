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


"""This module provides Drawable Interface definition.
"""

import abc


class Drawable(metaclass=abc.ABCMeta):
    """Drawable Interface definition."""

    @abc.abstractmethod
    def draw(self, *args):
        """draw abstract method

        Need to be implemented by subclass.
        """

        pass
