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


class V1DeploymentTriggerImageChangeParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, automatic=None, container_names=None, _from=None, last_triggered_image=None):
        """
        V1DeploymentTriggerImageChangeParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'automatic': 'bool',
            'container_names': 'list[str]',
            '_from': 'V1ObjectReference',
            'last_triggered_image': 'str'
        }

        self.attribute_map = {
            'automatic': 'automatic',
            'container_names': 'containerNames',
            '_from': 'from',
            'last_triggered_image': 'lastTriggeredImage'
        }


        self._automatic = automatic
        self._container_names = container_names
        self.__from = _from
        self._last_triggered_image = last_triggered_image

    @property
    def automatic(self):
        """
        Gets the automatic of this V1DeploymentTriggerImageChangeParams.
        Automatic means that the detection of a new tag value should result in a new deployment.

        :return: The automatic of this V1DeploymentTriggerImageChangeParams.
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """
        Sets the automatic of this V1DeploymentTriggerImageChangeParams.
        Automatic means that the detection of a new tag value should result in a new deployment.

        :param automatic: The automatic of this V1DeploymentTriggerImageChangeParams.
        :type: bool
        """

        self._automatic = automatic

    @property
    def container_names(self):
        """
        Gets the container_names of this V1DeploymentTriggerImageChangeParams.
        ContainerNames is used to restrict tag updates to the specified set of container names in a pod.

        :return: The container_names of this V1DeploymentTriggerImageChangeParams.
        :rtype: list[str]
        """
        return self._container_names

    @container_names.setter
    def container_names(self, container_names):
        """
        Sets the container_names of this V1DeploymentTriggerImageChangeParams.
        ContainerNames is used to restrict tag updates to the specified set of container names in a pod.

        :param container_names: The container_names of this V1DeploymentTriggerImageChangeParams.
        :type: list[str]
        """

        self._container_names = container_names

    @property
    def _from(self):
        """
        Gets the _from of this V1DeploymentTriggerImageChangeParams.
        From is a reference to an image stream tag to watch for changes. From.Name is the only required subfield - if From.Namespace is blank, the namespace of the current deployment trigger will be used.

        :return: The _from of this V1DeploymentTriggerImageChangeParams.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1DeploymentTriggerImageChangeParams.
        From is a reference to an image stream tag to watch for changes. From.Name is the only required subfield - if From.Namespace is blank, the namespace of the current deployment trigger will be used.

        :param _from: The _from of this V1DeploymentTriggerImageChangeParams.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def last_triggered_image(self):
        """
        Gets the last_triggered_image of this V1DeploymentTriggerImageChangeParams.
        LastTriggeredImage is the last image to be triggered.

        :return: The last_triggered_image of this V1DeploymentTriggerImageChangeParams.
        :rtype: str
        """
        return self._last_triggered_image

    @last_triggered_image.setter
    def last_triggered_image(self, last_triggered_image):
        """
        Sets the last_triggered_image of this V1DeploymentTriggerImageChangeParams.
        LastTriggeredImage is the last image to be triggered.

        :param last_triggered_image: The last_triggered_image of this V1DeploymentTriggerImageChangeParams.
        :type: str
        """

        self._last_triggered_image = last_triggered_image

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
