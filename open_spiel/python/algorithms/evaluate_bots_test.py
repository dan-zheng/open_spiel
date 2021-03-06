# Copyright 2019 DeepMind Technologies Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for google3.third_party.open_spiel.python.algorithms.evaluate_bots."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

import numpy as np

from open_spiel.python.algorithms import evaluate_bots
from open_spiel.python.bots import uniform_random
import pyspiel


class EvaluateBotsTest(absltest.TestCase):

  def test_cpp_vs_python(self):
    game = pyspiel.load_game("kuhn_poker")
    bots = [
        pyspiel.make_uniform_random_bot(game, 0, 1234),
        uniform_random.UniformRandomBot(game, 1, np.random.RandomState(4321))
    ]
    results = np.array([
        evaluate_bots.evaluate_bots(game.new_initial_state(), bots, np.random)
        for _ in range(10000)
    ])
    average_results = np.mean(results, axis=0)
    np.testing.assert_allclose(average_results, [0.125, -0.125], atol=0.1)


if __name__ == "__main__":
  absltest.main()
