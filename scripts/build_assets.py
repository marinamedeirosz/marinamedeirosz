"""Gera as imagens SVG do README (versões clara e escura).

Uso: python scripts/build_assets.py
Saída: assets/*.svg
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": {
        "card": "#151b23", "stroke": "#30363d", "title": "#f0f6fc", "body": "#9198a1",
        "accent": "#2dd4bf", "pill_text": "#d1d7e0", "pill_stroke": "#3d444d", "muted": "#6e7681",
    },
    "light": {
        "card": "#ffffff", "stroke": "#d1d9e0", "title": "#1f2328", "body": "#59636e",
        "accent": "#0f766e", "pill_text": "#1f2328", "pill_stroke": "#d1d9e0", "muted": "#818b98",
    },
}

# ------------------------------------------------------------------ texto


def char_w(c, size):
    if c in "il.,'|!:;ijlt ()[]f":
        k = 0.30
    elif c in "mwMW":
        k = 0.86
    elif c.isupper():
        k = 0.66
    elif c.isdigit():
        k = 0.56
    else:
        k = 0.53
    return k * size


def text_w(s, size):
    return sum(char_w(c, size) for c in s)


def wrap(text, size, max_w):
    lines, cur = [], ""
    for word in text.split():
        cand = f"{cur} {word}".strip()
        if text_w(cand, size) <= max_w:
            cur = cand
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(label)}">\n{body}\n</svg>\n')


def pills(items, x, y, t):
    out, cx = [], x
    for it in items:
        w = len(it) * 7.6 + 22
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.1f}" height="28" rx="7" fill="none" '
                   f'stroke="{t["pill_stroke"]}"/>')
        out.append(f'<text x="{cx + w / 2:.1f}" y="{y + 18.5}" text-anchor="middle" font-family="{MONO}" '
                   f'font-size="12.5" fill="{t["pill_text"]}">{escape(it)}</text>')
        cx += w + 8
    return "\n".join(out)


def wave(x, y, w, t, opacity=0.55, amp=5, waves=3):
    """Linha de onda discreta, o motivo visual do perfil."""
    seg = w / (waves * 2)
    d = f"M {x} {y}"
    for i in range(waves * 2):
        dy = -amp if i % 2 == 0 else amp
        d += f" q {seg / 2:.1f} {dy} {seg:.1f} 0"
    return (f'<path d="{d}" fill="none" stroke="{t["accent"]}" stroke-width="2" '
            f'stroke-linecap="round" opacity="{opacity}"/>')


def arrow(x, y, t):
    return (f'<path d="M {x} {y + 12} L {x + 12} {y} M {x + 3} {y} L {x + 12} {y} L {x + 12} {y + 9}" '
            f'fill="none" stroke="{t["accent"]}" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def eyebrow(x, y, strong, rest, t):
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="11.5" letter-spacing="1.2">'
            f'<tspan font-weight="700" fill="{t["accent"]}">{escape(strong)}</tspan>'
            f'<tspan fill="{t["muted"]}">{escape(rest)}</tspan></text>')


# ------------------------------------------------------------------ peças


def header(t):
    w, h = 880, 210
    body = [
        f'<text x="2" y="44" font-family="{MONO}" font-size="13" letter-spacing="2" font-weight="700" '
        f'fill="{t["accent"]}">FULL STACK DEVELOPER · MACEIÓ, BRAZIL</text>',
        f'<text x="0" y="106" font-family="{SANS}" font-size="54" font-weight="700" '
        f'fill="{t["title"]}">Marina Medeiros</text>',
        f'<text x="2" y="146" font-family="{SANS}" font-size="19" fill="{t["body"]}">Software built end to end, '
        f'from the database to the app in people\'s hands,</text>',
        f'<text x="2" y="174" font-family="{SANS}" font-size="19" fill="{t["body"]}">for the Government of '
        f'Alagoas, SaaS products, and social impact projects.</text>',
        wave(660, 70, 200, t, 0.9, 7, 3),
        wave(690, 96, 170, t, 0.55, 6, 3),
        wave(720, 120, 140, t, 0.3, 5, 3),
    ]
    return svg(w, h, "\n".join(body),
               "Marina Medeiros, full stack developer in Maceió, Brazil. Software built end to end, from the "
               "database to the app in people's hands.")


CARD_W, CARD_H = 420, 318
# O GitHub ignora margens em CSS, então cada card leva uma borda transparente de PAD px em todos os lados.
# Entre dois cards o espaço fica PAD + PAD (mais o espaço de texto que o navegador já coloca), igual nos dois eixos.
PAD = 8


def padded(w, h, body, label):
    return svg(w + 2 * PAD, h + 2 * PAD, f'<g transform="translate({PAD} {PAD})">\n{body}\n</g>', label)


def card(c, t):
    pad = 26
    body = [f'<rect x="1" y="1" width="{CARD_W - 2}" height="{CARD_H - 2}" rx="14" fill="{t["card"]}" '
            f'stroke="{t["stroke"]}"/>',
            eyebrow(pad, 44, c["eyebrow"][0], c["eyebrow"][1], t),
            wave(CARD_W - 96, 40, 60, t, 0.5, 3, 2)]
    if c.get("link"):
        body.append(arrow(CARD_W - 32, 30, t))
    body.append(f'<text x="{pad}" y="96" font-family="{SANS}" font-size="27" font-weight="700" '
                f'fill="{t["title"]}">{escape(c["title"])}</text>')
    for i, line in enumerate(wrap(c["desc"], 15.5, CARD_W - 2 * pad)):
        body.append(f'<text x="{pad}" y="{132 + i * 23}" font-family="{SANS}" font-size="15.5" '
                    f'fill="{t["body"]}">{escape(line)}</text>')
    body.append(pills(c["pills"], pad, CARD_H - 54, t))
    return padded(CARD_W, CARD_H, "\n".join(body), c["title"])


def wide(c, t):
    w, h, pad = 880, 212, 28
    body = [f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t["card"]}" '
            f'stroke="{t["stroke"]}"/>',
            eyebrow(pad, 44, c["eyebrow"][0], c["eyebrow"][1], t),
            arrow(w - 36, 30, t),
            f'<text x="{pad}" y="92" font-family="{SANS}" font-size="27" font-weight="700" '
            f'fill="{t["title"]}">{escape(c["title"])}</text>']
    for i, line in enumerate(wrap(c["desc"], 15.5, 560)):
        body.append(f'<text x="{pad}" y="{124 + i * 23}" font-family="{SANS}" font-size="15.5" '
                    f'fill="{t["body"]}">{escape(line)}</text>')
    # mapa estilizado: pontos de coleta de tamanhos diferentes
    for cx, cy, r, o in [(690, 110, 22, 0.25), (735, 80, 12, 0.5), (770, 125, 16, 0.35),
                         (815, 92, 9, 0.7), (720, 140, 7, 0.6), (790, 60, 6, 0.8)]:
        body.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{t["accent"]}" opacity="{o}"/>')
    body.append(pills(c["pills"], pad, h - 50, t))
    return padded(w, h, "\n".join(body), c["title"])


def icon(kind, t):
    s = 36
    base = f'<rect x="1" y="1" width="{s - 2}" height="{s - 2}" rx="9" fill="{t["card"]}" stroke="{t["stroke"]}"/>'
    if kind == "linkedin":
        g = (f'<text x="18" y="24" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="700" '
             f'fill="{t["accent"]}">in</text>')
    else:
        g = (f'<rect x="9" y="11" width="18" height="14" rx="2.5" fill="none" stroke="{t["accent"]}" '
             f'stroke-width="1.8"/><path d="M 10 13 L 18 19 L 26 13" fill="none" stroke="{t["accent"]}" '
             f'stroke-width="1.8" stroke-linejoin="round"/>')
    return svg(s, s, base + g, kind)


# ------------------------------------------------------------------ conteúdo

CARDS = {
    "gov": {
        "eyebrow": ("GOVERNMENT", " · TEAM PLATFORM"),
        "title": "Government data platform",
        "desc": "The State of Alagoas's data and decision-support platform: 50+ solutions in production, about "
                "250 users and 40+ native dashboards. I work on validated imports and the APIs other agencies "
                "use to send data.",
        "pills": ["React", "Node.js", "PostgreSQL", "Keycloak"],
    },
    "docs": {
        "eyebrow": ("SAAS", " · DIGITAL SIGNATURES"),
        "title": "Documents and signatures",
        "desc": "Document management with qualified ICP-Brasil signatures, batch signing, public signature verification, "
                "a local Windows signer written in Rust and full-text search with OCR.",
        "pills": ["React", "Fastify", "Java", "Rust"],
    },
    "offline": {
        "eyebrow": ("MOBILE", " · OFFLINE FIRST"),
        "title": "Apps that work offline",
        "desc": "Time tracking with facial recognition and kiosks that sign every request, plus field service apps on the Play "
                "Store and App Store with checklists, photos, signatures and offline sync.",
        "pills": ["React Native", "Expo", "Python", "NestJS"],
    },
    "ai": {
        "eyebrow": ("AI", " · MULTI-TENANT SAAS"),
        "title": "SaaS and AI agents",
        "desc": "Project and service management with row-level tenant isolation and plan-based features, and "
                "MCP servers that let agents in n8n and Gemini work with real systems.",
        "pills": ["NestJS", "Next.js", "MCP", "Oracle"],
    },
    "acolhe": {
        "eyebrow": ("IFAL", " · OUTREACH · THESIS"),
        "title": "Acolhe.AL",
        "desc": "Helps short-term shelters for people experiencing homelessness manage residents, multi-step intake and attendance, replacing "
                "paper records, spreadsheets and WhatsApp. Running in production.",
        "pills": ["Laravel", "React", "Inertia.js", "PostgreSQL"],
    },
    "mariscar": {
        "eyebrow": ("IFAL", " · OUTREACH"),
        "title": "Mariscar com Dignidade",
        "desc": "Records and analyzes artisanal shellfish gathering: an offline-first app for the field, an API "
                "built with privacy (LGPD) in mind and a dashboard for researchers.",
        "pills": ["Flutter", "Django", "Next.js", "PostgreSQL"],
    },
}

PROJECT = {
    "eyebrow": ("PUBLIC PROJECT", " · OPEN SOURCE"),
    "title": "mapa-cc-mhn",
    "desc": "Turns a crustacean (carcinological) collection spreadsheet into interactive maps, filters and statistics, "
            "with no programming required.",
    "pills": ["React", "Leaflet", "TanStack Table", "Vitest"],
}

for name, t in THEMES.items():
    (OUT / f"header-{name}.svg").write_text(header(t), encoding="utf-8")
    for key, c in CARDS.items():
        (OUT / f"card-{key}-{name}.svg").write_text(card(c, t), encoding="utf-8")
    (OUT / f"project-mapa-cc-mhn-{name}.svg").write_text(wide(PROJECT, t), encoding="utf-8")
    for k in ("linkedin", "email"):
        (OUT / f"link-{k}-{name}.svg").write_text(icon(k, t), encoding="utf-8")

print("ok:", len(list(OUT.glob("*.svg"))), "svgs em", OUT)
