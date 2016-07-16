# coding: utf-8

"""
    OpenShift v1 REST API

    The OpenShift API exposes operations for managing an enterprise Kubernetes cluster, including security and user management, application deployments, image and source builds, HTTP(s) routing, and project management.

    OpenAPI spec version: v1
    
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


class V1ImageStreamTag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, kind=None, api_version=None, metadata=None, tag=None, generation=None, conditions=None, image=None):
        """
        V1ImageStreamTag - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'tag': 'V1TagReference',
            'generation': 'int',
            'conditions': 'list[V1TagEventCondition]',
            'image': 'V1Image'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'tag': 'tag',
            'generation': 'generation',
            'conditions': 'conditions',
            'image': 'image'
        }

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._tag = tag
        self._generation = generation
        self._conditions = conditions
        self._image = image

    @property
    def kind(self):
        """
        Gets the kind of this V1ImageStreamTag.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ImageStreamTag.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ImageStreamTag.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ImageStreamTag.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ImageStreamTag.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ImageStreamTag.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ImageStreamTag.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ImageStreamTag.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ImageStreamTag.
        Standard object's metadata.

        :return: The metadata of this V1ImageStreamTag.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ImageStreamTag.
        Standard object's metadata.

        :param metadata: The metadata of this V1ImageStreamTag.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def tag(self):
        """
        Gets the tag of this V1ImageStreamTag.
        Tag is the spec tag associated with this image stream tag, and it may be null if only pushes have occured to this image stream.

        :return: The tag of this V1ImageStreamTag.
        :rtype: V1TagReference
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this V1ImageStreamTag.
        Tag is the spec tag associated with this image stream tag, and it may be null if only pushes have occured to this image stream.

        :param tag: The tag of this V1ImageStreamTag.
        :type: V1TagReference
        """

        self._tag = tag

    @property
    def generation(self):
        """
        Gets the generation of this V1ImageStreamTag.
        Generation is the current generation of the tagged image - if tag is provided and this value is not equal to the tag generation, a user has requested an import that has not completed, or Conditions will be filled out indicating any error.

        :return: The generation of this V1ImageStreamTag.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """
        Sets the generation of this V1ImageStreamTag.
        Generation is the current generation of the tagged image - if tag is provided and this value is not equal to the tag generation, a user has requested an import that has not completed, or Conditions will be filled out indicating any error.

        :param generation: The generation of this V1ImageStreamTag.
        :type: int
        """

        self._generation = generation

    @property
    def conditions(self):
        """
        Gets the conditions of this V1ImageStreamTag.
        Conditions is an array of conditions that apply to the image stream tag.

        :return: The conditions of this V1ImageStreamTag.
        :rtype: list[V1TagEventCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1ImageStreamTag.
        Conditions is an array of conditions that apply to the image stream tag.

        :param conditions: The conditions of this V1ImageStreamTag.
        :type: list[V1TagEventCondition]
        """

        self._conditions = conditions

    @property
    def image(self):
        """
        Gets the image of this V1ImageStreamTag.
        Image associated with the ImageStream and tag.

        :return: The image of this V1ImageStreamTag.
        :rtype: V1Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1ImageStreamTag.
        Image associated with the ImageStream and tag.

        :param image: The image of this V1ImageStreamTag.
        :type: V1Image
        """

        self._image = image

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