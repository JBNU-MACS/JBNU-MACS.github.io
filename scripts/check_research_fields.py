#!/usr/bin/env python3
"""Validate research-field references and ko/en publication parity (stdlib only)."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate():
    registry = json.loads((ROOT / 'data/research_fields.json').read_text())
    ids = {field['id'] for field in registry}
    assert len(ids) == len(registry), 'Duplicate research field ID'
    by_language = {}
    for language in ('ko', 'en'):
        for field in registry:
            page = ROOT / 'content' / language / field['path'] / 'index.md'
            match = re.search(r'^research_field: (.+)$', page.read_text().split('---', 2)[1], re.M)
            assert match and match[1] == field['id'], f'{page}: incorrect research_field'
        publications = {}
        for page in sorted((ROOT / 'content' / language / 'publication').glob('*/index.md')):
            metadata = page.read_text().split('---', 2)[1]
            match = re.search(r'^research_fields: (\[.*\])$', metadata, re.M)
            assert match, f'{page}: add research_fields as a JSON-style inline array'
            fields = json.loads(match[1])
            assert fields and len(fields) == len(set(fields)), f'{page}: empty or repeated fields'
            assert set(fields) <= ids, f'{page}: unknown field IDs {set(fields) - ids}'
            number = page.parent.name.split('-', 1)[0]
            assert number not in publications, f'{page}: duplicate publication number {number}'
            publications[number] = set(fields)
        assert publications, f'No {language} publications found'
        by_language[language] = publications
    assert by_language['ko'] == by_language['en'], 'Korean and English classifications differ'
    counts = Counter(field for fields in by_language['ko'].values() for field in fields)
    print(f"Validated {len(by_language['ko'])} publications in each language and {len(ids)} fields.")
    for field in registry:
        print(f"{field['id']}: {counts[field['id']]}")


if __name__ == '__main__':
    try:
        validate()
    except (AssertionError, ValueError, KeyError, OSError) as error:
        print(f'Research field validation failed: {error}', file=sys.stderr)
        sys.exit(1)
