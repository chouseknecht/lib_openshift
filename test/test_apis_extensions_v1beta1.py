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

from __future__ import absolute_import

import os
import sys
import unittest

import lib_openshift
from lib_openshift.rest import ApiException
from lib_openshift.apis.apis_extensions_v1beta1 import ApisExtensionsV1beta1


class TestApisExtensionsV1beta1(unittest.TestCase):
    """ ApisExtensionsV1beta1 unit test stubs """

    def setUp(self):
        self.api = lib_openshift.apis.apis_extensions_v1beta1.ApisExtensionsV1beta1()

    def tearDown(self):
        pass

    def test_create_daemonset(self):
        """
        Test case for create_daemonset

        create a DaemonSet
        """
        pass

    def test_create_deployment(self):
        """
        Test case for create_deployment

        create a Deployment
        """
        pass

    def test_create_horizontalpodautoscaler(self):
        """
        Test case for create_horizontalpodautoscaler

        create a HorizontalPodAutoscaler
        """
        pass

    def test_create_ingress(self):
        """
        Test case for create_ingress

        create a Ingress
        """
        pass

    def test_create_job(self):
        """
        Test case for create_job

        create a Job
        """
        pass

    def test_create_namespaced_daemonset(self):
        """
        Test case for create_namespaced_daemonset

        create a DaemonSet
        """
        pass

    def test_create_namespaced_deployment(self):
        """
        Test case for create_namespaced_deployment

        create a Deployment
        """
        pass

    def test_create_namespaced_deployment_rollback(self):
        """
        Test case for create_namespaced_deployment_rollback

        create rollback of a DeploymentRollback
        """
        pass

    def test_create_namespaced_horizontalpodautoscaler(self):
        """
        Test case for create_namespaced_horizontalpodautoscaler

        create a HorizontalPodAutoscaler
        """
        pass

    def test_create_namespaced_ingress(self):
        """
        Test case for create_namespaced_ingress

        create a Ingress
        """
        pass

    def test_create_namespaced_job(self):
        """
        Test case for create_namespaced_job

        create a Job
        """
        pass

    def test_create_namespaced_replicaset(self):
        """
        Test case for create_namespaced_replicaset

        create a ReplicaSet
        """
        pass

    def test_create_replicaset(self):
        """
        Test case for create_replicaset

        create a ReplicaSet
        """
        pass

    def test_delete_namespaced_daemonset(self):
        """
        Test case for delete_namespaced_daemonset

        delete a DaemonSet
        """
        pass

    def test_delete_namespaced_daemonsets(self):
        """
        Test case for delete_namespaced_daemonsets

        delete collection of DaemonSet
        """
        pass

    def test_delete_namespaced_deployment(self):
        """
        Test case for delete_namespaced_deployment

        delete a Deployment
        """
        pass

    def test_delete_namespaced_deployments(self):
        """
        Test case for delete_namespaced_deployments

        delete collection of Deployment
        """
        pass

    def test_delete_namespaced_horizontalpodautoscaler(self):
        """
        Test case for delete_namespaced_horizontalpodautoscaler

        delete a HorizontalPodAutoscaler
        """
        pass

    def test_delete_namespaced_horizontalpodautoscalers(self):
        """
        Test case for delete_namespaced_horizontalpodautoscalers

        delete collection of HorizontalPodAutoscaler
        """
        pass

    def test_delete_namespaced_ingress(self):
        """
        Test case for delete_namespaced_ingress

        delete a Ingress
        """
        pass

    def test_delete_namespaced_ingresses(self):
        """
        Test case for delete_namespaced_ingresses

        delete collection of Ingress
        """
        pass

    def test_delete_namespaced_job(self):
        """
        Test case for delete_namespaced_job

        delete a Job
        """
        pass

    def test_delete_namespaced_jobs(self):
        """
        Test case for delete_namespaced_jobs

        delete collection of Job
        """
        pass

    def test_delete_namespaced_replicaset(self):
        """
        Test case for delete_namespaced_replicaset

        delete a ReplicaSet
        """
        pass

    def test_delete_namespaced_replicasets(self):
        """
        Test case for delete_namespaced_replicasets

        delete collection of ReplicaSet
        """
        pass

    def test_get_namespaced_daemonset(self):
        """
        Test case for get_namespaced_daemonset

        read the specified DaemonSet
        """
        pass

    def test_get_namespaced_deployment(self):
        """
        Test case for get_namespaced_deployment

        read the specified Deployment
        """
        pass

    def test_get_namespaced_deployment_scale(self):
        """
        Test case for get_namespaced_deployment_scale

        read scale of the specified Scale
        """
        pass

    def test_get_namespaced_horizontalpodautoscaler(self):
        """
        Test case for get_namespaced_horizontalpodautoscaler

        read the specified HorizontalPodAutoscaler
        """
        pass

    def test_get_namespaced_ingress(self):
        """
        Test case for get_namespaced_ingress

        read the specified Ingress
        """
        pass

    def test_get_namespaced_job(self):
        """
        Test case for get_namespaced_job

        read the specified Job
        """
        pass

    def test_get_namespaced_replicaset(self):
        """
        Test case for get_namespaced_replicaset

        read the specified ReplicaSet
        """
        pass

    def test_get_namespaced_replicaset_scale(self):
        """
        Test case for get_namespaced_replicaset_scale

        read scale of the specified Scale
        """
        pass

    def test_get_namespaced_replicationcontroller_scale(self):
        """
        Test case for get_namespaced_replicationcontroller_scale

        read scale of the specified Scale
        """
        pass

    def test_list(self):
        """
        Test case for list

        get available resources
        """
        pass

    def test_list_daemonsets(self):
        """
        Test case for list_daemonsets

        list or watch objects of kind DaemonSet
        """
        pass

    def test_list_deployments(self):
        """
        Test case for list_deployments

        list or watch objects of kind Deployment
        """
        pass

    def test_list_horizontalpodautoscalers(self):
        """
        Test case for list_horizontalpodautoscalers

        list or watch objects of kind HorizontalPodAutoscaler
        """
        pass

    def test_list_ingresses(self):
        """
        Test case for list_ingresses

        list or watch objects of kind Ingress
        """
        pass

    def test_list_jobs(self):
        """
        Test case for list_jobs

        list or watch objects of kind Job
        """
        pass

    def test_list_namespaced_daemonsets(self):
        """
        Test case for list_namespaced_daemonsets

        list or watch objects of kind DaemonSet
        """
        pass

    def test_list_namespaced_deployments(self):
        """
        Test case for list_namespaced_deployments

        list or watch objects of kind Deployment
        """
        pass

    def test_list_namespaced_horizontalpodautoscalers(self):
        """
        Test case for list_namespaced_horizontalpodautoscalers

        list or watch objects of kind HorizontalPodAutoscaler
        """
        pass

    def test_list_namespaced_ingresses(self):
        """
        Test case for list_namespaced_ingresses

        list or watch objects of kind Ingress
        """
        pass

    def test_list_namespaced_jobs(self):
        """
        Test case for list_namespaced_jobs

        list or watch objects of kind Job
        """
        pass

    def test_list_namespaced_replicasets(self):
        """
        Test case for list_namespaced_replicasets

        list or watch objects of kind ReplicaSet
        """
        pass

    def test_list_replicasets(self):
        """
        Test case for list_replicasets

        list or watch objects of kind ReplicaSet
        """
        pass

    def test_patch_namespaced_daemonset(self):
        """
        Test case for patch_namespaced_daemonset

        partially update the specified DaemonSet
        """
        pass

    def test_patch_namespaced_deployment(self):
        """
        Test case for patch_namespaced_deployment

        partially update the specified Deployment
        """
        pass

    def test_patch_namespaced_deployment_scale(self):
        """
        Test case for patch_namespaced_deployment_scale

        partially update scale of the specified Scale
        """
        pass

    def test_patch_namespaced_horizontalpodautoscaler(self):
        """
        Test case for patch_namespaced_horizontalpodautoscaler

        partially update the specified HorizontalPodAutoscaler
        """
        pass

    def test_patch_namespaced_ingress(self):
        """
        Test case for patch_namespaced_ingress

        partially update the specified Ingress
        """
        pass

    def test_patch_namespaced_job(self):
        """
        Test case for patch_namespaced_job

        partially update the specified Job
        """
        pass

    def test_patch_namespaced_replicaset(self):
        """
        Test case for patch_namespaced_replicaset

        partially update the specified ReplicaSet
        """
        pass

    def test_patch_namespaced_replicaset_scale(self):
        """
        Test case for patch_namespaced_replicaset_scale

        partially update scale of the specified Scale
        """
        pass

    def test_patch_namespaced_replicationcontroller_scale(self):
        """
        Test case for patch_namespaced_replicationcontroller_scale

        partially update scale of the specified Scale
        """
        pass

    def test_replace_namespaced_daemonset(self):
        """
        Test case for replace_namespaced_daemonset

        replace the specified DaemonSet
        """
        pass

    def test_replace_namespaced_daemonset_status(self):
        """
        Test case for replace_namespaced_daemonset_status

        replace status of the specified DaemonSet
        """
        pass

    def test_replace_namespaced_deployment(self):
        """
        Test case for replace_namespaced_deployment

        replace the specified Deployment
        """
        pass

    def test_replace_namespaced_deployment_scale(self):
        """
        Test case for replace_namespaced_deployment_scale

        replace scale of the specified Scale
        """
        pass

    def test_replace_namespaced_deployment_status(self):
        """
        Test case for replace_namespaced_deployment_status

        replace status of the specified Deployment
        """
        pass

    def test_replace_namespaced_horizontalpodautoscaler(self):
        """
        Test case for replace_namespaced_horizontalpodautoscaler

        replace the specified HorizontalPodAutoscaler
        """
        pass

    def test_replace_namespaced_horizontalpodautoscaler_status(self):
        """
        Test case for replace_namespaced_horizontalpodautoscaler_status

        replace status of the specified HorizontalPodAutoscaler
        """
        pass

    def test_replace_namespaced_ingress(self):
        """
        Test case for replace_namespaced_ingress

        replace the specified Ingress
        """
        pass

    def test_replace_namespaced_ingress_status(self):
        """
        Test case for replace_namespaced_ingress_status

        replace status of the specified Ingress
        """
        pass

    def test_replace_namespaced_job(self):
        """
        Test case for replace_namespaced_job

        replace the specified Job
        """
        pass

    def test_replace_namespaced_job_status(self):
        """
        Test case for replace_namespaced_job_status

        replace status of the specified Job
        """
        pass

    def test_replace_namespaced_replicaset(self):
        """
        Test case for replace_namespaced_replicaset

        replace the specified ReplicaSet
        """
        pass

    def test_replace_namespaced_replicaset_scale(self):
        """
        Test case for replace_namespaced_replicaset_scale

        replace scale of the specified Scale
        """
        pass

    def test_replace_namespaced_replicaset_status(self):
        """
        Test case for replace_namespaced_replicaset_status

        replace status of the specified ReplicaSet
        """
        pass

    def test_replace_namespaced_replicationcontroller_scale(self):
        """
        Test case for replace_namespaced_replicationcontroller_scale

        replace scale of the specified Scale
        """
        pass

    def test_watch_namespaced_watch_daemonset(self):
        """
        Test case for watch_namespaced_watch_daemonset

        watch changes to an object of kind DaemonSet
        """
        pass

    def test_watch_namespaced_watch_daemonsets(self):
        """
        Test case for watch_namespaced_watch_daemonsets

        watch individual changes to a list of DaemonSet
        """
        pass

    def test_watch_namespaced_watch_deployment(self):
        """
        Test case for watch_namespaced_watch_deployment

        watch changes to an object of kind Deployment
        """
        pass

    def test_watch_namespaced_watch_deployments(self):
        """
        Test case for watch_namespaced_watch_deployments

        watch individual changes to a list of Deployment
        """
        pass

    def test_watch_namespaced_watch_horizontalpodautoscaler(self):
        """
        Test case for watch_namespaced_watch_horizontalpodautoscaler

        watch changes to an object of kind HorizontalPodAutoscaler
        """
        pass

    def test_watch_namespaced_watch_horizontalpodautoscalers(self):
        """
        Test case for watch_namespaced_watch_horizontalpodautoscalers

        watch individual changes to a list of HorizontalPodAutoscaler
        """
        pass

    def test_watch_namespaced_watch_ingress(self):
        """
        Test case for watch_namespaced_watch_ingress

        watch changes to an object of kind Ingress
        """
        pass

    def test_watch_namespaced_watch_ingresses(self):
        """
        Test case for watch_namespaced_watch_ingresses

        watch individual changes to a list of Ingress
        """
        pass

    def test_watch_namespaced_watch_job(self):
        """
        Test case for watch_namespaced_watch_job

        watch changes to an object of kind Job
        """
        pass

    def test_watch_namespaced_watch_jobs(self):
        """
        Test case for watch_namespaced_watch_jobs

        watch individual changes to a list of Job
        """
        pass

    def test_watch_namespaced_watch_replicaset(self):
        """
        Test case for watch_namespaced_watch_replicaset

        watch changes to an object of kind ReplicaSet
        """
        pass

    def test_watch_namespaced_watch_replicasets(self):
        """
        Test case for watch_namespaced_watch_replicasets

        watch individual changes to a list of ReplicaSet
        """
        pass

    def test_watch_watch_daemonsets(self):
        """
        Test case for watch_watch_daemonsets

        watch individual changes to a list of DaemonSet
        """
        pass

    def test_watch_watch_deployments(self):
        """
        Test case for watch_watch_deployments

        watch individual changes to a list of Deployment
        """
        pass

    def test_watch_watch_horizontalpodautoscalers(self):
        """
        Test case for watch_watch_horizontalpodautoscalers

        watch individual changes to a list of HorizontalPodAutoscaler
        """
        pass

    def test_watch_watch_ingresses(self):
        """
        Test case for watch_watch_ingresses

        watch individual changes to a list of Ingress
        """
        pass

    def test_watch_watch_jobs(self):
        """
        Test case for watch_watch_jobs

        watch individual changes to a list of Job
        """
        pass

    def test_watch_watch_replicasets(self):
        """
        Test case for watch_watch_replicasets

        watch individual changes to a list of ReplicaSet
        """
        pass


if __name__ == '__main__':
    unittest.main()
