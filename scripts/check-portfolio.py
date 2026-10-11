#!/usr/bin/env python3
"""Validate the static published-app portfolio locally; no CI/network required."""
from __future__ import annotations
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = json.loads((ROOT / 'data/released-apps.json').read_text())['apps']

class Portfolio(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.links = []
        self.images = []
        self.headings = 0
        self.canonicals = []

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == 'article' and 'data-app-store-id' in attrs:
            self.cards.append((attrs.get('id'), attrs['data-app-store-id']))
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'h1':
            self.headings += 1
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href'))

p = Portfolio()
p.feed((ROOT / 'index.html').read_text(encoding='utf-8'))
expected = [(app['slug'], str(app['app_store_id'])) for app in EXPECTED]
assert len(expected) == len(set(expected)), 'Duplicate published app in release manifest'
assert p.cards == expected, f'Catalog differs from verified public apps: {p.cards!r} vs {expected!r}'
assert p.headings == 1
assert p.canonicals == ['https://git-ksk.github.io/']
assert len(p.images) == len(expected) * 3
for image in p.images:
    assert image.get('alt'), f'Missing accessible alt: {image}'
    target = ROOT / image['src']
    assert target.is_file() and target.stat().st_size > 1000, f'Missing/broken local image: {target}'
for slug, identifier in expected:
    assert f'https://apps.apple.com/jp/app/id{identifier}' in p.links, f'Missing Apple listing: {slug}'
    for name in ['icon.jpg', 'screen-01.jpg', 'screen-02.jpg']:
        assert (ROOT / 'assets' / 'images' / 'store' / slug / name).is_file()
assert '/karupic/photo-under-500kb/' in p.links, 'Missing KaruPic SEO guide link'
print(f'Published app portfolio PASS: {len(expected)} live apps, {len(p.images)} official images, {len(expected)} Store links')
