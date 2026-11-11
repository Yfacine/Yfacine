"""Generate the profile's repository cards as reproducible, self-contained SVGs."""
from html import escape
from pathlib import Path
from base64 import b64encode

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "cards" / "v0.1"
COVERS = ROOT / "assets" / "covers" / "v0.1"
# slug, sequence/label, title, two description lines, footer, illustration
CARDS = [
    ("Craft-FIRE", "01 / FIRE PROTECTION", "Craft-FIRE", "AutoCAD 소방설비 설계", "재현 후보", "재현 후보 · 구현 전", "fire"),
    ("Craft-DreamPlus", "02 / CAD AUTOMATION", "Craft-DreamPlus", "다중 플롯과 XCLIP", "반복 작업 재현 후보", "재현 후보 · 구현 전", "drawing"),
    ("Craft-PyroSim", "03 / FIRE & SMOKE", "Craft-PyroSim", "3D 화재·연기 모델과", "FDS 해석 입력 준비", "재현 후보 · 구현 전", "pyrosim"),
    ("Craft-Pathfinder", "04 / PEDESTRIAN FLOW", "Craft-Pathfinder", "보행자 이동과", "피난 시나리오 비교", "재현 후보 · 구현 전", "pathfinder"),
    ("Craft-Simulex", "05 / EVACUATION", "Craft-Simulex", "층별 피난 경로와", "대피 시간 분석", "재현 후보 · 구현 전", "route"),
    ("Craft-Contam", "06 / AIR QUALITY", "Craft-Contam", "구역 간 공기 흐름과", "오염물 이동 분석", "재현 후보 · 구현 전", "contam"),
    ("Craft-Ventus", "07 / VENTILATION", "Craft-Ventus", "환기·제연 모델링과", "풍량·차압 분석", "재현 후보 · 구현 전", "ventus"),
    ("Craft-Pipenet", "08 / PIPE NETWORK", "Craft-Pipenet", "배관망 구성과", "유량·압력 해석", "재현 후보 · 구현 전", "pipenet"),
    ("Craft-AutoCAD", "09 / CAD WORKFLOW", "Craft-AutoCAD", "도면 작성·편집과", "반복 작업", "재현 후보 · 구현 전", "cad"),
    ("Craft-Vehicle-Tracking", "10 / VEHICLE TRACKING", "Craft-Vehicle Tracking", "차량 회전 궤적과", "통과 공간 검토", "재현 후보 · 구현 전", "vehicle"),
    ("PASS_AI-FLY", "11 / LEARNING", "PASS_AI-FLY", "Simulex·Contam", "학습 주제", "소개 문서만 공개", "fly"),
    ("PASS_AI-MCP", "12 / INTEGRATION", "PASS_AI-MCP", "공개 저장소", "프로젝트 안내", "소개 문서만 공개", "mcp"),
    ("Asta-Profile", "13 / DESIGN", "Asta-Profile", "프로필 시안 30종", "저장소 삽화 13종", "디자인 자료 · 이미지 공개", "asta"),
]

# 공개 접근이 확인되면 해당 항목을 제거하고 README 링크를 복구한다.
UNLINKED = {
    "Craft-FIRE", "Craft-DreamPlus", "Craft-PyroSim", "Craft-Pathfinder",
    "Craft-Simulex", "Craft-Contam", "Craft-Ventus", "Craft-Pipenet",
    "Craft-AutoCAD", "Craft-Vehicle-Tracking",
}

def render(row):
    slug, label, title, line1, line2, status, art = row
    title_size = 48 if len(title) <= 17 else (39 if len(title) <= 23 else 31)
    cta = "공개 주소 확인 중" if slug in UNLINKED else "저장소 보기 ↗"
    art_data = b64encode((ROOT / "assets" / "card-illustrations" / "v0.1" / f"{art}.jpg").read_bytes()).decode("ascii")
    # The content is clipped to the card, while the canvas margins stay transparent.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="744" height="298" viewBox="0 0 744 298" role="img" aria-label="{escape(title)} · {escape(status)}">
<defs><clipPath id="frame"><rect x="12" y="0" width="720" height="276"/></clipPath><linearGradient id="textfade"><stop offset="0" stop-color="#fff"/><stop offset=".78" stop-color="#fff" stop-opacity=".97"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<g clip-path="url(#frame)"><rect x="12" y="0" width="720" height="276" fill="#f5f5f5"/>
<image x="12" y="0" width="720" height="226" preserveAspectRatio="xMaxYMax meet" href="data:image/jpeg;base64,{art_data}"/>
<rect x="12" y="0" width="500" height="226" fill="url(#textfade)"/>
<rect x="12.5" y=".5" width="719" height="275" fill="none" stroke="#a5a5a5"/>
<g font-family="Arial, 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif" fill="#151515">
<text x="38" y="44" font-family="monospace" font-weight="700" font-size="17" letter-spacing="1">{escape(label)}</text>
<text x="38" y="101" font-size="{title_size}" font-weight="700" letter-spacing="-1.5">{escape(title)}</text>
<text x="38" y="145" font-size="21">{escape(line1)}</text><text x="38" y="174" font-size="21">{escape(line2)}</text></g>
<rect x="13" y="226" width="718" height="49" fill="#202020"/>
<g fill="#fff" font-family="Arial, 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif" font-weight="700" font-size="19"><text x="38" y="257">{escape(status)}</text><text x="704" y="257" text-anchor="end">{cta}</text></g></g></svg>\n'''

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    COVERS.mkdir(parents=True, exist_ok=True)
    for row in CARDS:
        card = render(row)
        (OUT / f"{row[0]}.svg").write_text(card, encoding="utf-8", newline="\n")
        cover = card.replace("저장소 보기 ↗", "YFACINE").replace("공개 주소 확인 중", "YFACINE")
        (COVERS / f"{row[0]}.svg").write_text(cover, encoding="utf-8", newline="\n")
    print(f"Generated {len(CARDS)} cards and covers in {OUT} and {COVERS}")
