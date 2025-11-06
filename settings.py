import os

# Number of participants per group (adjust as needed)
PARTICIPANTS_PER_GROUP = 4

SESSION_CONFIGS = [
    dict(
        name="public_goods_treatment_1",
        display_name="Citizen Reporting PGG - Treatment 1",
        num_demo_participants=PARTICIPANTS_PER_GROUP,
        app_sequence=["public_goods"],
        treatment=1,  # Treatment group 1
    ),
    dict(
        name="public_goods_treatment_2",
        display_name="Citizen Reporting PGG - Treatment 2",
        num_demo_participants=PARTICIPANTS_PER_GROUP,
        app_sequence=["public_goods"],
        treatment=2,  # Treatment group 2
    ),
    dict(
        name="public_goods_treatment_3",
        display_name="Citizen Reporting PGG - Treatment 3",
        num_demo_participants=PARTICIPANTS_PER_GROUP,
        app_sequence=["public_goods"],
        treatment=3,  # Treatment group 3
    ),
    dict(
        name="public_goods_treatment_4",
        display_name="Citizen Reporting PGG - Treatment 4",
        num_demo_participants=PARTICIPANTS_PER_GROUP,
        app_sequence=["public_goods"],
        treatment=4,  # Treatment group 4
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "USD"
USE_POINTS = False
INSTALLED_APPS = ["otree"]

# Database configuration for Railway/Production
# Railway provides DATABASE_URL for PostgreSQL
if "DATABASE_URL" in os.environ:
    import dj_database_url
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=False,
        )
    }
else:
    # Local development - use SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "_defaultdb",
        }
    }

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = os.environ.get("OTREE_ADMIN_PASSWORD", "changeme")
SECRET_KEY = os.environ.get("SECRET_KEY", "replace-this-secret-key-for-production")

