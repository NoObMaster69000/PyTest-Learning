# test_advanced_mocking.py
import pytest
from unittest.mock import PropertyMock
from service import process_payment, PaymentProcessor

# This test demonstrates how to mock a property using `PropertyMock`.
def test_process_payment_with_mocked_property(mocker):
    """
    Tests that `process_payment` calls the `charge` method when the
    processor is configured.
    """
    # We want to mock the `is_configured` property to return True.
    # `new_callable=PropertyMock` tells mocker to use a PropertyMock for this patch.
    mocker.patch(
        'service.PaymentProcessor.is_configured',
        new_callable=PropertyMock,
        return_value=True
    )

    # We also need to mock the `charge` method, since we're only testing
    # the logic of `process_payment`, not the `charge` method itself.
    mock_processor = PaymentProcessor(api_key="dummy_key")
    mocker.patch.object(mock_processor, 'charge', return_value={"status": "success"})

    # Call the function with the mocked processor.
    process_payment(100, mock_processor)

    # Assert that the `charge` method was called with the correct arguments.
    mock_processor.charge.assert_called_once_with(100)

def test_process_payment_unconfigured(mocker):
    """
    Tests that `process_payment` raises a ValueError if the processor
    is not configured.
    """
    # Mock the `is_configured` property to return False.
    mocker.patch(
        'service.PaymentProcessor.is_configured',
        new_callable=PropertyMock,
        return_value=False
    )

    mock_processor = PaymentProcessor(api_key=None)
    mocker.patch.object(mock_processor, 'charge') # Mock the charge method as well

    # Assert that a ValueError is raised.
    with pytest.raises(ValueError, match="Payment processor is not configured."):
        process_payment(100, mock_processor)

    # Assert that the `charge` method was never called.
    mock_processor.charge.assert_not_called()
