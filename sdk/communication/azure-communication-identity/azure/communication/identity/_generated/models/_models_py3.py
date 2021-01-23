# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CommunicationError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code.
    :type code: str
    :param message: Required. The error message.
    :type message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.identity.models.CommunicationError]
    :param inner_error: The Communication Services error.
    :type inner_error: ~azure.communication.identity.models.CommunicationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CommunicationError]'},
        'inner_error': {'key': 'innerError', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        inner_error: Optional["CommunicationError"] = None,
        **kwargs
    ):
        super(CommunicationError, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = None
        self.details = None
        self.inner_error = inner_error


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. The Communication Services error.
    :type error: ~azure.communication.identity.models.CommunicationError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        error: "CommunicationError",
        **kwargs
    ):
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = error


class CommunicationIdentity(msrest.serialization.Model):
    """A communication identity.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Identifier of the identity.
    :type id: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: str,
        **kwargs
    ):
        super(CommunicationIdentity, self).__init__(**kwargs)
        self.id = id


class CommunicationIdentityAccessTokenRequest(msrest.serialization.Model):
    """CommunicationIdentityAccessTokenRequest.

    All required parameters must be populated in order to send to Azure.

    :param scopes: Required. List of scopes attached to the token.
    :type scopes: list[str or ~azure.communication.identity.models.CommunicationTokenScope]
    """

    _validation = {
        'scopes': {'required': True},
    }

    _attribute_map = {
        'scopes': {'key': 'scopes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        scopes: List[Union[str, "CommunicationTokenScope"]],
        **kwargs
    ):
        super(CommunicationIdentityAccessTokenRequest, self).__init__(**kwargs)
        self.scopes = scopes


class CommunicationIdentityAccessTokenResult(msrest.serialization.Model):
    """A communication identity with access token.

    All required parameters must be populated in order to send to Azure.

    :param identity: Required. A communication identity.
    :type identity: ~azure.communication.identity.models.CommunicationIdentity
    :param access_token: An access token.
    :type access_token: ~azure.communication.identity.models.CommunicationUserToken
    """

    _validation = {
        'identity': {'required': True},
    }

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'CommunicationIdentity'},
        'access_token': {'key': 'accessToken', 'type': 'CommunicationUserToken'},
    }

    def __init__(
        self,
        *,
        identity: "CommunicationIdentity",
        access_token: Optional["CommunicationUserToken"] = None,
        **kwargs
    ):
        super(CommunicationIdentityAccessTokenResult, self).__init__(**kwargs)
        self.identity = identity
        self.access_token = access_token


class CommunicationIdentityCreateRequest(msrest.serialization.Model):
    """CommunicationIdentityCreateRequest.

    :param create_token_with_scopes: Also create access token for the created identity.
    :type create_token_with_scopes: list[str or
     ~azure.communication.identity.models.CommunicationTokenScope]
    """

    _attribute_map = {
        'create_token_with_scopes': {'key': 'createTokenWithScopes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        create_token_with_scopes: Optional[List[Union[str, "CommunicationTokenScope"]]] = None,
        **kwargs
    ):
        super(CommunicationIdentityCreateRequest, self).__init__(**kwargs)
        self.create_token_with_scopes = create_token_with_scopes


class CommunicationUserToken(msrest.serialization.Model):
    """An access token.

    All required parameters must be populated in order to send to Azure.

    :param token: Required. The access token issued for the identity.
    :type token: str
    :param expires_on: Required. The expiry time of the token.
    :type expires_on: ~datetime.datetime
    """

    _validation = {
        'token': {'required': True},
        'expires_on': {'required': True},
    }

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'expires_on': {'key': 'expiresOn', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        token: str,
        expires_on: datetime.datetime,
        **kwargs
    ):
        super(CommunicationUserToken, self).__init__(**kwargs)
        self.token = token
        self.expires_on = expires_on
