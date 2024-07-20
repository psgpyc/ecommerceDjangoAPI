# E-Commerce API

## Overview

This is a RESTful API for an e-commerce application built using Django Rest Framework (DRF). It provides endpoints for managing products, orders, users, and more.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- Product management (CRUD operations)
- Order processing
- Shopping cart functionality
- User profile management
- Search and filtering capabilities
- Pagination for list views

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework 3.12+

## Installation

1. Clone the repository:
```python
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

2. Create a virtual environment and activate it
```python -m venv venv
source venv/bin/activate 
# On Windows, use 
venv\Scripts\activate
```


3. Install the required packages:
```python
pip install -r requirements.txt

```
4. Set up the database:
```python
python manage.py migrate

```
5. Create a superuser:
```python
python manage.py createsuperuser
```
6. Run the development server
```python
python manage.py runserver
```

## Usage

The API will be available at `http://localhost:8000/api/`. You can use tools like cURL, Postman, or a web browser to interact with the API endpoints.

## API Endpoints

### Authentication

- `POST /api/auth/register/`: Register a new user
- `POST /api/auth/login/`: Obtain a JWT token
- `POST /api/auth/refresh/`: Refresh JWT token
- `POST /api/auth/logout/`: Logout (invalidate token)

### Products

- `GET /api/products/`: List all products
- `POST /api/products/`: Create a new product
- `GET /api/products/{id}/`: Retrieve a specific product
- `PUT /api/products/{id}/`: Update a product
- `DELETE /api/products/{id}/`: Delete a product

### Orders

- `GET /api/orders/`: List all orders for the authenticated user
- `POST /api/orders/`: Create a new order
- `GET /api/orders/{id}/`: Retrieve a specific order
- `PUT /api/orders/{id}/`: Update an order
- `DELETE /api/orders/{id}/`: Cancel an order

### User Profile

- `GET /api/profile/`: Retrieve the user's profile
- `PUT /api/profile/`: Update the user's profile

### Cart

- `GET /api/cart/`: Retrieve the user's cart
- `POST /api/cart/`: Add an item to the cart
- `PUT /api/cart/{id}/`: Update a cart item
- `DELETE /api/cart/{id}/`: Remove an item from the cart

## Authentication

This API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints, include the JWT token in the Authorization header of your requests:



## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.