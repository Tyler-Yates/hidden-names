from flask import Blueprint, current_app, redirect, render_template

from application.data.dao import TTL_SECONDS, ApplicationDao

HTML_BLUEPRINT = Blueprint("routes.html", __name__)


@HTML_BLUEPRINT.route("/")
def homepage():
    return "<a href='/documents'>Documents</a>"


@HTML_BLUEPRINT.route("/documents")
def documents_page():
    documents = _get_dao().get_documents()
    return render_template("documents.html", documents=documents, collection_ttl=TTL_SECONDS)


@HTML_BLUEPRINT.route("/documents/<document_id>")
def document_page(document_id):
    document = _get_dao().get_document(document_id)
    return render_template("document.html", document=document)


# HTML forms do not allow use of the DELETE method so use POST and make the endpoint path descriptive
@HTML_BLUEPRINT.route("/delete_document/<document_id>", methods=["POST"])
def delete_document(document_id):
    _get_dao().delete_document(document_id)
    return redirect("/documents", code=302)


# HTML forms do not allow use of the DELETE method so use POST and make the endpoint path descriptive
@HTML_BLUEPRINT.route("/delete_documents", methods=["POST"])
def delete_documents():
    _get_dao().delete_documents()
    return redirect("/documents", code=302)


@HTML_BLUEPRINT.route("/create_document")
def add_document_page():
    return render_template("create_document.html")


def _get_dao() -> ApplicationDao:
    return current_app.config["DB"]
