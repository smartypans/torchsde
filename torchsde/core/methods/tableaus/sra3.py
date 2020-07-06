# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# From "RUNGE-KUTTA METHODS FOR THE STRONG APPROXIMATION OF SOLUTIONS OF STOCHASTIC DIFFERENTIAL EQUATIONS".
# For additive noise structure.
# (ODE order, SDE strong order) = (3.0, 1.5).

STAGES = 3

C0 = (0, 1, 1 / 2)
C1 = (1, 0, 0)

A0 = (
    (),
    (1,),
    (1 / 4, 1 / 4),
)

B0 = (
    (),
    (0,),
    (1, 1 / 2),
)

alpha = (1 / 6, 1 / 6, 2 / 3)
beta1 = (1, 0, 0)
beta2 = (1, -1, 0)
