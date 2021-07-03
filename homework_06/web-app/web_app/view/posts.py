from flask import Blueprint, request, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from ..models import db
from ..models import Post

posts_app = Blueprint("posts_app", __name__, url_prefix="/posts")


@posts_app.route("/", endpoint="list")
def posts_list():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)


@posts_app.route("/<int:post_id>/", endpoint="details")
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).one_or_none()
    if post is None:
        raise NotFound(f"Post #{post_id} doesn't exist.")
    return render_template(
        "posts/details.html",
        post=post,
    )


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def post_add():
    if request.method == "GET":
        return render_template("posts/add.html")

    post_name = request.form.get("post-name")
    post_body = request.form.get("post-body")
    if not post_name:
        raise BadRequest("Field product-name is required!")
    elif not post_body:
        raise BadRequest("Field product-body is required!")

    post = Post(name=post_name, body=post_body)
    db.session.add(post)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Could not save post with name {post_name!r}")

    url = url_for("posts_app.details", post_id=post.id)
    return redirect(url)