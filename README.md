<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>🛍️ Product Review API</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 2rem;
      line-height: 1.6;
      background-color: #f5f7fa;
      color: #333;
    }
    h1, h2, h3 {
      color: #2b2e4a;
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }
    code, pre {
      background-color: #eee;
      padding: 0.4rem 0.6rem;
      border-radius: 5px;
      font-family: 'Courier New', Courier, monospace;
    }
    .badge {
      background-color: #9a1750;
      color: #fff;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-size: 0.9rem;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      background-color: white;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 0.75rem;
      text-align: left;
    }
    th {
      background-color: #f3f3f3;
    }
    a {
      color: #0077cc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    section {
      margin-bottom: 2rem;
    }
    .code-block {
      background: #282c34;
      color: #fff;
      padding: 1rem;
      border-radius: 6px;
      overflow-x: auto;
      margin-top: 1rem;
    }
  </style>
</head>
<body>

  <h1>🛍️ Product Review API</h1>
  <p>
    A robust, secure, and developer-friendly RESTful API for managing products and customer reviews. Built with Django REST Framework and JWT, this API supports admin-level product control and public product browsing, with user-authenticated review submission.
  </p>

  <section>
    <h2>🚀 Tech Stack</h2>
    <ul>
      <li>Python 3.12</li>
      <li>Django 5.x</li>
      <li>Django REST Framework</li>
      <li>PostgreSQL</li>
      <li>JWT Auth (<code>djangorestframework-simplejwt</code>)</li>
      <li>Swagger UI (<code>drf-yasg</code>)</li>
      <li>dotenv</li>
    </ul>
  </section>

  <section>
    <h2>⚙️ Getting Started</h2>
    <h3>1. Clone and Setup</h3>
    <pre class="code-block">
git clone https://github.com/yourusername/product-review-api.git
cd product-review-api
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
    </pre>

    <h3>2. Setup Environment Variables</h3>
    <pre class="code-block">
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
    </pre>

    <h3>3. Migrate and Create Superuser</h3>
    <pre class="code-block">
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
    </pre>

    <h3>4. Run Server</h3>
    <pre class="code-block">python manage.py runserver</pre>
  </section>

  <section>
    <h2>🔐 Authentication (JWT)</h2>
    <p>
      Obtain access tokens via:
      <code>POST /api/auth/login/</code>
    </p>
    <pre class="code-block">
{
  "username": "your_username",
  "password": "your_password"
}
    </pre>
    <p>Use access token in header:</p>
    <pre class="code-block">
Authorization: Bearer &lt;your_access_token&gt;
    </pre>
  </section>

  <section>
    <h2>📘 API Endpoints</h2>

    <h3>🧑 User Authentication</h3>
    <table>
      <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
      <tr><td>POST</td><td>/api/auth/register/</td><td>Register new user</td></tr>
      <tr><td>POST</td><td>/api/auth/login/</td><td>Obtain JWT token</td></tr>
      <tr><td>POST</td><td>/api/auth/token/refresh/</td><td>Refresh access token</td></tr>
    </table>

    <h3>📦 Products</h3>
    <table>
      <tr><th>Method</th><th>Endpoint</th><th>Auth</th><th>Description</th></tr>
      <tr><td>GET</td><td>/api/products/</td><td>❌</td><td>List all products</td></tr>
      <tr><td>POST</td><td>/api/products/</td><td>✅ (admin)</td><td>Create new product</td></tr>
      <tr><td>GET</td><td>/api/products/{id}/</td><td>❌</td><td>Get single product</td></tr>
    </table>

    <h3>📝 Reviews</h3>
    <table>
      <tr><th>Method</th><th>Endpoint</th><th>Auth</th><th>Description</th></tr>
      <tr><td>POST</td><td>/api/reviews/create/</td><td>✅</td><td>Submit review for product</td></tr>
      <tr><td>GET</td><td>/api/products/{product_id}/reviews/</td><td>❌</td><td>List reviews of product</td></tr>
    </table>
  </section>

  <section>
    <h2>🌐 API Documentation</h2>
    <p>
      📄 <a href="http://localhost:8000/swagger/" target="_blank">Swagger UI</a><br/>
      📘 <a href="http://localhost:8000/redoc/" target="_blank">ReDoc UI</a>
    </p>
  </section>

  <section>
    <h2>🧪 Example cURL Requests</h2>
    <h3>Login</h3>
    <pre class="code-block">
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "adminpass"}'
    </pre>

    <h3>Create Review</h3>
    <pre class="code-block">
curl -X POST http://localhost:8000/api/reviews/create/ \
  -H "Authorization: Bearer &lt;your_access_token&gt;" \
  -H "Content-Type: application/json" \
  -d '{
    "rating": 5,
    "review_text": "Fantastic product!",
    "product": 1
  }'
    </pre>
  </section>

  <section>
    <h2>🧑‍💻 Admin Access</h2>
    <p>
      Only users with <code>is_staff = True</code> can create products and access <code>/admin/</code>.
    </p>
  </section>

  <section>
    <h2>📂 Project Structure</h2>
    <pre class="code-block">
product-review-api/
├── backend/
│   ├── settings.py
│   ├── urls.py
├── users/
├── product/
├── review/
├── .env
├── requirements.txt
└── manage.py
    </pre>
  </section>

  <section>
    <h2>📜 License</h2>
    <p>
      MIT License. Feel free to use and modify this project.
    </p>
  </section>

  <section>
    <h2>🤝 Contributing</h2>
    <p>Pull requests are welcome! Open issues first to propose changes.</p>
  </section>

  <section>
    <h2>📧 Contact</h2>
    <p>
      Developer: <strong>Sreeraj P</strong><br/>
      Email: <a href="mailto:sreerajporukandy@gmail.com">sreerajporukandy@gmail.com</a><br/>
      GitHub: <a href="https://github.com/srreeraj" target="_blank">github.com/srreeraj</a>
    </p>
  </section>

</body>
</html>
