

## 🚀 Features

### 🔐 Authentication

* **User Registration** → New users can sign up.
* **User Login/Logout** → Secure session-based authentication.
* **Access Control** → Certain actions (e.g., creating posts) require login.

### 📰 Blog Post Management

* **List View (`/posts/`)** → View all blog posts (public).
* **Detail View (`/posts/<id>/`)** → View individual post (public).
* **Create Post (`/posts/new/`)** → Authenticated users only.
* **Update Post (`/posts/<id>/edit/`)** → Only the post’s author.
* **Delete Post (`/posts/<id>/delete/`)** → Only the post’s author.

---

## 🔒 Permissions

* **Anyone** → Can view posts (list & detail).
* **Authenticated Users** → Can create posts.
* **Post Authors Only** → Can edit or delete their own posts.

This is enforced using:

* `LoginRequiredMixin` → Ensures only logged-in users can create/update/delete.
* `UserPassesTestMixin` → Restricts updates/deletes to the post’s author.

---

## 📂 Project Structure

```
django_blog/
│
├── blog/               # Blog app
│   ├── models.py       # Post model
│   ├── views.py        # CRUD views
│   ├── forms.py        # Post forms
│   ├── urls.py         # Blog URLs
│   ├── templates/blog/ # HTML templates
│
├── users/              # User management app
│   ├── views.py        # Registration, login, logout
│   ├── forms.py        # User creation form
│   ├── urls.py         # User URLs
│   ├── templates/users/# Authentication templates
│
├── django_blog/        # Project settings & main URLs
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd django_blog
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app** at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🧪 Testing

* Verify that all views (list, detail, create, update, delete) work as expected.
* Check that **unauthenticated users** cannot create, update, or delete posts.
* Ensure only the **post author** can edit/delete their own posts.
* Test navigation links between pages (list → detail → edit/delete).

---



---




