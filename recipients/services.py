import requests

class MobileServiceProvider:
    @staticmethod
    def verify_phone_number(phone_number, mobile_account_number, mobile_network):
        # API endpoint for phone number verification
        verification_api_url = 'https://example.com/verify-phone-number'

        # Payload to send to the verification API
        payload = {
            'phone_number': phone_number,
            'mobile_account_number': mobile_account_number,
            'mobile_network': mobile_network
        }

        try:
            # Make a POST request to the verification API
            response = requests.post(verification_api_url, json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the response JSON
                verification_result = response.json()

                # Check if the phone number was verified successfully
                if verification_result.get('verified'):
                    return True  # Phone number verified successfully
                else:
                    return False  # Phone number verification failed
            else:
                # Handle non-200 status code
                print(f'Failed to verify phone number: {response.status_code}')
                return False
        except requests.exceptions.RequestException as e:
            # Handle connection errors or other exceptions
            print(f'Error verifying phone number: {e}')
            return False
