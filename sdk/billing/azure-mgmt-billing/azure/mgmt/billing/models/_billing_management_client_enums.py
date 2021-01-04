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


class AcceptanceMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode of acceptance for an agreement.
    """

    CLICK_TO_ACCEPT = "ClickToAccept"
    E_SIGN_EMBEDDED = "ESignEmbedded"
    E_SIGN_OFFLINE = "ESignOffline"

class AccountStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the billing account.
    """

    ACTIVE = "Active"
    DELETED = "Deleted"
    DISABLED = "Disabled"
    EXPIRED = "Expired"
    TRANSFERRED = "Transferred"
    EXTENDED = "Extended"
    TERMINATED = "Terminated"

class AccountType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of customer.
    """

    ENTERPRISE = "Enterprise"
    INDIVIDUAL = "Individual"
    PARTNER = "Partner"

class AddressValidationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the address validation.
    """

    VALID = "Valid"
    INVALID = "Invalid"

class AgreementType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of agreement.
    """

    MICROSOFT_CUSTOMER_AGREEMENT = "MicrosoftCustomerAgreement"
    ENTERPRISE_AGREEMENT = "EnterpriseAgreement"
    MICROSOFT_ONLINE_SERVICES_PROGRAM = "MicrosoftOnlineServicesProgram"
    MICROSOFT_PARTNER_AGREEMENT = "MicrosoftPartnerAgreement"

class AutoRenew(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether auto renewal is turned on or off for a product.
    """

    OFF = "Off"
    ON = "On"

class BillingFrequency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The frequency at which the product will be billed.
    """

    ONE_TIME = "OneTime"
    MONTHLY = "Monthly"
    USAGE_BASED = "UsageBased"

class BillingProfileSpendingLimit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The billing profile spending limit.
    """

    OFF = "Off"
    ON = "On"

class BillingProfileStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the billing profile.
    """

    ACTIVE = "Active"
    DISABLED = "Disabled"
    WARNED = "Warned"

class BillingProfileStatusReasonCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Reason for the specified billing profile status.
    """

    PAST_DUE = "PastDue"
    SPENDING_LIMIT_REACHED = "SpendingLimitReached"
    SPENDING_LIMIT_EXPIRED = "SpendingLimitExpired"

class BillingRelationshipType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Identifies which services and purchases are paid by a billing profile.
    """

    DIRECT = "Direct"
    INDIRECT_CUSTOMER = "IndirectCustomer"
    INDIRECT_PARTNER = "IndirectPartner"
    CSP_PARTNER = "CSPPartner"

class BillingSubscriptionStatusType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current billing status of the subscription.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    ABANDONED = "Abandoned"
    DELETED = "Deleted"
    WARNING = "Warning"

class Category(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The category of the agreement signed by a customer.
    """

    MICROSOFT_CUSTOMER_AGREEMENT = "MicrosoftCustomerAgreement"
    AFFILIATE_PURCHASE_TERMS = "AffiliatePurchaseTerms"
    OTHER = "Other"

class DocumentSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The source of the document. ENF for Brazil and DRS for rest of the world.
    """

    DRS = "DRS"
    ENF = "ENF"

class DocumentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the document.
    """

    INVOICE = "Invoice"
    VOID_NOTE = "VoidNote"
    TAX_RECEIPT = "TaxReceipt"
    CREDIT_NOTE = "CreditNote"

class InvoiceDocumentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the document.
    """

    INVOICE = "Invoice"
    CREDIT_NOTE = "CreditNote"

class InvoiceSectionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Identifies the state of an invoice section.
    """

    ACTIVE = "Active"
    RESTRICTED = "Restricted"

class InvoiceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the invoice.
    """

    DUE = "Due"
    OVER_DUE = "OverDue"
    PAID = "Paid"
    VOID = "Void"

class InvoiceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Invoice type.
    """

    AZURE_SERVICE = "AzureService"
    AZURE_MARKETPLACE = "AzureMarketplace"
    AZURE_SUPPORT = "AzureSupport"

class MarketplacePurchasesPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The policy that controls whether Azure marketplace purchases are allowed for a billing profile.
    """

    ALL_ALLOWED = "AllAllowed"
    ONLY_FREE_ALLOWED = "OnlyFreeAllowed"
    NOT_ALLOWED = "NotAllowed"

class PaymentMethodFamily(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The family of payment method.
    """

    CREDITS = "Credits"
    CHECK_WIRE = "CheckWire"
    CREDIT_CARD = "CreditCard"
    NONE = "None"

class ProductStatusType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the product.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    PAST_DUE = "PastDue"
    EXPIRING = "Expiring"
    EXPIRED = "Expired"
    DISABLED = "Disabled"
    CANCELLED = "Cancelled"
    AUTO_RENEW = "AutoRenew"

class ProductTransferValidationErrorCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Error code of the transfer validation response.
    """

    INVALID_SOURCE = "InvalidSource"
    PRODUCT_NOT_ACTIVE = "ProductNotActive"
    INSUFFICIENT_PERMISSION_ON_SOURCE = "InsufficientPermissionOnSource"
    INSUFFICIENT_PERMISSION_ON_DESTINATION = "InsufficientPermissionOnDestination"
    DESTINATION_BILLING_PROFILE_PAST_DUE = "DestinationBillingProfilePastDue"
    PRODUCT_TYPE_NOT_SUPPORTED = "ProductTypeNotSupported"
    CROSS_BILLING_ACCOUNT_NOT_ALLOWED = "CrossBillingAccountNotAllowed"
    NOT_AVAILABLE_FOR_DESTINATION_MARKET = "NotAvailableForDestinationMarket"
    ONE_TIME_PURCHASE_PRODUCT_TRANSFER_NOT_ALLOWED = "OneTimePurchaseProductTransferNotAllowed"

class ReservationPurchasesPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The policy that controls whether Azure reservation purchases are allowed for a billing profile.
    """

    ALLOWED = "Allowed"
    NOT_ALLOWED = "NotAllowed"

class ReservationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of transaction.
    """

    PURCHASE = "Purchase"
    USAGE_CHARGE = "Usage Charge"

class SpendingLimit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The billing profile spending limit.
    """

    OFF = "Off"
    ON = "On"

class SpendingLimitForBillingProfile(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The billing profile spending limit.
    """

    OFF = "Off"
    ON = "On"

class StatusReasonCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Reason for the specified billing profile status.
    """

    PAST_DUE = "PastDue"
    SPENDING_LIMIT_REACHED = "SpendingLimitReached"
    SPENDING_LIMIT_EXPIRED = "SpendingLimitExpired"

class StatusReasonCodeForBillingProfile(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Reason for the specified billing profile status.
    """

    PAST_DUE = "PastDue"
    SPENDING_LIMIT_REACHED = "SpendingLimitReached"
    SPENDING_LIMIT_EXPIRED = "SpendingLimitExpired"

class SubscriptionTransferValidationErrorCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Error code of the transfer validation response.
    """

    INVALID_SOURCE = "InvalidSource"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"
    INSUFFICIENT_PERMISSION_ON_SOURCE = "InsufficientPermissionOnSource"
    INSUFFICIENT_PERMISSION_ON_DESTINATION = "InsufficientPermissionOnDestination"
    DESTINATION_BILLING_PROFILE_PAST_DUE = "DestinationBillingProfilePastDue"
    SUBSCRIPTION_TYPE_NOT_SUPPORTED = "SubscriptionTypeNotSupported"
    CROSS_BILLING_ACCOUNT_NOT_ALLOWED = "CrossBillingAccountNotAllowed"
    NOT_AVAILABLE_FOR_DESTINATION_MARKET = "NotAvailableForDestinationMarket"

class TargetCloud(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Possible cloud environments.
    """

    US_GOV = "USGov"
    US_NAT = "USNat"
    US_SEC = "USSec"

class TransactionTypeKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of transaction. Options are all or reservation.
    """

    ALL = "all"
    RESERVATION = "reservation"

class ViewCharges(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The policy that controls whether the users in customer's organization can view charges at pay-
    as-you-go prices.
    """

    ALLOWED = "Allowed"
    NOT_ALLOWED = "NotAllowed"

class ViewChargesPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The policy that controls whether users with Azure RBAC access to a subscription can view its
    charges.
    """

    ALLOWED = "Allowed"
    NOT_ALLOWED = "NotAllowed"
