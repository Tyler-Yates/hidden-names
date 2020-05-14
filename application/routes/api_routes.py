from flask import Blueprint, current_app, jsonify, redirect, request
from flask_accept import accept

from application.data.dao import ID_FIELD, ApplicationDao

API_BLUEPRINT = Blueprint("routes.api", __name__, url_prefix="/api/v1/")


@API_BLUEPRINT.route("/documents")
def documents_api_page():
    documents = _get_dao().get_documents()
    return jsonify(list(documents))


@API_BLUEPRINT.route("/documents/<document_id>")
def document_api_page(document_id):
    document = _get_dao().get_document(document_id)
    if document:
        return jsonify(document)
    else:
        return _as_json("Document with ID {document_id} not found!"), 404


@API_BLUEPRINT.route("/documents", methods=["POST"])
@accept("application/json")
def add_document_api_json():
    json_data = None
    if request.json:
        json_data = request.json.get("document_text", None)

    if json_data:
        inserted_document = _get_dao().insert_document(json_data)
        return jsonify({ID_FIELD: str(inserted_document.inserted_id)}), 201
    else:
        return _as_json("Document must have text!"), 400


@API_BLUEPRINT.route("/documents", methods=["POST"])
@add_document_api_json.support("application/x-www-form-urlencoded", "multipart/form-data", "text/html")
def add_document_api_form():
    form_data = None
    if request.form:
        form_data = request.form.get("document_text", None)

    if form_data:
        inserted_document = _get_dao().insert_document(form_data)
        return redirect(f"/documents/{inserted_document.inserted_id}", code=302)
    else:
        return "Document must have text!", 400


def _as_json(message: str) -> str:
    return jsonify({"message": message})


def _get_dao() -> ApplicationDao:
    return current_app.config["DB"]
