# BigMart E-commerce Web Application

BigMart is a fully functional e-commerce platform built with Django, designed for both admin and user interactions. It includes features for managing categories and products, viewing product listings, adding items to the cart, checking out, and processing payments using Razorpay.

## Features

### Admin Features:
- **Dashboard**: View a summary of the system including categories, products, and the current date.
- **Category Management**: Add, update, delete, and view product categories.
- **Product Management**: Add, update, delete, and view products with their respective details such as price, description, and category.
- **User Management**: Manage the newsletter subscriptions and user contact messages.

### User Features:
- **Homepage**: Users can browse products, filter by category, and view products in detail.
- **About Page**: Information about the platform.
- **Contact Page**: Users can contact the platform by filling out a message form.
- **Newsletter Subscription**: Users can subscribe to newsletters by providing their email.
- **User Authentication**: Users can sign up, log in, and log out.
- **Cart Management**: Users can add products to the cart, view cart items, and remove items.
- **Checkout**: Users can review their cart, apply shipping charges, and proceed with the order.
- **Payment Integration**: Integration with Razorpay for secure payment processing.

## Project Structure

### Admin Views:
- **Category Management**:
  - Add, edit, update, and delete categories.
  - View all categories in the system.
  
- **Product Management**:
  - Add, update, and delete products.
  - View all products and filter them by category.

- **User Management**:
  - View user-submitted contact messages.
  - View newsletter subscriptions.

### User Views:
- **Homepage**: Displays product categories and all available products.
- **Product Filtering**: Products can be filtered by categories.
- **Product Detail Page**: View detailed information about a specific product.
- **User Authentication**:
  - **Login**: Users can log in with their credentials.
  - **Sign Up**: Users can create a new account.
  - **Logout**: Users can log out of their account.
  
- **Cart Management**:
  - Add products to the cart.
  - Remove products from the cart.
  - View the cart's content, including total price, shipping charges, and the total amount.

- **Checkout**: Users can proceed to checkout after reviewing the cart.
  
- **Payment Integration**: Payments are processed using Razorpay. Users can complete their orders via a secure payment gateway.

## Technologies Used
- **Django**: Web framework used for building the application.
- **Razorpay**: Payment gateway integration.
- **SQLite**: Database for storing product, category, and user data.
- **HTML, CSS, JavaScript**: Frontend technologies for building the user interface.

