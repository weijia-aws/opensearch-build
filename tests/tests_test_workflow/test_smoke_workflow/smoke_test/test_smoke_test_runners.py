# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import unittest
from unittest.mock import MagicMock, patch

from test_workflow.smoke_test.smoke_test_runners import SmokeTestRunners


class TestSmokeTestRunners(unittest.TestCase):

    def test_opensearch(self) -> None:

        mock_args = MagicMock()
        mock_test_manifest = MagicMock()
        mock_test_manifest.name = "OpenSearch"

        mock_opensearch_runner_object = MagicMock()
        mock_opensearch_runner = MagicMock()
        mock_opensearch_runner.return_value = mock_opensearch_runner_object

        with patch.dict("test_workflow.smoke_test.smoke_test_runners.SmokeTestRunners.RUNNERS", {
            "OpenSearch": mock_opensearch_runner
        }):
            runner = SmokeTestRunners.from_test_manifest(mock_args, mock_test_manifest)
            self.assertEqual(runner, mock_opensearch_runner_object)
            mock_opensearch_runner.assert_called_once_with(mock_args, mock_test_manifest)
