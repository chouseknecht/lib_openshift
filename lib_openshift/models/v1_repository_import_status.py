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


class V1RepositoryImportStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, status=None, images=None, additional_tags=None):
        """
        V1RepositoryImportStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'UnversionedStatus',
            'images': 'list[V1ImageImportStatus]',
            'additional_tags': 'list[str]'
        }

        self.attribute_map = {
            'status': 'status',
            'images': 'images',
            'additional_tags': 'additionalTags'
        }

        self._status = status
        self._images = images
        self._additional_tags = additional_tags

    @property
    def status(self):
        """
        Gets the status of this V1RepositoryImportStatus.
        Status reflects whether any failure occurred during import

        :return: The status of this V1RepositoryImportStatus.
        :rtype: UnversionedStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1RepositoryImportStatus.
        Status reflects whether any failure occurred during import

        :param status: The status of this V1RepositoryImportStatus.
        :type: UnversionedStatus
        """

        self._status = status

    @property
    def images(self):
        """
        Gets the images of this V1RepositoryImportStatus.
        Images is a list of images successfully retrieved by the import of the repository.

        :return: The images of this V1RepositoryImportStatus.
        :rtype: list[V1ImageImportStatus]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this V1RepositoryImportStatus.
        Images is a list of images successfully retrieved by the import of the repository.

        :param images: The images of this V1RepositoryImportStatus.
        :type: list[V1ImageImportStatus]
        """

        self._images = images

    @property
    def additional_tags(self):
        """
        Gets the additional_tags of this V1RepositoryImportStatus.
        AdditionalTags are tags that exist in the repository but were not imported because a maximum limit of automatic imports was applied.

        :return: The additional_tags of this V1RepositoryImportStatus.
        :rtype: list[str]
        """
        return self._additional_tags

    @additional_tags.setter
    def additional_tags(self, additional_tags):
        """
        Sets the additional_tags of this V1RepositoryImportStatus.
        AdditionalTags are tags that exist in the repository but were not imported because a maximum limit of automatic imports was applied.

        :param additional_tags: The additional_tags of this V1RepositoryImportStatus.
        :type: list[str]
        """

        self._additional_tags = additional_tags

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
