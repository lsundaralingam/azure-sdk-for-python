# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CommunicationError
    from ._models_py3 import CommunicationErrorResponse
    from ._models_py3 import CommunicationIdentity
    from ._models_py3 import CommunicationIdentityAccessTokenRequest
    from ._models_py3 import CommunicationIdentityAccessTokenResult
    from ._models_py3 import CommunicationIdentityCreateRequest
    from ._models_py3 import CommunicationUserToken
except (SyntaxError, ImportError):
    from ._models import CommunicationError  # type: ignore
    from ._models import CommunicationErrorResponse  # type: ignore
    from ._models import CommunicationIdentity  # type: ignore
    from ._models import CommunicationIdentityAccessTokenRequest  # type: ignore
    from ._models import CommunicationIdentityAccessTokenResult  # type: ignore
    from ._models import CommunicationIdentityCreateRequest  # type: ignore
    from ._models import CommunicationUserToken  # type: ignore

from ._communication_identity_client_enums import (
    CommunicationTokenScope,
)

__all__ = [
    'CommunicationError',
    'CommunicationErrorResponse',
    'CommunicationIdentity',
    'CommunicationIdentityAccessTokenRequest',
    'CommunicationIdentityAccessTokenResult',
    'CommunicationIdentityCreateRequest',
    'CommunicationUserToken',
    'CommunicationTokenScope',
]
