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


class V1LifecycleHook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, failure_policy=None, exec_new_pod=None, tag_images=None):
        """
        V1LifecycleHook - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'failure_policy': 'str',
            'exec_new_pod': 'V1ExecNewPodHook',
            'tag_images': 'list[V1TagImageHook]'
        }

        self.attribute_map = {
            'failure_policy': 'failurePolicy',
            'exec_new_pod': 'execNewPod',
            'tag_images': 'tagImages'
        }

        self._failure_policy = failure_policy
        self._exec_new_pod = exec_new_pod
        self._tag_images = tag_images

    @property
    def failure_policy(self):
        """
        Gets the failure_policy of this V1LifecycleHook.
        FailurePolicy specifies what action to take if the hook fails.

        :return: The failure_policy of this V1LifecycleHook.
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """
        Sets the failure_policy of this V1LifecycleHook.
        FailurePolicy specifies what action to take if the hook fails.

        :param failure_policy: The failure_policy of this V1LifecycleHook.
        :type: str
        """

        self._failure_policy = failure_policy

    @property
    def exec_new_pod(self):
        """
        Gets the exec_new_pod of this V1LifecycleHook.
        ExecNewPod specifies the options for a lifecycle hook backed by a pod.

        :return: The exec_new_pod of this V1LifecycleHook.
        :rtype: V1ExecNewPodHook
        """
        return self._exec_new_pod

    @exec_new_pod.setter
    def exec_new_pod(self, exec_new_pod):
        """
        Sets the exec_new_pod of this V1LifecycleHook.
        ExecNewPod specifies the options for a lifecycle hook backed by a pod.

        :param exec_new_pod: The exec_new_pod of this V1LifecycleHook.
        :type: V1ExecNewPodHook
        """

        self._exec_new_pod = exec_new_pod

    @property
    def tag_images(self):
        """
        Gets the tag_images of this V1LifecycleHook.
        TagImages instructs the deployer to tag the current image referenced under a container onto an image stream tag.

        :return: The tag_images of this V1LifecycleHook.
        :rtype: list[V1TagImageHook]
        """
        return self._tag_images

    @tag_images.setter
    def tag_images(self, tag_images):
        """
        Sets the tag_images of this V1LifecycleHook.
        TagImages instructs the deployer to tag the current image referenced under a container onto an image stream tag.

        :param tag_images: The tag_images of this V1LifecycleHook.
        :type: list[V1TagImageHook]
        """

        self._tag_images = tag_images

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
