
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
gunicorn run:app -b localhost:8000 -w 4 --access-logfile /home/ec2-user/access.log --error-logfile /home/ec2-user/error.log
```

### Nginx Setup:

1. Install and set up Nginx:

```bash
sudo yum install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

2. Set up Nginx configuration and create the relevant folders if not present:

```bash
sudo bash -c 'cat > /etc/nginx/conf.d/flask_app.conf <<EOF
server {
    listen 80;
    server_name florishatwork.xyz www.florishatwork.xyz;

    # Redirect all HTTP requests to HTTPS
    location / {
        return 301 https://\$host\$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name florishatwork.xyz www.florishatwork.xyz;

    ssl_certificate /etc/nginx/ssl/florishatwork_xyz.crt;
    ssl_certificate_key /etc/nginx/ssl/private.key;
    ssl_trusted_certificate /etc/nginx/ssl/florishatwork_xyz.ca-bundle;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
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
sudo vim /etc/nginx/conf.d/flask_app.conf
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
gunicorn run:app -b localhost:8000 -w 4 --access-logfile /home/ec2-user/access.log --error-logfile /home/ec2-user/error.log
```

2. **Configure and Start Nginx**:
   - Configure Nginx after starting Flask with Gunicorn.
   - Nginx acts as a reverse proxy and serves static files efficiently.

```bash
sudo systemctl restart nginx
```

In essence, Gunicorn runs the Flask app, while Nginx directs external requests to Gunicorn.

---

## How to Update the Application with new Code

When you need to update the application, especially after pulling new changes from a repository, you may need to restart Gunicorn and Nginx to reflect these updates. The following script helps automate this process:

```bash
#!/bin/bash

# Navigate to the given directory
cd Main_app/Burnout/

# Perform a git pull
git pull
sleep 15

# Forcefully kill all processes with the name involving "gunicorn"
pkill -9 -f gunicorn
sleep 15

# Start gunicorn with the specified parameters
gunicorn run:app -b localhost:8000 -w 4 --access-logfile /home/ec2-user/access.log --error-logfile /home/ec2-user/error.log &
sleep 15

# Restart nginx
sudo systemctl restart nginx
```

To utilize this script, simply run `./deploy.sh` in the folder you log into when connecting to the ec2 instance or do the following:

1. Copy the script content into a file, for instance, `deply.sh`.
2. Provide executable permissions: `chmod +x deploy.sh`.
3. Run the script using `./deploy.sh` whenever you need to update your Flask application.

Remember, you'll need sufficient permissions to execute some commands, especially those involving `sudo`. Ensure that you are logged in as a user with the required permissions, or consider using `sudo` where needed.

---
