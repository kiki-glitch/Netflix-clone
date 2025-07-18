# 🎬 Netflix Clone (Django + Tailwind CSS)

A fully functional Netflix-like streaming platform built using **Django**. It includes movies and series, genre-based filtering, a featured slider, trailer previews, search functionality, user authentication, and a dynamic movie modal interface styled with **Tailwind CSS**.

---

## 🚀 Features

- 🔐 User Signup, Login, and Logout
- 🎞️ Add/Edit Movies with:
  - Cover + Card Images
  - Trailer (YouTube or File Upload)
  - Description, Genre, Release Date, Runtime
  - Language, Subtitles, Actors
  - Rating out of 10 with Stars
  - `is_featured` support
- 🔎 Search Bar with auto-reload of results
- 🧾 Genre Filtering (`/genre/<genre_name>`)
- 🧲 Featured Movie on Homepage
- 🖼️ Modal Popup with play button + trailer (optional)
- 📺 Video player for full movie playback
- ➕ Add to My List (AJAX powered)
- 🌐 Responsive design with Tailwind CSS
- 📂 Image + Video uploads supported via `Pillow` and `MEDIA_URL`
- 📃 Admin panel for managing content

---

## 🛠 Tech Stack

- Backend: Django
- Frontend: Tailwind CSS, HTML, JS (AJAX)
- Database: SQLite (default), switchable to PostgreSQL/MySQL
- Media Handling: `ImageField`, `FileField`, and YouTube trailers via `<iframe>`
- Authentication: Django's built-in `User` model

---

## 🧩 Installation

### 🔗 Clone the repository

```bash
git clone https://github.com/yourusername/netflix-clone-django.git
cd netflix-clone-django
```

### 🐍 Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 📁 Create `.env` file

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
```

(Use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` to generate a key)

---

## ⚙️ Run the app locally

```bash
python manage.py migrate
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🖼️ Media Setup

Ensure you set the following in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧪 Test Accounts

- Signup on `/signup`
- Login on `/login`

Admin access:

```bash
python manage.py createsuperuser
```

---

## 📌 Folder Structure

```
project-root/
│
├── core/                   # Django app for movies, models, views
├── templates/              # All HTML files
├── static/assets/          # CSS files, logos, JS
├── media/                  # Uploaded media (images, trailers)
├── db.sqlite3              # Default DB
├── .env                    # Environment settings
├── requirements.txt
└── manage.py
```

---

## ✅ Future Improvements

- Pagination / Lazy Loading
- Watch History Tracking
- Advanced Filters (language, actor, rating, etc.)
- REST API for frontend integration
- React Frontend (Optional)
- Subscriptions and Watchlists

---

## 🧑‍💻 Author

Built with ❤️ by [Alex Wamai](https://github.com/kiki-glitch)

---

## 📄 License

MIT License — Free to use and modify