# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class DeploymentMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the type of ARM deployment to be performed on the resource.
    """

    INCREMENTAL = "Incremental"
    COMPLETE = "Complete"

class RestAuthLocation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The location of the authentication key/value pair in the request.
    """

    QUERY = "Query"
    HEADER = "Header"

class RestAuthType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type.
    """

    API_KEY = "ApiKey"
    ROLLOUT_IDENTITY = "RolloutIdentity"

class RestMatchQuantifier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether any or all of the expressions should match with the response content.
    """

    ALL = "All"
    ANY = "Any"

class RestRequestMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The HTTP method to use for the request.
    """

    GET = "GET"
    POST = "POST"

class StepType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of step.
    """

    WAIT = "Wait"
    HEALTH_CHECK = "HealthCheck"
