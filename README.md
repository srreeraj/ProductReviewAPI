<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Product Review API</title>
</head>
<body>

  <h1>🛍️ Product Review API</h1>
  <p>
    A robust, secure, and developer-friendly RESTful API for managing products and customer reviews. Built with Django REST Framework and JWT authentication, this API supports admin-level product management and authenticated user reviews, while also offering public access to product and review listings.
  </p>

  <h2>🚀 Tech Stack</h2>
  <ul>
    <li>Python 3.12</li>
    <li>Django 5.x</li>
    <li>Django REST Framework</li>
    <li>PostgreSQL</li>
    <li>JWT Authentication (djangorestframework-simplejwt)</li>
    <li>Swagger UI (drf-yasg)</li>
    <li>dotenv for environment configuration</li>
  </ul>

  <h2>⚙️ Getting Started</h2>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/yourusername/product-review-api.git
cd product-review-api
</code></pre>

  <h3>2. Create & Activate Virtual Environment</h3>
  <pre><code>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
</code></pre>

  <h3>3. Install Dependencies</h3>
  <pre><code>pip install -r requirements.txt
</code></pre>

  <h3>4. Configure Environment Variables</h3>
  <p>Create a <code>.env</code> file in the root:</p>
  <pre><code>SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
</code></pre>

  <h3>5. Run Migrations & Create Superuser</h3>
  <pre><code>python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
</code></pre>

  <h3>6. Start the Development Server</h3>
  <pre><code>python manage.py runserver
</code></pre>

  <h2>🔐 Authentication (JWT)</h2>
  <p>Login to get access token:</p>
  <pre><code>POST /api/auth/login/</code></pre>
  <p>Request body:</p>
  <pre><code>{
  "username": "your_username",
  "password": "your_password"
}</code></pre>
  <p>Use access token in the header:</p>
  <pre><code>Authorization: Bearer &lt;your_access_token&gt;</code></pre>

  <h2>📘 API Endpoints</h2>

  <h3>🧑 User Authentication</h3>
  <table border="1" cellpadding="5">
    <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
    <tr><td>POST</td><td>/api/auth/register/</td><td>Register new user</td></tr>
    <tr><td>POST</td><td>/api/auth/login/</td><td>Obtain JWT token</td></tr>
    <tr><td>POST</td><td>/api/auth/token/refresh/</td><td>Refresh access token</td></tr>
  </table>

  <h3>📦 Products</h3>
  <table border="1" cellpadding="5">
    <tr><th>Method</th><th>Endpoint</th><th>Auth</th><th>Description</th></tr>
    <tr><td>GET</td><td>/api/products/</td><td>No</td><td>List all products</td></tr>
    <tr><td>POST</td><td>/api/products/</td><td>Admin</td><td>Create new product</td></tr>
    <tr><td>GET</td><td>/api/products/{id}/</td><td>No</td><td>Get single product</td></tr>
  </table>

  <h3>📝 Reviews</h3>
  <table border="1" cellpadding="5">
    <tr><th>Method</th><th>Endpoint</th><th>Auth</th><th>Description</th></tr>
    <tr><td>POST</td><td>/api/reviews/create/</td><td>Yes</td><td>Create review</td></tr>
    <tr><td>GET</td><td>/api/products/{product_id}/reviews/</td><td>No</td><td>Get reviews</td></tr>
  </table>

  <h2>🌐 API Documentation</h2>
  <ul>
    <li><a href="http://localhost:8000/swagger/">Swagger UI</a></li>
    <li><a href="http://localhost:8000/redoc/">ReDoc UI</a></li>
  </ul>

  <h2>🧪 Example cURL Requests</h2>

  <h3>Login</h3>
  <pre><code>curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "adminpass"}'
</code></pre>

  <h3>Create Review</h3>
  <pre><code>curl -X POST http://localhost:8000/api/reviews/create/ \
  -H "Authorization: Bearer &lt;your_access_token&gt;" \
  -H "Content-Type: application/json" \
  -d '{
    "rating": 5,
    "review_text": "Fantastic product!",
    "product": 1
  }'
</code></pre>

  <h2>🧑‍💻 Admin Access</h2>
  <p>Only users with <code>is_staff=True</code> can create products or access the Django Admin panel at <code>/admin/</code>.</p>

  <h2>📂 Project Structure</h2>
  <pre><code>product-review-api/
├── backend/
│   ├── settings.py
│   ├── urls.py
├── users/
├── product/
├── review/
├── .env
├── requirements.txt
└── manage.py
</code></pre>

  <h2>📜 License</h2>
  <p>MIT License. Free to use and modify.</p>

  <h2>🤝 Contributing</h2>
  <p>Pull requests are welcome! Please open an issue first to discuss changes.</p>

  <h2>📧 Contact</h2>
  <p>
    Developer: Sreeraj P<br />
    Email: <a href="mailto:sreeraj@example.com">sreeraj@example.com</a><br />
    GitHub: <a href="https://github.com/yourusername">github.com/yourusername</a>
  </p>

</body>
</html>
