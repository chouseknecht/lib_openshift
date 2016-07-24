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


class V1GitSourceRevision(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, commit=None, author=None, committer=None, message=None):
        """
        V1GitSourceRevision - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'commit': 'str',
            'author': 'V1SourceControlUser',
            'committer': 'V1SourceControlUser',
            'message': 'str'
        }

        self.attribute_map = {
            'commit': 'commit',
            'author': 'author',
            'committer': 'committer',
            'message': 'message'
        }

        self._commit = commit
        self._author = author
        self._committer = committer
        self._message = message

    @property
    def commit(self):
        """
        Gets the commit of this V1GitSourceRevision.
        Commit is the commit hash identifying a specific commit

        :return: The commit of this V1GitSourceRevision.
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """
        Sets the commit of this V1GitSourceRevision.
        Commit is the commit hash identifying a specific commit

        :param commit: The commit of this V1GitSourceRevision.
        :type: str
        """

        self._commit = commit

    @property
    def author(self):
        """
        Gets the author of this V1GitSourceRevision.
        Author is the author of a specific commit

        :return: The author of this V1GitSourceRevision.
        :rtype: V1SourceControlUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this V1GitSourceRevision.
        Author is the author of a specific commit

        :param author: The author of this V1GitSourceRevision.
        :type: V1SourceControlUser
        """

        self._author = author

    @property
    def committer(self):
        """
        Gets the committer of this V1GitSourceRevision.
        Committer is the committer of a specific commit

        :return: The committer of this V1GitSourceRevision.
        :rtype: V1SourceControlUser
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """
        Sets the committer of this V1GitSourceRevision.
        Committer is the committer of a specific commit

        :param committer: The committer of this V1GitSourceRevision.
        :type: V1SourceControlUser
        """

        self._committer = committer

    @property
    def message(self):
        """
        Gets the message of this V1GitSourceRevision.
        Message is the description of a specific commit

        :return: The message of this V1GitSourceRevision.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1GitSourceRevision.
        Message is the description of a specific commit

        :param message: The message of this V1GitSourceRevision.
        :type: str
        """

        self._message = message

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