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


class V1beta1DeploymentRollback(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, kind=None, api_version=None, name=None, updated_annotations=None, rollback_to=None):
        """
        V1beta1DeploymentRollback - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'name': 'str',
            'updated_annotations': 'object',
            'rollback_to': 'V1beta1RollbackConfig'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'name': 'name',
            'updated_annotations': 'updatedAnnotations',
            'rollback_to': 'rollbackTo'
        }

        self._kind = kind
        self._api_version = api_version
        self._name = name
        self._updated_annotations = updated_annotations
        self._rollback_to = rollback_to

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1DeploymentRollback.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta1DeploymentRollback.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1DeploymentRollback.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta1DeploymentRollback.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta1DeploymentRollback.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1beta1DeploymentRollback.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta1DeploymentRollback.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta1DeploymentRollback.
        :type: str
        """

        self._api_version = api_version

    @property
    def name(self):
        """
        Gets the name of this V1beta1DeploymentRollback.
        Required: This must match the Name of a deployment.

        :return: The name of this V1beta1DeploymentRollback.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1DeploymentRollback.
        Required: This must match the Name of a deployment.

        :param name: The name of this V1beta1DeploymentRollback.
        :type: str
        """

        self._name = name

    @property
    def updated_annotations(self):
        """
        Gets the updated_annotations of this V1beta1DeploymentRollback.
        The annotations to be updated to a deployment

        :return: The updated_annotations of this V1beta1DeploymentRollback.
        :rtype: object
        """
        return self._updated_annotations

    @updated_annotations.setter
    def updated_annotations(self, updated_annotations):
        """
        Sets the updated_annotations of this V1beta1DeploymentRollback.
        The annotations to be updated to a deployment

        :param updated_annotations: The updated_annotations of this V1beta1DeploymentRollback.
        :type: object
        """

        self._updated_annotations = updated_annotations

    @property
    def rollback_to(self):
        """
        Gets the rollback_to of this V1beta1DeploymentRollback.
        The config of this deployment rollback.

        :return: The rollback_to of this V1beta1DeploymentRollback.
        :rtype: V1beta1RollbackConfig
        """
        return self._rollback_to

    @rollback_to.setter
    def rollback_to(self, rollback_to):
        """
        Sets the rollback_to of this V1beta1DeploymentRollback.
        The config of this deployment rollback.

        :param rollback_to: The rollback_to of this V1beta1DeploymentRollback.
        :type: V1beta1RollbackConfig
        """

        self._rollback_to = rollback_to

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
