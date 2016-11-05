from flask import Flask

app = Flask(__name__)
app.config.update(
    WTF_CSRF_ENABLED = True,
    DEBUG=True,
    SECRET_KEY='c11a678785091b7f1334c24a4123ee75'
)

from app.general import views
