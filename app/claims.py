"""Claims routes. Every query here is parameterized. Keep it that way."""
from flask import Blueprint, abort, jsonify

from .db import get_db

bp = Blueprint("claims", __name__)


@bp.get("/health")
def health():
    return jsonify(status="ok")


@bp.get("/claims/<claim_id>")
def get_claim(claim_id):
    row = get_db().execute(
        "SELECT claim_id, member_id, status, amount_usd FROM claims WHERE claim_id = ?",
        (claim_id,),
    ).fetchone()
    if row is None:
        abort(404)
    return jsonify(dict(row))


@bp.get("/members/<member_id>/claims")
def member_claims(member_id):
    rows = get_db().execute(
        "SELECT claim_id, status, amount_usd FROM claims WHERE member_id = ?",
        (member_id,),
    ).fetchall()
    return jsonify([dict(r) for r in rows])
