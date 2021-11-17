from flask import Blueprint, jsonify, make_response, Response, request
from flask_api import status
from ..db import db_sessions, db_roster


roster = Blueprint("/api/roster", __name__)

@roster.route("/api/roster", methods=["POST"])
def add_char_to_roster():
    pass