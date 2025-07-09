## 🛒E-commerce Platform

This repository hosts the source code for a full-featured e-commerce web application built using Django. The platform allows users to browse products, manage a shopping cart, and complete purchases via a simple checkout process.

## 🚀Project Overview
This Django-based e-commerce site provides the following key functionalities:
    • Product Catalog: Browse & view product listings with images &
      discriptions.
    • User Authentication: Register, log in, and manage sessions securely.
    • Shopping Cart: Add, update, and remove items from the cart.
    • Order Management: Place orders and track them through the system.

The project uses SQLite as the default database and is suitable for learning or small-scale deployments.

## 🛠️Technologies Used:

Technology	                   Purpose
------------------------------------------------------
Python	      ---->      Core programming language
Django	      ---->      Web framework
SQLite	      ---->      Lightweight development DB
HTML/CSS	  ---->      Frontend structure & styling
JavaScript	  ---->      Client-side interactivity

## Project Structure:
The project follows a typical Django project structure. Key files and directories include:
"bash"
ecommerce-platform/
│
├── ecommerce/              # Project settings and URLs
├── store/                  # Main app with models, views, templates
├── media/                  # Uploaded media (e.g. product images)
│   └── products/           # Product image directory
├── db.sqlite3              # SQLite database
├── manage.py               # Django CLI utility
└── requirements.txt        # Dependencies (optional but recommended)
Key supporting files:
    • .gitattributes: Handles Git file encoding settings.
    • store/views.py: Contains view logic like login_view.
    • store/templates/store/login.html: Login interface for users.

## 🔐User Authentication
   Example login_view behavior:
    • Accepts POST requests with username and password.
    • Uses Django’s authenticate() and login() methods.
    • Redirects authenticated users to the store homepage.
    • Returns error messages for failed login attempts.    

## 🗃️Database Overview:
Based on the contents of db.sqlite3, the platform uses standard Django auth
models plus custom store models:

   Table Name	                            Purpose
----------------------------------------------------------------------
auth_user                     ------>	Registered users
auth_group, auth_permission   ------>	User roles and access control
store_product	              ------>	Product details
store_productimage            ------>	Images linked to products
store_cartitem                ------>   Items currently in user carts
store_order	                  ------>	Completed orders

## Getting Started
To run this project, you will need to have Python and Django installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aadix07/Ecommerce_Website.git
    cd Ecommerce_Website
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt # Assuming a requirements.txt file exists
    ```

  3.  **Apply migrations:**
    This will set up your database schema.
    ```bash
    python manage.py migrate
    ```

4.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application should then be accessible at `http://127.0.0.1:8000/`.
