"""Deterministic tool for an AI agent. Python 3 standard library only.
All data is fictional. This script checks constraints; it is not an LLM agent.
"""
import argparse
import csv
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def evaluate(attendees=None, budget=None):
    request = json.loads((ROOT / 'data/request.json').read_text())
    policy = json.loads((ROOT / 'data/policy.json').read_text())
    count = request['attendees'] if attendees is None else attendees
    limit = Decimal(str(request['budget_usd'] if budget is None else budget))
    if count <= 0 or not limit.is_finite() or limit < 0:
        raise ValueError('Attendees must be positive and budget must be finite and nonnegative.')
    options = []
    with (ROOT / 'data/rooms.csv').open(newline='') as f:
        rooms = list(csv.DictReader(f))
    for room in rooms:
        for refreshments in (True, False):
            if not refreshments and not policy['refreshments_optional']:
                continue
            materials = count * Decimal(str(policy['materials_per_person_usd']))
            drinks = count * Decimal(str(policy['refreshments_per_person_usd'])) if refreshments else Decimal(0)
            total = Decimal(room['room_fee_usd']) + materials + drinks
            failures = []
            if count > int(room['capacity']):
                failures.append('capacity')
            if request['needs_projector'] and room['projector'] != 'yes':
                failures.append('projector')
            if request['needs_step_free'] and room['step_free'] != 'yes':
                failures.append('step_free_access')
            if total > limit:
                failures.append('budget')
            options.append(dict(room=room['room'], refreshments=refreshments,
                                total_usd=float(total), feasible=not failures,
                                failed_constraints=failures))
    return dict(attendees=count, budget_usd=float(limit),
                feasible_options=[o for o in options if o['feasible']],
                checked_options=options, booking_status=policy['booking_status'],
                sources=['data/request.json', 'data/rooms.csv', 'data/policy.json'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--attendees', type=int)
    parser.add_argument('--budget', type=Decimal)
    args = parser.parse_args()
    try:
        print(json.dumps(evaluate(args.attendees, args.budget), indent=2))
    except ValueError as exc:
        parser.error(str(exc))
