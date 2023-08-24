
# Deploying Flask Application on EC2 with Nginx and Gunicorn

## Prerequisites

Ensure you have the following dependencies installed:

- Python
- MySQL

Download all required python packages:

```bash
pip install -r requirements.txt
```

## Structure of the APP

- **Database**: MYSQL
- **Front end**: jinja3 (HTML/CSS)
- **Back end**: Flask/Python
- **Web Server**: Nginx
- **WSGI server**: Gunicorn

## Starting the Application

Note:
**Configure the database**: Check the `.env` file and ensure the string is correct.

### Gunicorn Setup:

1. Install Gunicorn (if not done through `requirements.txt`):

```bash
pip install gunicorn
```

2. Navigate to your Flask app's directory:

```bash
cd /path/to/your/flask_app
```

3. Start Gunicorn:

```bash
gunicorn run:app -b localhost:8000
```

### Nginx Setup:

1. Install and set up Nginx:

```bash
sudo yum install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

2. Set up Nginx configuration:

```bash
sudo bash -c 'cat > /etc/nginx/conf.d/flask_app.conf <<EOF
... # (your configuration details here)
EOF'
```

3. Restart Nginx:

```bash
sudo systemctl restart nginx
```

## SSL Configuration

### Creating SSL Certificate:

1. Generate CSR on AWS.
2. Use CSR to get certificates from the CA.

### Installing the SSL Certificate:

1. Upload the certificates to your EC2 instance:

```bash
scp your-certificate.crt ec2-user@your-ec2-ip:/home/ec2-user/
scp your-private.key ec2-user@your-ec2-ip:/home/ec2-user/
scp your-ca-bundle.crt ec2-user@your-ec2-ip:/home/ec2-user/
```

2. Move the certificates to the correct directory:

```bash
sudo mkdir -p /etc/nginx/ssl
sudo mv /home/ec2-user/*.crt /etc/nginx/ssl/
sudo mv /home/ec2-user/*.key /etc/nginx/ssl/
sudo chmod 600 /etc/nginx/ssl/your-private.key
```

3. Update your Nginx configuration:

```bash
sudo vim /etc/nginx/sites-available/your-site-config
```

4. Validate and restart Nginx:

```bash
sudo nginx -t
sudo systemctl restart nginx
```

5. Ensure your AWS security group allows HTTPS traffic (port 443).
6. Test your setup by navigating to `https://your_domain_name`.

## Architecture Insights

When deploying a Flask application with Gunicorn and Nginx:

1. **Start Gunicorn with the Flask App**:
   - Ensure your Flask app works as expected.
   - Use Gunicorn to serve the Flask app.

```bash
gunicorn your_flask_app:app -b localhost:8000
```

2. **Configure and Start Nginx**:
   - Configure Nginx after starting Flask with Gunicorn.
   - Nginx acts as a reverse proxy and serves static files efficiently.

```bash
sudo systemctl restart nginx
```

In essence, Gunicorn runs the Flask app, while Nginx directs external requests to Gunicorn.

---
