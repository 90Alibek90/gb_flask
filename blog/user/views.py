from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")
USERS = {
    1: {"name": "Ivan"},
    2: {"name": "Jon"},
    3: {"name": "Mary"}
}


@user.route("/")
@login_required
def user_list():
    from ..models import User
    users = User.query.all()
    return render_template(
        "users/list.html",
        users=users
    )


@user.route("/<int:pk>")
@login_required
def profile(pk: int):
    from ..models import User
    _user = User.query.filter_by(id=pk).one_or_none()
    if _user is None:
        raise NotFound("User id:{}, not found".format(pk))
    return render_template(
        "users/details.html",
        user=_user
    )


def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]["name"]
    else:
        raise NotFound("User id:{}, not found".format(pk))
    return user_name