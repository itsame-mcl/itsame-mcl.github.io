# /// script
# requires-python = ">=3.10"
# dependencies = ["reportlab>=4", "pyyaml>=6"]
# ///
"""Génère les CV en PDF (FR et EN) à partir des données du site (data/cv/*.yaml).

Usage, depuis la racine du dépôt :
    uv run scripts/build_cv_pdf.py

Les PDF sont écrits dans static/files/ puis servis par le site. Ils sont versionnés :
on les régénère après chaque modification des données du CV.
"""
import re
import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, KeepTogether, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'static' / 'files'
SITE = yaml.safe_load((ROOT / 'hugo.yaml').read_text(encoding='utf8'))
PARAMS = SITE['params']
BASE = SITE['baseURL'].rstrip('/')

ACCENT = colors.HexColor('#a23d19')
INK = colors.HexColor('#2d2218')
MUTED = colors.HexColor('#6a5848')
RULE = colors.HexColor('#e6d8c2')
PAPER_TINT = colors.HexColor('#fbf6ee')

MONTHS = {
    'fr': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
}
LABELS = {
    'fr': {'updated': 'Mis à jour en', 'page': 'Page'},
    'en': {'updated': 'Updated', 'page': 'Page'},
}

S = {
    'name': ParagraphStyle('name', fontName='Times-Bold', fontSize=25, leading=28, textColor=ACCENT),
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=INK, spaceBefore=1),
    'tag': ParagraphStyle('tag', fontName='Helvetica', fontSize=9.5, leading=13, textColor=MUTED, spaceBefore=2),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=12, textColor=INK, spaceBefore=4),
    'h': ParagraphStyle('h', fontName='Times-Bold', fontSize=13.5, leading=16, textColor=ACCENT, spaceBefore=6, spaceAfter=0),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, textColor=INK, alignment=TA_LEFT),
    'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=9.8, leading=12.5, textColor=INK),
    'when': ParagraphStyle('when', fontName='Helvetica', fontSize=9, leading=12.5, textColor=MUTED, alignment=2),
    'org': ParagraphStyle('org', fontName='Helvetica-Oblique', fontSize=9, leading=12, textColor=MUTED),
    'li': ParagraphStyle('li', fontName='Helvetica', fontSize=8.8, leading=11.4, textColor=INK, leftIndent=9, bulletIndent=0, spaceBefore=0.8),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.8, leading=11.4, textColor=INK),
}


def md(text: str) -> str:
    """Mini-Markdown (gras, italique, liens) vers le balisage de Paragraph de reportlab."""
    t = escape(str(text))
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" color="#a23d19">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', t)
    return t


def p(text, style='body'):
    return Paragraph(md(text), S[style])


def section(title):
    return [p(title, 'h'), HRFlowable(width='100%', thickness=0.8, color=RULE, spaceBefore=1, spaceAfter=4)]


def entry(role, org_line, when, summary=None, points=()):
    head = Table([[p(role, 'role'), p(when, 'when')]], colWidths=[None, 46 * mm])
    head.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                              ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    flow = [head, p(org_line, 'org')]
    if summary:
        flow.append(Spacer(1, 1.5))
        flow.append(p(summary, 'small'))
    for pt in points:
        flow.append(Paragraph(md(pt), S['li'], bulletText='•'))
    flow.append(Spacer(1, 3.5))
    return KeepTogether(flow[:4]) if len(flow) > 4 else KeepTogether(flow), flow[4:]


def first_sentence(text: str) -> str:
    """Première phrase d'un texte (le PDF est un résumé, le détail est sur le site)."""
    m = re.search(r'(?<=\S)\. (?=[A-ZÀ-Ý«])', text)
    return text[:m.start() + 1] if m else text


def build(lang: str):
    d = yaml.safe_load((ROOT / 'data' / 'cv' / f'{lang}.yaml').read_text(encoding='utf8'))
    ui, person = d['ui'], d['person']
    today = date.today()
    stamp = f"{LABELS[lang]['updated']} {MONTHS[lang][today.month - 1]} {today.year}"
    out = OUT / f'cv-maxence-lagalle-{lang}.pdf'

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(16 * mm, 10 * mm, f"{person['display']} · {stamp}")
        canvas.drawRightString(A4[0] - 16 * mm, 10 * mm, f"{BASE.replace('https://', '')} · {LABELS[lang]['page']} {doc.page}")
        canvas.setStrokeColor(RULE)
        canvas.line(16 * mm, 13.5 * mm, A4[0] - 16 * mm, 13.5 * mm)
        canvas.restoreState()

    doc = BaseDocTemplate(str(out), pagesize=A4, leftMargin=16 * mm, rightMargin=16 * mm, topMargin=13 * mm,
                          bottomMargin=16 * mm, title=f"{person['display']} · CV", author='Maxence Lagalle',
                          subject=person['title'], creator='scripts/build_cv_pdf.py')
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f', leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=footer)])

    story = [
        p(person['display'], 'name'),
        p(f"{person['title']}, {person['org']}", 'title'),
        p(person['tagline'], 'tag'),
        p(f"{PARAMS['email']} · [LinkedIn]({PARAMS['linkedin']}) · [GitHub]({PARAMS['github']}) · [{BASE.replace('https://', '')}]({BASE})", 'contact'),
        Spacer(1, 3),
    ]
    for para in person['summary']:
        story += [Spacer(1, 2.5), p(para)]

    story += section(ui['experience'])
    for e in d['experience']:
        when = f"{e['start']} – {e.get('end', ui['present'])}"
        head, rest = entry(e['role'], f"{e['org']}, {e['place']}", when, e.get('summary'), e.get('points') or [])
        story += [head] + rest
    story += section(ui['earlier'])
    for e in d['earlier']:
        head, rest = entry(e['role'], f"{e['org']}, {e['place']}", e['period'], e.get('summary'))
        story += [head] + rest

    story += section(ui['education'])
    for e in d['education']:
        story.append(Table([[p(f"**{e['name']}**, {e['org']}", 'small'), p(e['period'], 'when')]],
                           colWidths=[None, 30 * mm],
                           style=[('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                  ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))

    story += section(ui['certifications'])
    for c in d['certifications']:
        when = c.get('period') or ''
        story.append(Table([[p(c['name'], 'small'), p(when, 'when')]], colWidths=[None, 30 * mm],
                           style=[('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                  ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))

    story += section(ui['skills'])
    for s_ in d['skills']:
        story.append(p(f"**{s_['group']}.** {s_['items']}", 'small'))
        story.append(Spacer(1, 1.5))
    story += section(ui['languages'])
    story.append(p(' · '.join(d['languages']), 'small'))

    t = d['teaching']
    story += section(f"{ui['teaching']} · {ui['talks'].lower()}")
    for sec in t['sections']:
        for it in sec['items']:
            story.append(Paragraph(md(f"**{it['period']}.** {it['text']}"), S['li'], bulletText='•'))
    story.append(Spacer(1, 2))
    story.append(p(t['talks_intro'], 'small'))
    for it in t['talks']:
        story.append(Paragraph(md(f"**{it['period']}, {it['place']}.** {first_sentence(it['text'])}"), S['li'], bulletText='•'))

    doc.build(story)
    return out


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for lg in (sys.argv[1:] or ['fr', 'en']):
        print('écrit :', build(lg))
