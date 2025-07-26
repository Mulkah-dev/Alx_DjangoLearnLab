Here’s a concise guide (suitable for a `README.md` or comment block in your project) documenting how the **permissions and groups** are set up using the variable names like `can_edit`, `can_create`, etc.

---

### 📄 **Permissions & Groups Setup Documentation**

This guide explains how custom permissions and user groups are structured and used within this Django application.

---

#### ✅ **Custom Permissions Used**

| Variable     | Permission Codename | Purpose                       |
| ------------ | ------------------- | ----------------------------- |
| `can_create` | `add_book`          | Allows creating new books     |
| `can_edit`   | `change_book`       | Allows editing existing books |
| `can_delete` | `delete_book`       | Allows deleting books         |
| `can_view`   | `view_book`         | Allows viewing book entries   |

These are built-in permissions automatically created by Django for the `Book` model.

---

#### 👥 **User Groups Setup**

Groups are used to assign sets of permissions to multiple users.

| Group Name | Permissions Assigned                                                 |
| ---------- | -------------------------------------------------------------------- |
| `Editors`  | `can_view`, `can_edit`                                               |
| `Creators` | `can_create`, `can_view`                                             |
| `Admins`   | All permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) |

---

#### 🧪 **Creating and Assigning Groups via Shell**

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model

# Permission Variables
can_create = Permission.objects.get(codename='add_book')
can_edit = Permission.objects.get(codename='change_book')
can_delete = Permission.objects.get(codename='delete_book')
can_view = Permission.objects.get(codename='view_book')

# Group: Editors
editors_group, _ = Group.objects.get_or_create(name='Editors')
editors_group.permissions.set([can_view, can_edit])

# Group: Creators
creators_group, _ = Group.objects.get_or_create(name='Creators')
creators_group.permissions.set([can_view, can_create])

# Group: Admins
admins_group, _ = Group.objects.get_or_create(name='Admins')
admins_group.permissions.set([can_view, can_create, can_edit, can_delete])
```

---

#### 👤 **Assign a User to a Group**

```python
User = get_user_model()
user = User.objects.get(username='admin_user')  # Replace with your actual username

user.groups.add(admins_group)  # Or editors_group, creators_group
user.save()
```

---

#### ✅ **What to Expect in Admin Panel**

* **Editors** can only view and edit books
* **Creators** can create and view books
* **Admins** can create, view, edit, and delete books

---

This structure ensures a clear separation of responsibilities and scalable permission management across the application.


