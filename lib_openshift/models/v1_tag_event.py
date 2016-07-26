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


class V1TagEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, created=None, docker_image_reference=None, image=None, generation=None):
        """
        V1TagEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'str',
            'docker_image_reference': 'str',
            'image': 'str',
            'generation': 'int'
        }

        self.attribute_map = {
            'created': 'created',
            'docker_image_reference': 'dockerImageReference',
            'image': 'image',
            'generation': 'generation'
        }

        self._created = created
        self._docker_image_reference = docker_image_reference
        self._image = image
        self._generation = generation

    @property
    def created(self):
        """
        Gets the created of this V1TagEvent.
        Created holds the time the TagEvent was created

        :return: The created of this V1TagEvent.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this V1TagEvent.
        Created holds the time the TagEvent was created

        :param created: The created of this V1TagEvent.
        :type: str
        """

        self._created = created

    @property
    def docker_image_reference(self):
        """
        Gets the docker_image_reference of this V1TagEvent.
        DockerImageReference is the string that can be used to pull this image

        :return: The docker_image_reference of this V1TagEvent.
        :rtype: str
        """
        return self._docker_image_reference

    @docker_image_reference.setter
    def docker_image_reference(self, docker_image_reference):
        """
        Sets the docker_image_reference of this V1TagEvent.
        DockerImageReference is the string that can be used to pull this image

        :param docker_image_reference: The docker_image_reference of this V1TagEvent.
        :type: str
        """

        self._docker_image_reference = docker_image_reference

    @property
    def image(self):
        """
        Gets the image of this V1TagEvent.
        Image is the image

        :return: The image of this V1TagEvent.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1TagEvent.
        Image is the image

        :param image: The image of this V1TagEvent.
        :type: str
        """

        self._image = image

    @property
    def generation(self):
        """
        Gets the generation of this V1TagEvent.
        Generation is the spec tag generation that resulted in this tag being updated

        :return: The generation of this V1TagEvent.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """
        Sets the generation of this V1TagEvent.
        Generation is the spec tag generation that resulted in this tag being updated

        :param generation: The generation of this V1TagEvent.
        :type: int
        """

        self._generation = generation

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
