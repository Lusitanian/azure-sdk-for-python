# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterHealthPolicies(Model):
    """Health policies to evaluate cluster health.

    :param application_health_policy_map:
    :type application_health_policy_map: list of
     :class:`ApplicationHealthPolicyMapItem
     <azure.servicefabric.models.ApplicationHealthPolicyMapItem>`
    :param cluster_health_policy:
    :type cluster_health_policy: :class:`ClusterHealthPolicy
     <azure.servicefabric.models.ClusterHealthPolicy>`
    """ 

    _attribute_map = {
        'application_health_policy_map': {'key': 'ApplicationHealthPolicyMap', 'type': '[ApplicationHealthPolicyMapItem]'},
        'cluster_health_policy': {'key': 'ClusterHealthPolicy', 'type': 'ClusterHealthPolicy'},
    }

    def __init__(self, application_health_policy_map=None, cluster_health_policy=None):
        self.application_health_policy_map = application_health_policy_map
        self.cluster_health_policy = cluster_health_policy