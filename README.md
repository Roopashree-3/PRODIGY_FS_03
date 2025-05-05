🛒 Local Store – Flask Shopping Cart App

This is a basic Flask web application that allows users to browse products, add them to a shopping cart, and view the total cost of selected items. It demonstrates routing, session handling, templating with Jinja2, and basic use of static assets.

---
 📁 Project Structure

```
local-store/
├── app.py
├── products.py
├── static/
│   └── images/
│       ├── product1.jpg
│       ├── product2.jpg
│       └── product3.jpg
├── templates/
│   ├── index.html
│   └── cart.html


 🚀 Features

* View a list of products with images, descriptions, and prices
* Add products to a session-based shopping cart
* View items in the cart
* Display total cost of all items in the cart
* Lightweight and easy to run locally



### 🔧 Setup Instructions


 Install dependencies**
   You can use a virtual environment (optional):

   ```bash
   pip install Flask
   ```

 **Run the app**

   ```bash
   python app.py
   ```

 Open your browser and go to:
   [http://127.0.0.1:5050](http://127.0.0.1:5050)

---

### 📦 Files Explained

* **`app.py`** – Main Flask app with routes and session logic
* **`products.py`** – Product data (in-memory list)
* **`templates/`** – HTML templates using Jinja2
* **`static/images/`** – Product images

---

### 🧠 Concepts Used

* Flask routes and URL handling
* Jinja2 templating engine
* Session management with Flask
* Dynamic rendering of product and cart data
* HTML/CSS layout with basic Flexbox

---


