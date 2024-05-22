# PhonePe Integration with Django

This project demonstrates how to integrate PhonePe payment gateway with a Django application. It allows users to make
payments and captures payments through a webhook.

## Getting Started

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.9 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/shahdeep1908-tech/PhonePe-Payment-Integration.git
   cd phonepe_payment
   ```
2. Create a virtual environment (optional but recommended):
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install project dependencies:
   ```shell
   pip install -r requirements.txt
   pip install --index-url https://phonepe.mycloudrepo.io/public/repositories/phonepe-pg-sdk-python --extra-index-url https://pypi.org/simple phonepe_sdk==1.1.0
   ```

### Configuration

Configure PhonePe API Keys:

Create .env file and update "PHONEPE_MERCHANT_ID", "PHONEPE_SALT_KEY" and "PHONEPE_SALT_INDEX=1" with your actual PhonePe API
credentials.

## Usage

1. Start the Django application:
   ```shell
   python manage.py runserver
   ```

2. Access the payment initiation page:

   Open your web browser and visit http://localhost:8000 to access the PhonePe payment page.

## Project Workflow Diagram

*Figure 1: PhonePe Payment Dashboard*
![dashboard.png](images%2Fdashboard.png)
![dashboard2.png](images%2Fdashboard2.png)

*Figure 2: PhonePe Payment Options*
![phonepe_payment_options.png](images%2Fphonepe_payment_options.png)

*Figure 3: PhonePe Payment OTP Verification*
![OTP_verification.png](images%2FOTP_verification.png)

*Figure 4: PhonePe Success Page*
![payment_success.png](images%2Fpayment_success.png)

*Figure 5: PhonePe Success Page Redirect
![success_redirect.png](images%2Fsuccess_redirect.png)