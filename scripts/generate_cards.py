"""Generate the profile's repository cards as reproducible, self-contained SVGs."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "cards" / "v1"
# slug, sequence/label, title, two description lines, footer, illustration
CARDS = [
    ("CRAFT-FIRE", "01 / FIRE PROTECTION", "CRAFT-FIRE", "AutoCAD 소방설비 설계", "재현 후보", "재현 후보 · 구현 전", "building"),
    ("CRAFT-DreamPlus", "02 / CAD AUTOMATION", "CRAFT-DreamPlus", "다중 플롯과 XCLIP", "반복 작업 재현 후보", "재현 후보 · 구현 전", "drawing"),
    ("CRAFT-PyroSim", "03 / FIRE & SMOKE", "CRAFT-PyroSim", "3D 화재·연기 모델과", "FDS 해석 입력 준비", "재현 후보 · 구현 전", "building"),
    ("CRAFT-Pathfinder", "04 / PEDESTRIAN FLOW", "CRAFT-Pathfinder", "보행자 이동과", "피난 시나리오 비교", "재현 후보 · 구현 전", "route"),
    ("CRAFT-Simulex", "05 / EVACUATION", "CRAFT-Simulex", "층별 피난 경로와", "대피 시간 분석", "재현 후보 · 구현 전", "route"),
    ("CRAFT-Contam", "06 / AIR QUALITY", "CRAFT-Contam", "구역 간 공기 흐름과", "오염물 이동 분석", "재현 후보 · 구현 전", "building"),
    ("CRAFT-Ventus", "07 / VENTILATION", "CRAFT-Ventus", "환기·제연 모델링과", "풍량·차압 분석", "재현 후보 · 구현 전", "network"),
    ("CRAFT-Pipenet", "08 / PIPE NETWORK", "CRAFT-Pipenet", "배관망 구성과", "유량·압력 해석", "재현 후보 · 구현 전", "network"),
    ("CRAFT-AutoCAD", "09 / CAD WORKFLOW", "CRAFT-AutoCAD", "도면 작성·편집과", "반복 작업", "재현 후보 · 구현 전", "drawing"),
    ("CRAFT-Vehicle-Tracking", "10 / VEHICLE TRACKING", "CRAFT-Vehicle-Tracking", "차량 회전 궤적과", "통과 공간 검토", "재현 후보 · 구현 전", "route"),
    ("PASS_AI-FLY", "11 / LEARNING", "PASS_AI-FLY", "Simulex·Contam", "학습 주제", "소개 문서만 공개", "building"),
    ("PASS_AI-MCP", "12 / INTEGRATION", "PASS_AI-MCP", "공개 저장소", "프로젝트 안내", "소개 문서만 공개", "network"),
    ("Asta-Profile", "13 / DESIGN", "Asta-Profile", "아스타 프로필 이미지", "흑백·성장·픽셀 시안 30종", "디자인 자료 · 이미지 공개", "drawing"),
]

ART = {
    "building": '<path d="M382 165 515 92 698 141 566 216Z M382 165v-46l133-71 183 46v47 M382 119l184 50 132-75 M566 169v47 M421 140v45m40-66v82m42-104v115m41-94v91m45-52v47m40-71v45m38-65v42"/><path d="m406 126 133 36m-89-59 135 34m-91-57 132 33m-91-57 132 33"/>',
    "drawing": '<path d="M400 39h263v159H400z M422 58h217v117H422z M442 76h75v43h-75z M537 76h81v43h-81z M442 137h176M466 137v38m73-38v38m52-38v38"/><path d="M385 53V26h27m252 0h25v27M385 183v28h27m252 0h25v-28 M404 222h261 M404 217v10m261-10v10"/>',
    "route": '<path d="M407 50h100v37h74V50h93v138h-65v-37h-99v37H407z M435 50v68h75m71-31v40h93 M510 151v-33m99 33v-24"/><path stroke-dasharray="7 6" d="M424 171q41-45 75-39t63-19q28-24 77-25"/><path d="m628 82 14 6-7 13"/>',
    "network": '<path d="M409 64h109v53h89V67h58 M409 64v105h94v-52m0 52h124v-52h38 M457 64v53m0 52v26h153"/><circle cx="409" cy="64" r="7"/><circle cx="518" cy="117" r="7"/><circle cx="607" cy="67" r="7"/><circle cx="503" cy="169" r="7"/><circle cx="627" cy="169" r="7"/><circle cx="665" cy="117" r="7"/>',
}

def render(row):
    slug, label, title, line1, line2, status, art = row
    title_size = 48 if len(title) <= 17 else (39 if len(title) <= 20 else 31)
    # The content is clipped to the card, while the canvas margins stay transparent.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="744" height="298" viewBox="0 0 744 298" role="img" aria-label="{escape(title)} · {escape(status)}">
<defs><clipPath id="frame"><rect x="12" y="0" width="720" height="276"/></clipPath><linearGradient id="fade"><stop stop-color="#f5f5f5"/><stop offset="1" stop-color="#fff"/></linearGradient></defs>
<g clip-path="url(#frame)"><rect x="12" y="0" width="720" height="276" fill="#f5f5f5"/>
<g fill="none" stroke="#b6b6b6" stroke-width="1.6" stroke-linecap="square" stroke-linejoin="round">{ART[art]}</g>
<path d="M350 0h62v226h-62z" fill="url(#fade)" opacity=".85"/>
<rect x="12.5" y=".5" width="719" height="275" fill="none" stroke="#a5a5a5"/>
<g font-family="Arial, 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif" fill="#151515">
<text x="38" y="44" font-family="monospace" font-weight="700" font-size="17" letter-spacing="1">{escape(label)}</text>
<text x="38" y="101" font-size="{title_size}" font-weight="700" letter-spacing="-1.5">{escape(title)}</text>
<text x="38" y="145" font-size="21">{escape(line1)}</text><text x="38" y="174" font-size="21">{escape(line2)}</text></g>
<rect x="13" y="226" width="718" height="49" fill="#202020"/>
<g fill="#fff" font-family="Arial, 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif" font-weight="700" font-size="19"><text x="38" y="257">{escape(status)}</text><text x="704" y="257" text-anchor="end">저장소 보기 ↗</text></g></g></svg>\n'''

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for row in CARDS:
        (OUT / f"{row[0]}.svg").write_text(render(row), encoding="utf-8", newline="\n")
    print(f"Generated {len(CARDS)} cards in {OUT}")
