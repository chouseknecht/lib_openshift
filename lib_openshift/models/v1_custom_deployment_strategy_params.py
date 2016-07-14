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


class V1CustomDeploymentStrategyParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, image=None, environment=None, command=None):
        """
        V1CustomDeploymentStrategyParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'image': 'str',
            'environment': 'list[V1EnvVar]',
            'command': 'list[str]'
        }

        self.attribute_map = {
            'image': 'image',
            'environment': 'environment',
            'command': 'command'
        }

        self._image = image
        self._environment = environment
        self._command = command

    @property
    def image(self):
        """
        Gets the image of this V1CustomDeploymentStrategyParams.
        Image specifies a Docker image which can carry out a deployment.

        :return: The image of this V1CustomDeploymentStrategyParams.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1CustomDeploymentStrategyParams.
        Image specifies a Docker image which can carry out a deployment.

        :param image: The image of this V1CustomDeploymentStrategyParams.
        :type: str
        """

        self._image = image

    @property
    def environment(self):
        """
        Gets the environment of this V1CustomDeploymentStrategyParams.
        Environment holds the environment which will be given to the container for Image.

        :return: The environment of this V1CustomDeploymentStrategyParams.
        :rtype: list[V1EnvVar]
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this V1CustomDeploymentStrategyParams.
        Environment holds the environment which will be given to the container for Image.

        :param environment: The environment of this V1CustomDeploymentStrategyParams.
        :type: list[V1EnvVar]
        """

        self._environment = environment

    @property
    def command(self):
        """
        Gets the command of this V1CustomDeploymentStrategyParams.
        Command is optional and overrides CMD in the container Image.

        :return: The command of this V1CustomDeploymentStrategyParams.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this V1CustomDeploymentStrategyParams.
        Command is optional and overrides CMD in the container Image.

        :param command: The command of this V1CustomDeploymentStrategyParams.
        :type: list[str]
        """

        self._command = command

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
