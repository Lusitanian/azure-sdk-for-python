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


class ContentLink(Model):
    """Definition of the content link.

    :param uri: Gets or sets the uri of the runbook content.
    :type uri: str
    :param content_hash: Gets or sets the hash.
    :type content_hash: ~azure.mgmt.automation.models.ContentHash
    :param version: Gets or sets the version of the content.
    :type version: str
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'content_hash': {'key': 'contentHash', 'type': 'ContentHash'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, uri=None, content_hash=None, version=None):
        super(ContentLink, self).__init__()
        self.uri = uri
        self.content_hash = content_hash
        self.version = version
