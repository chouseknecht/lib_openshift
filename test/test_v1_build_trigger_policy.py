# coding: utf-8

"""
    

    

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import lib_openshift
from lib_openshift.rest import ApiException
from lib_openshift.models.v1_build_trigger_policy import V1BuildTriggerPolicy


class TestV1BuildTriggerPolicy(unittest.TestCase):
    """ V1BuildTriggerPolicy unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1BuildTriggerPolicy(self):
        """
        Test V1BuildTriggerPolicy
        """
        model = lib_openshift.models.v1_build_trigger_policy.V1BuildTriggerPolicy()


if __name__ == '__main__':
    unittest.main()
