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


class V1CustomBuildStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]


    def __init__(self, _from=None, pull_secret=None, env=None, expose_docker_socket=None, force_pull=None, secrets=None, build_api_version=None):
        """
        V1CustomBuildStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'V1ObjectReference',
            'pull_secret': 'V1LocalObjectReference',
            'env': 'list[V1EnvVar]',
            'expose_docker_socket': 'bool',
            'force_pull': 'bool',
            'secrets': 'list[V1SecretSpec]',
            'build_api_version': 'str'
        }

        self.attribute_map = {
            '_from': 'from',
            'pull_secret': 'pullSecret',
            'env': 'env',
            'expose_docker_socket': 'exposeDockerSocket',
            'force_pull': 'forcePull',
            'secrets': 'secrets',
            'build_api_version': 'buildAPIVersion'
        }

        self.__from = _from
        self._pull_secret = pull_secret
        self._env = env
        self._expose_docker_socket = expose_docker_socket
        self._force_pull = force_pull
        self._secrets = secrets
        self._build_api_version = build_api_version

    @property
    def _from(self):
        """
        Gets the _from of this V1CustomBuildStrategy.
        From is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled

        :return: The _from of this V1CustomBuildStrategy.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1CustomBuildStrategy.
        From is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled

        :param _from: The _from of this V1CustomBuildStrategy.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def pull_secret(self):
        """
        Gets the pull_secret of this V1CustomBuildStrategy.
        PullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :return: The pull_secret of this V1CustomBuildStrategy.
        :rtype: V1LocalObjectReference
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """
        Sets the pull_secret of this V1CustomBuildStrategy.
        PullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :param pull_secret: The pull_secret of this V1CustomBuildStrategy.
        :type: V1LocalObjectReference
        """

        self._pull_secret = pull_secret

    @property
    def env(self):
        """
        Gets the env of this V1CustomBuildStrategy.
        Env contains additional environment variables you want to pass into a builder container

        :return: The env of this V1CustomBuildStrategy.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1CustomBuildStrategy.
        Env contains additional environment variables you want to pass into a builder container

        :param env: The env of this V1CustomBuildStrategy.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def expose_docker_socket(self):
        """
        Gets the expose_docker_socket of this V1CustomBuildStrategy.
        ExposeDockerSocket will allow running Docker commands (and build Docker images) from inside the Docker container.

        :return: The expose_docker_socket of this V1CustomBuildStrategy.
        :rtype: bool
        """
        return self._expose_docker_socket

    @expose_docker_socket.setter
    def expose_docker_socket(self, expose_docker_socket):
        """
        Sets the expose_docker_socket of this V1CustomBuildStrategy.
        ExposeDockerSocket will allow running Docker commands (and build Docker images) from inside the Docker container.

        :param expose_docker_socket: The expose_docker_socket of this V1CustomBuildStrategy.
        :type: bool
        """

        self._expose_docker_socket = expose_docker_socket

    @property
    def force_pull(self):
        """
        Gets the force_pull of this V1CustomBuildStrategy.
        ForcePull describes if the controller should configure the build pod to always pull the images for the builder or only pull if it is not present locally

        :return: The force_pull of this V1CustomBuildStrategy.
        :rtype: bool
        """
        return self._force_pull

    @force_pull.setter
    def force_pull(self, force_pull):
        """
        Sets the force_pull of this V1CustomBuildStrategy.
        ForcePull describes if the controller should configure the build pod to always pull the images for the builder or only pull if it is not present locally

        :param force_pull: The force_pull of this V1CustomBuildStrategy.
        :type: bool
        """

        self._force_pull = force_pull

    @property
    def secrets(self):
        """
        Gets the secrets of this V1CustomBuildStrategy.
        Secrets is a list of additional secrets that will be included in the build pod

        :return: The secrets of this V1CustomBuildStrategy.
        :rtype: list[V1SecretSpec]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """
        Sets the secrets of this V1CustomBuildStrategy.
        Secrets is a list of additional secrets that will be included in the build pod

        :param secrets: The secrets of this V1CustomBuildStrategy.
        :type: list[V1SecretSpec]
        """

        self._secrets = secrets

    @property
    def build_api_version(self):
        """
        Gets the build_api_version of this V1CustomBuildStrategy.
        BuildAPIVersion is the requested API version for the Build object serialized and passed to the custom builder

        :return: The build_api_version of this V1CustomBuildStrategy.
        :rtype: str
        """
        return self._build_api_version

    @build_api_version.setter
    def build_api_version(self, build_api_version):
        """
        Sets the build_api_version of this V1CustomBuildStrategy.
        BuildAPIVersion is the requested API version for the Build object serialized and passed to the custom builder

        :param build_api_version: The build_api_version of this V1CustomBuildStrategy.
        :type: str
        """

        self._build_api_version = build_api_version

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
