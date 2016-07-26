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


class V1beta1DeploymentStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, observed_generation=None, replicas=None, updated_replicas=None, available_replicas=None, unavailable_replicas=None):
        """
        V1beta1DeploymentStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observed_generation': 'int',
            'replicas': 'int',
            'updated_replicas': 'int',
            'available_replicas': 'int',
            'unavailable_replicas': 'int'
        }

        self.attribute_map = {
            'observed_generation': 'observedGeneration',
            'replicas': 'replicas',
            'updated_replicas': 'updatedReplicas',
            'available_replicas': 'availableReplicas',
            'unavailable_replicas': 'unavailableReplicas'
        }

        self._observed_generation = observed_generation
        self._replicas = replicas
        self._updated_replicas = updated_replicas
        self._available_replicas = available_replicas
        self._unavailable_replicas = unavailable_replicas

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1beta1DeploymentStatus.
        The generation observed by the deployment controller.

        :return: The observed_generation of this V1beta1DeploymentStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1beta1DeploymentStatus.
        The generation observed by the deployment controller.

        :param observed_generation: The observed_generation of this V1beta1DeploymentStatus.
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def replicas(self):
        """
        Gets the replicas of this V1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment (their labels match the selector).

        :return: The replicas of this V1beta1DeploymentStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment (their labels match the selector).

        :param replicas: The replicas of this V1beta1DeploymentStatus.
        :type: int
        """

        self._replicas = replicas

    @property
    def updated_replicas(self):
        """
        Gets the updated_replicas of this V1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment that have the desired template spec.

        :return: The updated_replicas of this V1beta1DeploymentStatus.
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """
        Sets the updated_replicas of this V1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment that have the desired template spec.

        :param updated_replicas: The updated_replicas of this V1beta1DeploymentStatus.
        :type: int
        """

        self._updated_replicas = updated_replicas

    @property
    def available_replicas(self):
        """
        Gets the available_replicas of this V1beta1DeploymentStatus.
        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.

        :return: The available_replicas of this V1beta1DeploymentStatus.
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """
        Sets the available_replicas of this V1beta1DeploymentStatus.
        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.

        :param available_replicas: The available_replicas of this V1beta1DeploymentStatus.
        :type: int
        """

        self._available_replicas = available_replicas

    @property
    def unavailable_replicas(self):
        """
        Gets the unavailable_replicas of this V1beta1DeploymentStatus.
        Total number of unavailable pods targeted by this deployment.

        :return: The unavailable_replicas of this V1beta1DeploymentStatus.
        :rtype: int
        """
        return self._unavailable_replicas

    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas):
        """
        Sets the unavailable_replicas of this V1beta1DeploymentStatus.
        Total number of unavailable pods targeted by this deployment.

        :param unavailable_replicas: The unavailable_replicas of this V1beta1DeploymentStatus.
        :type: int
        """

        self._unavailable_replicas = unavailable_replicas

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
