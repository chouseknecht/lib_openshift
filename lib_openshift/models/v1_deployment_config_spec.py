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

from pprint import pformat
from six import iteritems
import re


class V1DeploymentConfigSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, strategy=None, triggers=None, replicas=None, test=None, selector=None, template=None):
        """
        V1DeploymentConfigSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'strategy': 'V1DeploymentStrategy',
            'triggers': 'list[V1DeploymentTriggerPolicy]',
            'replicas': 'int',
            'test': 'bool',
            'selector': 'object',
            'template': 'V1PodTemplateSpec'
        }

        self.attribute_map = {
            'strategy': 'strategy',
            'triggers': 'triggers',
            'replicas': 'replicas',
            'test': 'test',
            'selector': 'selector',
            'template': 'template'
        }

        self._strategy = strategy
        self._triggers = triggers
        self._replicas = replicas
        self._test = test
        self._selector = selector
        self._template = template

    @property
    def strategy(self):
        """
        Gets the strategy of this V1DeploymentConfigSpec.
        Strategy describes how a deployment is executed.

        :return: The strategy of this V1DeploymentConfigSpec.
        :rtype: V1DeploymentStrategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Sets the strategy of this V1DeploymentConfigSpec.
        Strategy describes how a deployment is executed.

        :param strategy: The strategy of this V1DeploymentConfigSpec.
        :type: V1DeploymentStrategy
        """

        self._strategy = strategy

    @property
    def triggers(self):
        """
        Gets the triggers of this V1DeploymentConfigSpec.
        Triggers determine how updates to a DeploymentConfig result in new deployments. If no triggers are defined, a new deployment can only occur as a result of an explicit client update to the DeploymentConfig with a new LatestVersion.

        :return: The triggers of this V1DeploymentConfigSpec.
        :rtype: list[V1DeploymentTriggerPolicy]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """
        Sets the triggers of this V1DeploymentConfigSpec.
        Triggers determine how updates to a DeploymentConfig result in new deployments. If no triggers are defined, a new deployment can only occur as a result of an explicit client update to the DeploymentConfig with a new LatestVersion.

        :param triggers: The triggers of this V1DeploymentConfigSpec.
        :type: list[V1DeploymentTriggerPolicy]
        """

        self._triggers = triggers

    @property
    def replicas(self):
        """
        Gets the replicas of this V1DeploymentConfigSpec.
        Replicas is the number of desired replicas.

        :return: The replicas of this V1DeploymentConfigSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1DeploymentConfigSpec.
        Replicas is the number of desired replicas.

        :param replicas: The replicas of this V1DeploymentConfigSpec.
        :type: int
        """

        self._replicas = replicas

    @property
    def test(self):
        """
        Gets the test of this V1DeploymentConfigSpec.
        Test ensures that this deployment config will have zero replicas except while a deployment is running. This allows the deployment config to be used as a continuous deployment test - triggering on images, running the deployment, and then succeeding or failing. Post strategy hooks and After actions can be used to integrate successful deployment with an action.

        :return: The test of this V1DeploymentConfigSpec.
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """
        Sets the test of this V1DeploymentConfigSpec.
        Test ensures that this deployment config will have zero replicas except while a deployment is running. This allows the deployment config to be used as a continuous deployment test - triggering on images, running the deployment, and then succeeding or failing. Post strategy hooks and After actions can be used to integrate successful deployment with an action.

        :param test: The test of this V1DeploymentConfigSpec.
        :type: bool
        """

        self._test = test

    @property
    def selector(self):
        """
        Gets the selector of this V1DeploymentConfigSpec.
        Selector is a label query over pods that should match the Replicas count.

        :return: The selector of this V1DeploymentConfigSpec.
        :rtype: object
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1DeploymentConfigSpec.
        Selector is a label query over pods that should match the Replicas count.

        :param selector: The selector of this V1DeploymentConfigSpec.
        :type: object
        """

        self._selector = selector

    @property
    def template(self):
        """
        Gets the template of this V1DeploymentConfigSpec.
        Template is the object that describes the pod that will be created if insufficient replicas are detected.

        :return: The template of this V1DeploymentConfigSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1DeploymentConfigSpec.
        Template is the object that describes the pod that will be created if insufficient replicas are detected.

        :param template: The template of this V1DeploymentConfigSpec.
        :type: V1PodTemplateSpec
        """

        self._template = template

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
