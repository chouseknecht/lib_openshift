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


class V1RollingDeploymentStrategyParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, update_period_seconds=None, interval_seconds=None, timeout_seconds=None, max_unavailable=None, max_surge=None, update_percent=None, pre=None, post=None):
        """
        V1RollingDeploymentStrategyParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'update_period_seconds': 'int',
            'interval_seconds': 'int',
            'timeout_seconds': 'int',
            'max_unavailable': 'str',
            'max_surge': 'str',
            'update_percent': 'int',
            'pre': 'V1LifecycleHook',
            'post': 'V1LifecycleHook'
        }

        self.attribute_map = {
            'update_period_seconds': 'updatePeriodSeconds',
            'interval_seconds': 'intervalSeconds',
            'timeout_seconds': 'timeoutSeconds',
            'max_unavailable': 'maxUnavailable',
            'max_surge': 'maxSurge',
            'update_percent': 'updatePercent',
            'pre': 'pre',
            'post': 'post'
        }

        self._update_period_seconds = update_period_seconds
        self._interval_seconds = interval_seconds
        self._timeout_seconds = timeout_seconds
        self._max_unavailable = max_unavailable
        self._max_surge = max_surge
        self._update_percent = update_percent
        self._pre = pre
        self._post = post

    @property
    def update_period_seconds(self):
        """
        Gets the update_period_seconds of this V1RollingDeploymentStrategyParams.
        UpdatePeriodSeconds is the time to wait between individual pod updates. If the value is nil, a default will be used.

        :return: The update_period_seconds of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._update_period_seconds

    @update_period_seconds.setter
    def update_period_seconds(self, update_period_seconds):
        """
        Sets the update_period_seconds of this V1RollingDeploymentStrategyParams.
        UpdatePeriodSeconds is the time to wait between individual pod updates. If the value is nil, a default will be used.

        :param update_period_seconds: The update_period_seconds of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._update_period_seconds = update_period_seconds

    @property
    def interval_seconds(self):
        """
        Gets the interval_seconds of this V1RollingDeploymentStrategyParams.
        IntervalSeconds is the time to wait between polling deployment status after update. If the value is nil, a default will be used.

        :return: The interval_seconds of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._interval_seconds

    @interval_seconds.setter
    def interval_seconds(self, interval_seconds):
        """
        Sets the interval_seconds of this V1RollingDeploymentStrategyParams.
        IntervalSeconds is the time to wait between polling deployment status after update. If the value is nil, a default will be used.

        :param interval_seconds: The interval_seconds of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._interval_seconds = interval_seconds

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this V1RollingDeploymentStrategyParams.
        TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used.

        :return: The timeout_seconds of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this V1RollingDeploymentStrategyParams.
        TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used.

        :param timeout_seconds: The timeout_seconds of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    @property
    def max_unavailable(self):
        """
        Gets the max_unavailable of this V1RollingDeploymentStrategyParams.
        MaxUnavailable is the maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of update (ex: 10%). Absolute number is calculated from percentage by rounding up.  This cannot be 0 if MaxSurge is 0. By default, 25% is used.  Example: when this is set to 30%, the old RC can be scaled down by 30% immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that at least 70% of original number of pods are available at all times during the update.

        :return: The max_unavailable of this V1RollingDeploymentStrategyParams.
        :rtype: str
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        """
        Sets the max_unavailable of this V1RollingDeploymentStrategyParams.
        MaxUnavailable is the maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of update (ex: 10%). Absolute number is calculated from percentage by rounding up.  This cannot be 0 if MaxSurge is 0. By default, 25% is used.  Example: when this is set to 30%, the old RC can be scaled down by 30% immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that at least 70% of original number of pods are available at all times during the update.

        :param max_unavailable: The max_unavailable of this V1RollingDeploymentStrategyParams.
        :type: str
        """

        self._max_unavailable = max_unavailable

    @property
    def max_surge(self):
        """
        Gets the max_surge of this V1RollingDeploymentStrategyParams.
        MaxSurge is the maximum number of pods that can be scheduled above the original number of pods. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up.  This cannot be 0 if MaxUnavailable is 0. By default, 25% is used.  Example: when this is set to 30%, the new RC can be scaled up by 30% immediately when the rolling update starts. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is atmost 130% of original pods.

        :return: The max_surge of this V1RollingDeploymentStrategyParams.
        :rtype: str
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        """
        Sets the max_surge of this V1RollingDeploymentStrategyParams.
        MaxSurge is the maximum number of pods that can be scheduled above the original number of pods. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up.  This cannot be 0 if MaxUnavailable is 0. By default, 25% is used.  Example: when this is set to 30%, the new RC can be scaled up by 30% immediately when the rolling update starts. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is atmost 130% of original pods.

        :param max_surge: The max_surge of this V1RollingDeploymentStrategyParams.
        :type: str
        """

        self._max_surge = max_surge

    @property
    def update_percent(self):
        """
        Gets the update_percent of this V1RollingDeploymentStrategyParams.
        UpdatePercent is the percentage of replicas to scale up or down each interval. If nil, one replica will be scaled up and down each interval. If negative, the scale order will be down/up instead of up/down. DEPRECATED: Use MaxUnavailable/MaxSurge instead.

        :return: The update_percent of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._update_percent

    @update_percent.setter
    def update_percent(self, update_percent):
        """
        Sets the update_percent of this V1RollingDeploymentStrategyParams.
        UpdatePercent is the percentage of replicas to scale up or down each interval. If nil, one replica will be scaled up and down each interval. If negative, the scale order will be down/up instead of up/down. DEPRECATED: Use MaxUnavailable/MaxSurge instead.

        :param update_percent: The update_percent of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._update_percent = update_percent

    @property
    def pre(self):
        """
        Gets the pre of this V1RollingDeploymentStrategyParams.
        Pre is a lifecycle hook which is executed before the deployment process begins. All LifecycleHookFailurePolicy values are supported.

        :return: The pre of this V1RollingDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._pre

    @pre.setter
    def pre(self, pre):
        """
        Sets the pre of this V1RollingDeploymentStrategyParams.
        Pre is a lifecycle hook which is executed before the deployment process begins. All LifecycleHookFailurePolicy values are supported.

        :param pre: The pre of this V1RollingDeploymentStrategyParams.
        :type: V1LifecycleHook
        """

        self._pre = pre

    @property
    def post(self):
        """
        Gets the post of this V1RollingDeploymentStrategyParams.
        Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. The LifecycleHookFailurePolicyAbort policy is NOT supported.

        :return: The post of this V1RollingDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._post

    @post.setter
    def post(self, post):
        """
        Sets the post of this V1RollingDeploymentStrategyParams.
        Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. The LifecycleHookFailurePolicyAbort policy is NOT supported.

        :param post: The post of this V1RollingDeploymentStrategyParams.
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
