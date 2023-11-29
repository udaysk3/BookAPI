<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Book App</title>
</head>
<body>
    <h1>Your Book App</h1>
    <p>
        Welcome to Your Book App! This document provides information on how to use the application, configure email credentials, and access documentation.
    </p>
    <h2>Getting Started</h2>
    <p>
        Follow the steps below to get started with Your Book App:
    </p>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/your-username/your-book-app.git</code></li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Migrate the database: <code>python manage.py migrate</code></li>
        <li>Run the development server: <code>python manage.py runserver</code></li>
    </ol>
    <h2>API Endpoints</h2>
    <p>
        Your Book App exposes the following API endpoints:
    </p>
    <ul>
        <li><strong>Books:</strong> /books/ (GET, POST, PUT, DELETE)</li>
        <li><strong>User Registration:</strong> /register/ (POST)</li>
        <li><strong>Email Verification:</strong> /verify/ (GET)</li>
    </ul>
    <h2>Email Configuration</h2>
    <p>
        To configure email settings, create a <code>email_config.json</code> file in the project root with the following format:
    </p>
    <pre>
        <code>
{
    "DEFAULT_FROM_EMAIL": "your_email@example.com",
    "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
    "EMAIL_HOST": "your_email_host.com",
    "EMAIL_PORT": 587,
    "EMAIL_HOST_USER": "your_email@example.com",
    "EMAIL_HOST_PASSWORD": "your_email_password",
    "EMAIL_USE_TLS": false,
    "EMAIL_USE_SSL": false
}
        </code>
    </pre>
    <h2>API Documentation</h2>
    <p>
        Access the Swagger documentation for the API at: <a href="http://127.0.0.1:8000/swagger/" target="_blank">http://127.0.0.1:8000/swagger/</a>
    </p>
    <p>
        Access the Redoc documentation for the API at: <a href="http://127.0.0.1:8000/redoc/" target="_blank">http://127.0.0.1:8000/redoc/</a>
    </p>

</body>
</html>
