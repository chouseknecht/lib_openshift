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


class V1ResourceAccessReview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, kind=None, api_version=None, namespace=None, verb=None, resource_api_group=None, resource_api_version=None, resource=None, resource_name=None, content=None):
        """
        V1ResourceAccessReview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'namespace': 'str',
            'verb': 'str',
            'resource_api_group': 'str',
            'resource_api_version': 'str',
            'resource': 'str',
            'resource_name': 'str',
            'content': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'namespace': 'namespace',
            'verb': 'verb',
            'resource_api_group': 'resourceAPIGroup',
            'resource_api_version': 'resourceAPIVersion',
            'resource': 'resource',
            'resource_name': 'resourceName',
            'content': 'content'
        }

        self._kind = kind
        self._api_version = api_version
        self._namespace = namespace
        self._verb = verb
        self._resource_api_group = resource_api_group
        self._resource_api_version = resource_api_version
        self._resource = resource
        self._resource_name = resource_name
        self._content = content

    @property
    def kind(self):
        """
        Gets the kind of this V1ResourceAccessReview.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ResourceAccessReview.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ResourceAccessReview.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ResourceAccessReview.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ResourceAccessReview.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ResourceAccessReview.
        :type: str
        """

        self._api_version = api_version

    @property
    def namespace(self):
        """
        Gets the namespace of this V1ResourceAccessReview.
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces

        :return: The namespace of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1ResourceAccessReview.
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces

        :param namespace: The namespace of this V1ResourceAccessReview.
        :type: str
        """

        self._namespace = namespace

    @property
    def verb(self):
        """
        Gets the verb of this V1ResourceAccessReview.
        Verb is one of: get, list, watch, create, update, delete

        :return: The verb of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """
        Sets the verb of this V1ResourceAccessReview.
        Verb is one of: get, list, watch, create, update, delete

        :param verb: The verb of this V1ResourceAccessReview.
        :type: str
        """

        self._verb = verb

    @property
    def resource_api_group(self):
        """
        Gets the resource_api_group of this V1ResourceAccessReview.
        Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined

        :return: The resource_api_group of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource_api_group

    @resource_api_group.setter
    def resource_api_group(self, resource_api_group):
        """
        Sets the resource_api_group of this V1ResourceAccessReview.
        Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined

        :param resource_api_group: The resource_api_group of this V1ResourceAccessReview.
        :type: str
        """

        self._resource_api_group = resource_api_group

    @property
    def resource_api_version(self):
        """
        Gets the resource_api_version of this V1ResourceAccessReview.
        Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined

        :return: The resource_api_version of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource_api_version

    @resource_api_version.setter
    def resource_api_version(self, resource_api_version):
        """
        Sets the resource_api_version of this V1ResourceAccessReview.
        Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined

        :param resource_api_version: The resource_api_version of this V1ResourceAccessReview.
        :type: str
        """

        self._resource_api_version = resource_api_version

    @property
    def resource(self):
        """
        Gets the resource of this V1ResourceAccessReview.
        Resource is one of the existing resource types

        :return: The resource of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this V1ResourceAccessReview.
        Resource is one of the existing resource types

        :param resource: The resource of this V1ResourceAccessReview.
        :type: str
        """

        self._resource = resource

    @property
    def resource_name(self):
        """
        Gets the resource_name of this V1ResourceAccessReview.
        ResourceName is the name of the resource being requested for a \"get\" or deleted for a \"delete\"

        :return: The resource_name of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this V1ResourceAccessReview.
        ResourceName is the name of the resource being requested for a \"get\" or deleted for a \"delete\"

        :param resource_name: The resource_name of this V1ResourceAccessReview.
        :type: str
        """

        self._resource_name = resource_name

    @property
    def content(self):
        """
        Gets the content of this V1ResourceAccessReview.
        Content is the actual content of the request for create and update

        :return: The content of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this V1ResourceAccessReview.
        Content is the actual content of the request for create and update

        :param content: The content of this V1ResourceAccessReview.
        :type: str
        """

        self._content = content

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
