# Deployment: Enabling HTTPS with Nginx and Certbot

1. Install Certbot and generate SSL certificates:
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

2. Nginx Configuration Snippet:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location /static/ {
        root /path/to/staticfiles;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
Restart nginx:
sudo systemctl restart nginx

Enable auto-renewal:
sudo certbot renew --dry-run

## ✅ 3. Security Review Report

You can include this in your project’s `docs/security_review.md`:

```markdown
# Security Review Summary

## Implemented Security Measures

- **HTTPS Enforcement**: All requests redirected to HTTPS using `SECURE_SSL_REDIRECT`.
- **HSTS Headers**: Enforced one-year HSTS with subdomain and preload support.
- **Secure Cookies**: Both session and CSRF cookies restricted to HTTPS connections.
- **Clickjacking Protection**: Denied page embedding using `X_FRAME_OPTIONS = "DENY"`.
- **MIME Sniffing Prevention**: Enabled `SECURE_CONTENT_TYPE_NOSNIFF`.
- **Browser XSS Filter**: Enabled `SECURE_BROWSER_XSS_FILTER`.

## Impact on Security

These settings:
- Prevent unauthorized interception of traffic (man-in-the-middle attacks).
- Reduce the risk of cross-site scripting (XSS) and clickjacking.
- Prevent browsers from misinterpreting content types (MIME sniffing).
- Enforce secure transport on all future requests (HSTS).

## Recommendations for Improvement

- **Content Security Policy (CSP)**: Integrate `django-csp` for stricter content control.
- **Security Testing**: Use tools like [OWASP ZAP](https://www.zaproxy.org/) or [SecurityHeaders.com](https://securityheaders.com) to assess HTTP headers.
- **Error Page Security**: Avoid exposing sensitive debug information in error pages.