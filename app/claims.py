"""Claims routes. Every query here is parameterized. Keep it that way."""
from flask import Blueprint, abort, jsonify, request

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


# DEMO PAYLOAD: "Small, harmless change"
# Intentionally vulnerable (SQL injection via string formatting) so CodeQL
# flags it on the pull request and Copilot Autofix can propose a fix.
# Never merge this. The ruleset should stop you anyway.
@bp.get("/claims/search")
def search_claims():
    status = request.args.get("status", "")
    query = f"SELECT claim_id, member_id, status, amount_usd FROM claims WHERE status = '{status}'"
    rows = get_db().execute(query).fetchall()
    return jsonify([dict(r) for r in rows])
