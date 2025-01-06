from loggers import TransactionLogger
from notifiers import EmailNotifier, NotifierProtocol, SMSNotifier
from processors import StripePaymentProcessor
from factory import PaymentProcessorFactory
from validators import CustomerValidator, PaymentDataValidator
from logging_service import PaymentServiceLogging

from commons import CustomerData, ContactInfo, PaymentData
from builder import PaymentServiceBuilder


def get_email_notifier() -> EmailNotifier:
    return EmailNotifier()


def get_sms_notifier() -> SMSNotifier:
    return SMSNotifier(gateway="SMSGatewayExample")


def get_notifier_implementation(
    customer_data: CustomerData,
) -> NotifierProtocol:
    if customer_data.contact_info.phone:
        return get_sms_notifier()

    if customer_data.contact_info.email:
        return get_email_notifier()
    raise ValueError("No se puede elegir la estrategia correcta")


def get_customer_data() -> CustomerData:
    contact_info = ContactInfo(email="jon.doe@mail.co")
    customer_data = CustomerData(name="Jon Doe", contact_info=contact_info)

    return customer_data


if __name__ == "__main__":
    stripe_payment_processor = StripePaymentProcessor()

    customer_data = get_customer_data()
    notifier = get_notifier_implementation(customer_data=customer_data)

    email_notifier = get_email_notifier()
    sms_notifier = get_sms_notifier()

    customer_validator = CustomerValidator()
    payment_data_validator = PaymentDataValidator()
    logger = TransactionLogger()

    payment_data = PaymentData(amount=100, source="tok_visa", currency="USD")
    service = PaymentProcessorFactory.create_payment_processor(
        payment_data=payment_data
    )
    
    service.process_transaction(customer_data=customer_data, payment_data=payment_data)

    logging_service = PaymentServiceLogging(wrapped=service)

    logging_service.process_transaction(customer_data=customer_data, payment_data=payment_data)

    payment_data = PaymentData(amount=100, source="tok_visa", currency="USD")



    builder = PaymentServiceBuilder()
    service = (
        builder.set_logger()
        .set_payment_validator()
        .set_customer_validator()
        .set_payment_processor(payment_data)
        .set_notifier(customer_data)
        .build()
    )

    service.process_transaction(customer_data,payment_data)
