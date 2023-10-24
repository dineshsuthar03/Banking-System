"# Banking-System" 
# MyBank - A Simple Banking System

MyBank is a simple and straightforward banking system built with Django. This project allows users to perform common banking operations like creating accounts, checking balances, depositing, withdrawing, and transferring funds between accounts.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Create Account**: Users can create new bank accounts, specifying the account holder's name, account number, and initial balance.

- **Get Account Balance**: Users can check the account balance by providing the account number.

- **Deposit**: Funds can be deposited into an account by specifying the account number and the deposit amount.

- **Withdraw**: Account holders can withdraw funds, given that there are sufficient funds in the account.

- **Transfer**: Funds can be transferred between two accounts, provided that the source account has sufficient balance.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Django (Install with `pip install django`)

## Installation

To set up the MyBank project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/dineshsuthar03/mybank.git
2. Navigate to the project directory:
  cd mybank
3.  Create a virtual environment (optional but recommended):
  python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
4. Install project dependencies:
  pip install -r requirements.txt
5. Run database migrations:
  python manage.py migrate
6. Create a superuser to access the admin panel:
  python manage.py createsuperuser
7. Start the development server:
  python manage.py runserver
8. Access the admin panel at http://localhost:8000/admin/ to manage accounts.

Usage
Access the main banking interface at http://localhost:8000/.

To create accounts, deposit, withdraw, or transfer funds, you can use the web interface provided.

For administrative tasks, visit the admin panel at http://localhost:8000/admin/.

Contributing
We welcome contributions from the community! If you'd like to contribute to this project, please follow our contributing guidelines.

License
This project is licensed under the MIT License. See the LICENSE file for details.
