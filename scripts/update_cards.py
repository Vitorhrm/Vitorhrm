"""Build profile cards from public GitHub data using only the standard library."""

import json
import os
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

USER = "Vitorhrm"
ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ["spring-docker-app", "MAC-Fabricante", "SADtrab", "Agrosense", "Mordix"]
COLORS = ["#b794ff", "#48d7ee", "#f5b86f", "#75dfb1", "#f678a5", "#94a8ff"]


def api(path):
    headers = {"User-Agent": "Vitorhrm-profile", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request("https://api.github.com" + path, headers=headers), timeout=30) as response:
        return json.load(response)


def card(title, subtitle, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="450" height="230" viewBox="0 0 450 230" role="img" aria-label="{escape(title)}">
<rect x="1" y="1" width="448" height="228" rx="16" fill="#11111f" stroke="#3a3555"/>
<text x="24" y="34" fill="#c7afff" font-family="sans-serif" font-size="18" font-weight="700">{escape(title)}</text>
<text x="24" y="56" fill="#aaa8bf" font-family="sans-serif" font-size="11">{escape(subtitle)}</text>
{body}</svg>'''


def main():
    user = api(f"/users/{USER}")
    repos = api(f"/users/{USER}/repos?per_page=100&type=owner")
    owned = [repo for repo in repos if not repo["fork"] and repo["name"] != USER]
    stars = sum(repo["stargazers_count"] for repo in owned)
    date = datetime.now(timezone.utc).strftime("%d/%m/%Y UTC")
    rows = [("Repositórios públicos autorais", len(owned)), ("Projetos selecionados", len(PROJECTS)),
            ("Estrelas nesses repositórios", stars), ("Pessoas acompanhando o perfil", user["followers"])]
    body = "".join(f'<text x="24" y="{89 + index * 29}" fill="#dedce9" font-family="sans-serif" font-size="13">{label}</text><text x="414" y="{89 + index * 29}" text-anchor="end" fill="#75dfb1" font-family="monospace" font-size="18">{value}</text>' for index, (label, value) in enumerate(rows))
    body += f'<text x="24" y="211" fill="#8b88a5" font-family="sans-serif" font-size="10">Dados públicos · atualizado em {date}</text>'
    target = ROOT / "assets"
    target.mkdir(exist_ok=True)
    (target / "stats.svg").write_text(card("Meu GitHub em números", "Atividade pública, sem incluir forks ou o README do perfil", body), encoding="utf-8")

    languages = Counter()
    for name in PROJECTS:
        languages.update(api(f"/repos/{USER}/{name}/languages"))
    top = languages.most_common(5)
    other = sum(languages.values()) - sum(value for _, value in top)
    if other:
        top.append(("Outras", other))
    total = sum(languages.values())
    bar = ""
    x = 24
    for index, (_, value) in enumerate(top):
        width = 402 * value / total
        bar += f'<rect x="{x:.2f}" y="77" width="{width:.2f}" height="12" fill="{COLORS[index]}"/>'
        x += width
    for index, (language, value) in enumerate(top):
        x = 24 + (index % 2) * 204
        y = 119 + (index // 2) * 26
        bar += f'<circle cx="{x + 4}" cy="{y - 4}" r="4" fill="{COLORS[index]}"/><text x="{x + 15}" y="{y}" fill="#dedce9" font-family="sans-serif" font-size="12">{escape(language)} · {100 * value / total:.1f}%</text>'
    bar += '<text x="24" y="211" fill="#8b88a5" font-family="sans-serif" font-size="10">Bytes de código dos 5 projetos · dados da API do GitHub</text>'
    (target / "languages.svg").write_text(card("Linguagens nos projetos", "Distribuição por bytes de código, segundo o GitHub", bar), encoding="utf-8")


if __name__ == "__main__":
    main()
