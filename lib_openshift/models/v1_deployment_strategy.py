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


class V1DeploymentStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, type=None, custom_params=None, recreate_params=None, rolling_params=None, resources=None, labels=None, annotations=None):
        """
        V1DeploymentStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'custom_params': 'V1CustomDeploymentStrategyParams',
            'recreate_params': 'V1RecreateDeploymentStrategyParams',
            'rolling_params': 'V1RollingDeploymentStrategyParams',
            'resources': 'V1ResourceRequirements',
            'labels': 'object',
            'annotations': 'object'
        }

        self.attribute_map = {
            'type': 'type',
            'custom_params': 'customParams',
            'recreate_params': 'recreateParams',
            'rolling_params': 'rollingParams',
            'resources': 'resources',
            'labels': 'labels',
            'annotations': 'annotations'
        }

        self._type = type
        self._custom_params = custom_params
        self._recreate_params = recreate_params
        self._rolling_params = rolling_params
        self._resources = resources
        self._labels = labels
        self._annotations = annotations

    @property
    def type(self):
        """
        Gets the type of this V1DeploymentStrategy.
        Type is the name of a deployment strategy.

        :return: The type of this V1DeploymentStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1DeploymentStrategy.
        Type is the name of a deployment strategy.

        :param type: The type of this V1DeploymentStrategy.
        :type: str
        """

        self._type = type

    @property
    def custom_params(self):
        """
        Gets the custom_params of this V1DeploymentStrategy.
        CustomParams are the input to the Custom deployment strategy.

        :return: The custom_params of this V1DeploymentStrategy.
        :rtype: V1CustomDeploymentStrategyParams
        """
        return self._custom_params

    @custom_params.setter
    def custom_params(self, custom_params):
        """
        Sets the custom_params of this V1DeploymentStrategy.
        CustomParams are the input to the Custom deployment strategy.

        :param custom_params: The custom_params of this V1DeploymentStrategy.
        :type: V1CustomDeploymentStrategyParams
        """

        self._custom_params = custom_params

    @property
    def recreate_params(self):
        """
        Gets the recreate_params of this V1DeploymentStrategy.
        RecreateParams are the input to the Recreate deployment strategy.

        :return: The recreate_params of this V1DeploymentStrategy.
        :rtype: V1RecreateDeploymentStrategyParams
        """
        return self._recreate_params

    @recreate_params.setter
    def recreate_params(self, recreate_params):
        """
        Sets the recreate_params of this V1DeploymentStrategy.
        RecreateParams are the input to the Recreate deployment strategy.

        :param recreate_params: The recreate_params of this V1DeploymentStrategy.
        :type: V1RecreateDeploymentStrategyParams
        """

        self._recreate_params = recreate_params

    @property
    def rolling_params(self):
        """
        Gets the rolling_params of this V1DeploymentStrategy.
        RollingParams are the input to the Rolling deployment strategy.

        :return: The rolling_params of this V1DeploymentStrategy.
        :rtype: V1RollingDeploymentStrategyParams
        """
        return self._rolling_params

    @rolling_params.setter
    def rolling_params(self, rolling_params):
        """
        Sets the rolling_params of this V1DeploymentStrategy.
        RollingParams are the input to the Rolling deployment strategy.

        :param rolling_params: The rolling_params of this V1DeploymentStrategy.
        :type: V1RollingDeploymentStrategyParams
        """

        self._rolling_params = rolling_params

    @property
    def resources(self):
        """
        Gets the resources of this V1DeploymentStrategy.
        Resources contains resource requirements to execute the deployment and any hooks

        :return: The resources of this V1DeploymentStrategy.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1DeploymentStrategy.
        Resources contains resource requirements to execute the deployment and any hooks

        :param resources: The resources of this V1DeploymentStrategy.
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def labels(self):
        """
        Gets the labels of this V1DeploymentStrategy.
        Labels is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :return: The labels of this V1DeploymentStrategy.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this V1DeploymentStrategy.
        Labels is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :param labels: The labels of this V1DeploymentStrategy.
        :type: object
        """

        self._labels = labels

    @property
    def annotations(self):
        """
        Gets the annotations of this V1DeploymentStrategy.
        Annotations is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :return: The annotations of this V1DeploymentStrategy.
        :rtype: object
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this V1DeploymentStrategy.
        Annotations is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :param annotations: The annotations of this V1DeploymentStrategy.
        :type: object
        """

        self._annotations = annotations

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
