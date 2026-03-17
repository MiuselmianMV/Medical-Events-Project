import os
from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

# Наш секретный ключ джанго
SECRET_KEY = config("SECRET_KEY")


DEBUG = config("DEBUG", default=False, cast=bool)

# Разрешенные хосты для подключения к серверу нашего Django-приложения 
ALLOWED_HOSTS =  config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=lambda v: [s.strip() for s in v.split(",") if s.strip()],
)

# Стандартные приложения Django, которые идут по умолчанию
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Сторонние приложения, которые мы добавляем для расширения функционала (рест фреймворк, фильтры и т.д.)
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "django_filters",

]

# Наши локальные приложения, которые мы создаем для реализации бизнес-логики нашего проекта
LOCAL_APPS = [
    "apps.users",
    "apps.events",
]

# Объединяем все приложения в один список, чтобы Django знал обо всех установленных приложениях
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Настройки нашего Миддлвера
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Корневой юрл файл нашего проекта
ROOT_URLCONF = "config.urls"


# Настройки шаблонов
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB', default='medicalevents'),
        'USER': config('POSTGRES_USER', default='postgres'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432', cast=int),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': config('DB_CONN_MAX_AGE', default=60, cast=int),
        "OPTIONS": {
            "sslmode": config("DB_SSLMODE", default="require"),
        }
    }
}
AUTH_USER_MODEL = "users.User"  # Указываем кастомную модель пользователя

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Настройки интернационализации
LANGUAGE_CODE = "uk"

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('uk', 'Ukrainian'),
    ('en', 'English'),
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Настройки Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # По умолчанию все запросы разрешены
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",  # Ограничение по количеству запросов для анонимных пользователей
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "500/hour",  # Максимум 500 запросов в час для анонимных пользователей
    },
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",  # Ответы будут в формате JSON
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",  # Принимаем данные в формате JSON
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend", # Фильтрация по полям модели
        ],
    
    "DEFAULT_PAGINATION_CLASS": 
        "rest_framework.pagination.PageNumberPagination", # Пагинация по номеру страницы

    "PAGE_SIZE": 
        12, # Количество объектов на странице при пагинации
}

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True  # Разрешаем все источники при DEBUG режиме
else:
    CORS_ALLOWED_ORIGINS = [
        config("FRONTEND_URL"),  # Разрешаем только фронтенд домен, указанный в .env файле
    ]

#JWT configuration
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), # Время жизни access токена
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Время жизни refresh токена
    'ROTATE_REFRESH_TOKENS': True,                  # Обновляем refresh токен при каждом запросе
    
    'BLACKLIST_AFTER_ROTATION': True,               # Добавляем старые refresh токены в черный список
    'UPDATE_LAST_LOGIN': True,                      # Обновляем поле last_login при каждом запросе
    'ALGORITHM': 'HS256',                           # Алгоритм шифрования
    'SIGNING_KEY': SECRET_KEY,                      # Ключ для шифрования
    
    'AUTH_HEADER_TYPES': ('Bearer',),               # Тип заголовка авторизации
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',       # Имя заголовка авторизации
    'USER_ID_FIELD': 'id',                          # Поле пользователя, которое будет использоваться
    'USER_ID_CLAIM': 'user_id',                     # Клейм, в котором будет храниться ID пользователя
}


SECURE_BROWSER_XSS_FILTER = True # Включаем защиту от XSS атак (не даём вписывать скрипты в поля форм и т.д.)
X_FRAME_OPTIONS = "DENY" # Запрещаем отображение сайта в iframe (защита от кликджекинга)
SECURE_CONTENT_TYPE_NOSNIFF = True # Защита от MIME-атаки (не даём отправлять .exe файлы вместо изображений и т.д.)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG" if DEBUG else "INFO",
            "propagate": False,
        },
    },
}

# S3 хранилище для медиа файлов
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", default="")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", default="eu-north-1")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

AWS_S3_PUBLIC = config("AWS_S3_PUBLIC", default=True, cast=bool)
AWS_QUERYSTRING_AUTH = False