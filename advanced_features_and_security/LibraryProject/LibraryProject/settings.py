from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!5@6k_bgc%x_hdh2$o0%u8yv4y98b43vdwtnnv^4gwhiu7oq*7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '127.0.0.1']

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app.apps.RelationshipAppConfig',
    'csp',  # Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  # Make sure there's a comma here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========== 🔐 SECURITY SETTINGS ==========

# Cookies should only be sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# ✅ Security Settings for HTTPS

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Required for HTTPS enforcement

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookies sent only over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Secure HTTP Headers
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent content type sniffing
X_FRAME_OPTIONS = 'DENY'            # Protect against clickjacking
SECURE_BROWSER_XSS_FILTER = True    # Enable XSS filter in browsers

