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


class V1DeploymentConfigRollbackSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, include_triggers=None, include_template=None, include_replication_meta=None, include_strategy=None):
        """
        V1DeploymentConfigRollbackSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'V1ObjectReference',
            'include_triggers': 'bool',
            'include_template': 'bool',
            'include_replication_meta': 'bool',
            'include_strategy': 'bool'
        }

        self.attribute_map = {
            '_from': 'from',
            'include_triggers': 'includeTriggers',
            'include_template': 'includeTemplate',
            'include_replication_meta': 'includeReplicationMeta',
            'include_strategy': 'includeStrategy'
        }


        self.__from = _from
        self._include_triggers = include_triggers
        self._include_template = include_template
        self._include_replication_meta = include_replication_meta
        self._include_strategy = include_strategy

    @property
    def _from(self):
        """
        Gets the _from of this V1DeploymentConfigRollbackSpec.
        From points to a ReplicationController which is a deployment.

        :return: The _from of this V1DeploymentConfigRollbackSpec.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1DeploymentConfigRollbackSpec.
        From points to a ReplicationController which is a deployment.

        :param _from: The _from of this V1DeploymentConfigRollbackSpec.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def include_triggers(self):
        """
        Gets the include_triggers of this V1DeploymentConfigRollbackSpec.
        IncludeTriggers specifies whether to include config Triggers.

        :return: The include_triggers of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_triggers

    @include_triggers.setter
    def include_triggers(self, include_triggers):
        """
        Sets the include_triggers of this V1DeploymentConfigRollbackSpec.
        IncludeTriggers specifies whether to include config Triggers.

        :param include_triggers: The include_triggers of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """

        self._include_triggers = include_triggers

    @property
    def include_template(self):
        """
        Gets the include_template of this V1DeploymentConfigRollbackSpec.
        IncludeTemplate specifies whether to include the PodTemplateSpec.

        :return: The include_template of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_template

    @include_template.setter
    def include_template(self, include_template):
        """
        Sets the include_template of this V1DeploymentConfigRollbackSpec.
        IncludeTemplate specifies whether to include the PodTemplateSpec.

        :param include_template: The include_template of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """

        self._include_template = include_template

    @property
    def include_replication_meta(self):
        """
        Gets the include_replication_meta of this V1DeploymentConfigRollbackSpec.
        IncludeReplicationMeta specifies whether to include the replica count and selector.

        :return: The include_replication_meta of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_replication_meta

    @include_replication_meta.setter
    def include_replication_meta(self, include_replication_meta):
        """
        Sets the include_replication_meta of this V1DeploymentConfigRollbackSpec.
        IncludeReplicationMeta specifies whether to include the replica count and selector.

        :param include_replication_meta: The include_replication_meta of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """

        self._include_replication_meta = include_replication_meta

    @property
    def include_strategy(self):
        """
        Gets the include_strategy of this V1DeploymentConfigRollbackSpec.
        IncludeStrategy specifies whether to include the deployment Strategy.

        :return: The include_strategy of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_strategy

    @include_strategy.setter
    def include_strategy(self, include_strategy):
        """
        Sets the include_strategy of this V1DeploymentConfigRollbackSpec.
        IncludeStrategy specifies whether to include the deployment Strategy.

        :param include_strategy: The include_strategy of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """

        self._include_strategy = include_strategy

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
