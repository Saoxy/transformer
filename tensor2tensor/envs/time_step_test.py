# coding=utf-8
# Copyright 2023 The Tensor2Tensor Authors.
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

"""Tests for tensor2tensor.envs.time_step."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.envs import time_step

import tensorflow.compat.v1 as tf


class TimeStepTest(tf.test.TestCase):

  def test_create_time_step(self):
    ts = time_step.TimeStep.create_time_step(
        observation=1, done=True, raw_reward=1.0, processed_reward=1, action=1,
        info={1: 1, 2: 4})

    self.assertEqual(1, ts.observation)
    self.assertTrue(ts.done)
    self.assertNear(1.0, ts.raw_reward, 1e-6)
    self.assertEqual(1, ts.processed_reward)
    self.assertEqual(1, ts.action)
    self.assertEqual({1: 1, 2: 4}, ts.info)

  def test_replace(self):
    ts = time_step.TimeStep.create_time_step(observation=1, action=1)
    self.assertFalse(ts.done)

    tsr = ts.replace(action=2, done=True, info={1: 1, 2: 4})

    # Asert that ts didn't change.
    self.assertFalse(ts.done)
    self.assertEqual(1, ts.observation)
    self.assertEqual(1, ts.action)

    # But tsr is as expected.
    self.assertTrue(tsr.done)
    self.assertEqual(1, tsr.observation)  # unchanged
    self.assertEqual(2, tsr.action)  # changed
    self.assertEqual({1: 1, 2: 4}, tsr.info)


if __name__ == '__main__':
  tf.test.main()
