from __future__ import absolute_import
import os
import yaml
import json


class WrapperException(Exception):

    def __init__(self, msg, **kwargs):
        self.msg = msg
        self.value = kwargs
        self.value['msg'] = msg

    def __str__(self):
        return json.dumps(self.value)


class Wrapper(object):

    def namespace(self, name=None, api_version='v1', labels=None,
                  annotations=None, state='present'):

        result = {'changed': False}

        if name is None:
            raise WrapperException(msg="name is required")

        if state not in ('present', 'absent'):
            raise WrapperException(msg="Unknown state: {0}".format(state))

        if labels is not None and not is_instance(dict, labels):
            raise WrapperException(msg="labels must be a dict")

        if annotations is not None and not is_instance(dict, annotations):
            raise WrapperException(msg="annotations must be a dict")

        if api_version == 'v1':
            from .models import V1Namespace
            model = V1Namespace

            from .apis import ApiV1
            api = ApiV1
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        # TODO: allow for setting api_client param to override config
#        api_object = api()
#        operations = model.operations
#        create_method = getattr(api_object, operations['crud']['create'])
#        read_method = getattr(api_object, operations['crud']['read'])
#        update_method = getattr(api_object, operations['crud']['update'])
#        delete_method = getattr(api_object, operations['crud']['delete'])
#
#        current_namespace = read_method(name)
#        # TODO: validate that it exists somehow
        already_exists = False

        if state == 'present':
            if already_exists:
                pass
                # TODO: compare and update if needed
            else:
                pass
                # TODO: create
                #metadata = v1ObjectMeta(...)
                #namespace_spec = v1NamespaceSpec(...)
                #namespace = V1Namespace(kind='namespace',
                #                        api_version=api_version,
                #                        metadata=metadata,
                #                        spec=namespace_spec,
                #                        status=V1NamespaceStatus())

        elif state == 'absent' and already_exists:
            pass
            # TODO: delete
            #delete_options = V1DeleteOptions()
            #status = delete_method(delete_options, name)
            # TODO: return data based on status

        return result



    def __init__(self, kubeconfig=None, api_endpoint=None, namespace=None,
                 username=None, password=None, token=None, client_cert=None,
                 client_key=None, certificate_authority=None,
                 certificate_authority_data = None,
                 insecure_skip_tls_verify=None):

        client_config = None

        try:
            if kubeconfig is None:
                kubeconfig = '~/.kube/config'
            client_config = yaml.load(open(os.path.expanduser(kubeconfig), 'r'))
        except IOError:
            # eat IOError, since we are only trying to read in the file if
            # it doesn't exist
            pass
        except yaml.YAMLError:
            raise WrapperException(msg="Could not parse kubeconfig: {0}".format(kubeconfig))

        config_curr_context = None
        if client_config is not None:
            config_curr_context = client_config.get('current-context')

        config_context = None
        config_cluster_name = None
        config_user_name = None
        if config_curr_context is not None:
            for entry in client_config.get('contexts'):
                if entry.get('name') == config_curr_context:
                    config_context = entry.get('context')
                    config_cluster_name = config_context.get('cluster')
                    config_user_name = config_context.get('user')

                    if namespace is None:
                        namespace = config_context.get('namespace')

        config_cluster = None
        if config_cluster_name is not None:
            for entry in client_config.get('clusters'):
                if entry.get('name') == config_cluster_name:
                    config_cluster = entry.get('cluster')
                    if api_endpoint is None:
                        api_endpoint = config_cluster.get('server')
                        if 'certificate-authority' in config_cluster:
                            certificate_authority = config_cluster.get('certificate-authority')
                        if 'certificate-authority-data' in config_cluster:
                            certificate_authority_data = config_cluster.get('certificate-authority-data')
                        if 'insecure-skip-tls-verify' in config_cluster:
                            insecure_skip_tls_verify = config_cluster.get('insecure-skip-tls-verify')

        config_user = None
        if config_user_name is not None:
            for entry in client_config.get('users'):
                if entry.get('name') == config_user_name:
                    config_user = entry.get('user')

        if username is not None and password is None:
            raise WrapperException(msg="username requires password")

        if password is not None and username is None:
            raise WrapperException(msg="password requires username")

        if username is not None and token is not None:
            raise WrapperException(msg="username and token are mutally exclusive")

        if password is not None and token is not None:
            raise WrapperException(msg="password and token are mutally exclusive")

        if username is not None and (client_cert is not None or client_key is not None):
            raise WrapperException(msg="username and client_cert/client_key are mutally exclusive")

        if password is not None and (client_cert is not None or client_key is not None):
            raise WrapperException(msg="password and client_cert/client_key are mutally exclusive")

        if token is not None and (client_cert is not None or client_key is not None):
            raise WrapperException(msg="token and client_cert/client_key are mutally exclusive")

        if client_cert is not None and client_key is None:
            raise WrapperException(msg="client_cert requires client_key")

        if client_key is not None and client_cert is None:
            raise WrapperException(msg="client_key requires client_cert")

        if config_user is not None and username is None and token is None and client_cert is None:
            username = config_user.get('username')
            password = config_user.get('password')
            token = config_user.get('token')
            client_cert = config_user.get('client-certificate')
            client_key = config_user.get('client-key')

        if api_endpoint is None:
            raise WrapperException(msg="api_endpoint is required when a kubeconfig is not provided")

        self._cluster = {'server': api_endpoint,
                         'certificate_authority': certificate_authority,
                         'certificate_authority_data': certificate_authority_data,
                         'insecure_skip_tls_verify': insecure_skip_tls_verify}
        self._user = {'username': username, 'password': password, 'token':
                      token, 'client_cert': client_cert, 'client_key': client_key}
        self._namespace = namespace