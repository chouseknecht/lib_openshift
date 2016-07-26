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


class V1RecreateDeploymentStrategyParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, timeout_seconds=None, pre=None, mid=None, post=None):
        """
        V1RecreateDeploymentStrategyParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timeout_seconds': 'int',
            'pre': 'V1LifecycleHook',
            'mid': 'V1LifecycleHook',
            'post': 'V1LifecycleHook'
        }

        self.attribute_map = {
            'timeout_seconds': 'timeoutSeconds',
            'pre': 'pre',
            'mid': 'mid',
            'post': 'post'
        }

        self._timeout_seconds = timeout_seconds
        self._pre = pre
        self._mid = mid
        self._post = post

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this V1RecreateDeploymentStrategyParams.
        TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used.

        :return: The timeout_seconds of this V1RecreateDeploymentStrategyParams.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this V1RecreateDeploymentStrategyParams.
        TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used.

        :param timeout_seconds: The timeout_seconds of this V1RecreateDeploymentStrategyParams.
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    @property
    def pre(self):
        """
        Gets the pre of this V1RecreateDeploymentStrategyParams.
        Pre is a lifecycle hook which is executed before the strategy manipulates the deployment. All LifecycleHookFailurePolicy values are supported.

        :return: The pre of this V1RecreateDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._pre

    @pre.setter
    def pre(self, pre):
        """
        Sets the pre of this V1RecreateDeploymentStrategyParams.
        Pre is a lifecycle hook which is executed before the strategy manipulates the deployment. All LifecycleHookFailurePolicy values are supported.

        :param pre: The pre of this V1RecreateDeploymentStrategyParams.
        :type: V1LifecycleHook
        """

        self._pre = pre

    @property
    def mid(self):
        """
        Gets the mid of this V1RecreateDeploymentStrategyParams.
        Mid is a lifecycle hook which is executed while the deployment is scaled down to zero before the first new pod is created. All LifecycleHookFailurePolicy values are supported.

        :return: The mid of this V1RecreateDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """
        Sets the mid of this V1RecreateDeploymentStrategyParams.
        Mid is a lifecycle hook which is executed while the deployment is scaled down to zero before the first new pod is created. All LifecycleHookFailurePolicy values are supported.

        :param mid: The mid of this V1RecreateDeploymentStrategyParams.
        :type: V1LifecycleHook
        """

        self._mid = mid

    @property
    def post(self):
        """
        Gets the post of this V1RecreateDeploymentStrategyParams.
        Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. All LifecycleHookFailurePolicy values are supported.

        :return: The post of this V1RecreateDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._post

    @post.setter
    def post(self, post):
        """
        Sets the post of this V1RecreateDeploymentStrategyParams.
        Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. All LifecycleHookFailurePolicy values are supported.

        :param post: The post of this V1RecreateDeploymentStrategyParams.
        :type: V1LifecycleHook
        """

        self._post = post

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
