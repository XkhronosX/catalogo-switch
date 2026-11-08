#!/usr/bin/env python3
"""
REGENERA HTML USANDO IMÁGENES LOCALES (carpeta images/)
Ejecutar DESPUÉS de download_covers.py y copiar la carpeta images/
"""

import json
from pathlib import Path

# ============================================================
PLACEHOLDER_SVGS = {
    'base': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="64" height="64"><rect x="2" y="3" width="20" height="18" rx="2"/><path d="M6 3v18M18 3v18M10 3v18"/></svg>',
    'dlc': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="64" height="64"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/></svg>',
    'update': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="64" height="64"><path d="M21 12a9 9 0 0 1-9 9c-2.5 0-4.8-.8-6.6-2.1"/><path d="M3 3v5h5"/></svg>',
    'xci': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="64" height="64"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M6 4v16M18 4v16M10 4v16"/></svg>',
}


def generate_html(games, total, d_count, e_count, nsp_count, xci_count, base_count, dlc_count, update_count):
    # Only include base games
    base_games = [g for g in games if g['category'] == 'base']
    games_sorted = sorted(base_games, key=lambda g: g['name'].lower())

    # Contar imágenes reales
    real_images = sum(1 for g in base_games if g.get('image'))
    total = len(base_games)
    d_count = sum(1 for g in base_games if g['drive'] == 'd')
    e_count = sum(1 for g in base_games if g['drive'] == 'e')
    nsp_count = sum(1 for g in base_games if g['type'] == 'nsp')
    xci_count = sum(1 for g in base_games if g['type'] == 'xci')
    base_count = len(base_games)
    dlc_count = 0
    update_count = 0

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catalogo Completo Nintendo Switch - {total} juegos</title>
    <style>
        :root {{
            --bg-primary: #0d1117;
            --bg-secondary: #161b22;
            --bg-tertiary: #21262d;
            --fg-primary: #e6edf3;
            --fg-secondary: #8b949e;
            --accent: #58a6ff;
            --accent-hover: #79b8ff;
            --border: #30363d;
            --success: #3fb950;
            --warning: #d29922;
            --danger: #f85149;
            --card-bg: #161b22;
            --input-bg: #0d1117;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            background: var(--bg-primary);
            color: var(--fg-primary);
            line-height: 1.6;
            min-height: 100vh;
        }}
        .container {{ max-width: 1600px; margin: 0 auto; padding: 24px; }}
        header {{
            text-align: center;
            padding: 32px 0;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
        }}
        h1 {{
            font-size: 2.5rem;
            font-weight: 600;
            background: linear-gradient(135deg, var(--accent), #a371f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .stats {{ display: flex; justify-content: center; gap: 16px; margin-top: 16px; flex-wrap: wrap; }}
        .stat {{ background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 8px; padding: 12px 20px; text-align: center; min-width: 100px; }}
        .stat-value {{ font-size: 1.75rem; font-weight: 700; color: var(--accent); }}
        .stat-label {{ font-size: 0.75rem; color: var(--fg-secondary); text-transform: uppercase; letter-spacing: 0.5px; }}
        .controls {{ display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; align-items: center; }}
        .search-box {{ flex: 1; min-width: 280px; position: relative; }}
        .search-box input {{ width: 100%; padding: 10px 14px 10px 40px; background: var(--input-bg); border: 1px solid var(--border); border-radius: 8px; color: var(--fg-primary); font-size: 0.95rem; transition: border-color 0.2s, box-shadow 0.2s; }}
        .search-box input:focus {{ outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15); }}
        .search-box svg {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--fg-secondary); width: 18px; height: 18px; }}
        .filters {{ display: flex; gap: 8px; flex-wrap: wrap; }}
        .filter-btn {{ padding: 6px 12px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 6px; color: var(--fg-secondary); font-size: 0.8rem; cursor: pointer; transition: all 0.2s; white-space: nowrap; }}
        .filter-btn:hover {{ border-color: var(--accent); color: var(--fg-primary); }}
        .filter-btn.active {{ background: var(--accent); border-color: var(--accent); color: var(--bg-primary); }}
        .view-toggle {{ display: flex; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }}
        .view-btn {{ padding: 6px 10px; background: transparent; border: none; color: var(--fg-secondary); cursor: pointer; transition: all 0.2s; }}
        .view-btn:hover {{ background: var(--bg-tertiary); color: var(--fg-primary); }}
        .view-btn.active {{ background: var(--accent); color: var(--bg-primary); }}
        .results-info {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding: 10px 14px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 8px; font-size: 0.8rem; color: var(--fg-secondary); flex-wrap: wrap; gap: 8px; }}

        .game-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }}
        .game-grid.list-view {{ grid-template-columns: 1fr; }}
        .game-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s; display: flex; flex-direction: column; }}
        .game-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 32px rgba(0,0,0,0.4); border-color: var(--accent); }}
        .game-card.list-view {{ flex-direction: row; align-items: stretch; padding: 0; }}
        .game-card.list-view .game-image {{ width: 160px; height: auto; min-height: 200px; border-radius: 0; border-right: 1px solid var(--border); }}
        .game-image {{ width: 100%; height: 180px; object-fit: cover; background: var(--bg-tertiary); }}
        .game-image-placeholder {{ width: 100%; height: 180px; display: flex; align-items: center; justify-content: center; background: var(--bg-tertiary); color: var(--fg-secondary); font-size: 2rem; }}
        .game-card.list-view .game-image-placeholder {{ width: 160px; height: auto; min-height: 200px; }}
        .game-content {{ padding: 14px; flex: 1; display: flex; flex-direction: column; }}
        .game-header {{ display: flex; align-items: flex-start; gap: 10px; margin-bottom: 8px; }}
        .game-icon {{ width: 36px; height: 36px; border-radius: 6px; background: linear-gradient(135deg, var(--accent), #a371f7); display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }}
        .game-icon.xci {{ background: linear-gradient(135deg, #f78166, #f78166); }}
        .game-icon.dlc {{ background: linear-gradient(135deg, var(--warning), #e3b341); }}
        .game-icon.update {{ background: linear-gradient(135deg, var(--success), #56d364); }}
        .game-title {{ flex: 1; min-width: 0; }}
        .game-title h3 {{ font-size: 0.9rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        .game-title .game-type {{ font-size: 0.65rem; color: var(--fg-secondary); text-transform: uppercase; letter-spacing: 0.5px; }}
        .game-meta {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto; }}
        .meta-tag {{ display: inline-flex; align-items: center; gap: 3px; padding: 3px 7px; background: var(--bg-primary); border: 1px solid var(--border); border-radius: 3px; font-size: 0.6rem; color: var(--fg-secondary); }}
        .meta-tag.drive-d {{ border-color: #58a6ff; color: #58a6ff; }}
        .meta-tag.drive-e {{ border-color: #a371f7; color: #a371f7; }}
        .meta-tag.type-nsp {{ border-color: var(--success); color: var(--success); }}
        .meta-tag.type-xci {{ border-color: #f78166; color: #f78166; }}
        .meta-tag.type-dlc {{ border-color: var(--warning); color: var(--warning); }}
        .meta-tag.type-update {{ border-color: #a371f7; color: #a371f7; }}
        .meta-tag.type-base {{ border-color: var(--success); color: var(--success); }}
        .meta-tag.type-size {{ border-color: var(--warning); color: var(--warning); font-family: monospace; }}
        .no-results {{ text-align: center; padding: 64px 24px; color: var(--fg-secondary); }}
        .no-results svg {{ width: 64px; height: 64px; margin-bottom: 16px; opacity: 0.5; }}

        @media (max-width: 768px) {{
            .container {{ padding: 16px; }}
            h1 {{ font-size: 1.75rem; }}
            .controls {{ flex-direction: column; align-items: stretch; }}
            .search-box {{ min-width: 0; }}
            .filters {{ justify-content: center; }}
            .game-grid {{ grid-template-columns: 1fr; }}
            .game-card.list-view {{ flex-direction: column; }}
            .game-card.list-view .game-image,
            .game-card.list-view .game-image-placeholder {{ width: 100%; height: 180px; min-height: 180px; border-radius: 0; border-right: none; border-bottom: 1px solid var(--border); }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Catalogo Nintendo Switch - Juegos Base</h1>
            <p style="color: var(--fg-secondary); margin-top: 8px;">{total} juegos base · Discos D: ({d_count}) + E: ({e_count}) · {real_images}/{base_count} con portada real</p>
            <div class="stats">
                <div class="stat"><div class="stat-value">{total:,}</div><div class="stat-label">Juegos Base</div></div>
                <div class="stat"><div class="stat-value">{real_images:,}</div><div class="stat-label">Con Portada</div></div>
                <div class="stat"><div class="stat-value">{total - real_images:,}</div><div class="stat-label">Sin Portada</div></div>
            </div>
        </header>

        <div class="controls">
            <div class="search-box">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <input type="text" id="search-input" placeholder="Buscar juegos base..." autocomplete="off">
            </div>
            <div class="filters" id="filters">
                <button class="filter-btn active" data-filter="base">Juegos Base ({base_count:,})</button>
            </div>
            <div class="view-toggle">
                <button class="view-btn active" data-view="grid" title="Vista cuadrícula"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg></button>
                <button class="view-btn" data-view="list" title="Vista lista"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
            </div>
        </div>

        <div class="results-info">
            <span id="results-count">Mostrando {total:,} de {total:,} juegos base</span>
            <span id="active-filters"></span>
        </div>

        <div class="game-grid" id="game-grid">
'''

    for game in games_sorted:
        cat = game['category']

        if game['type'] == 'xci':
            icon = '💾'
            icon_class = 'xci'
        elif cat == 'dlc':
            icon = '🧩'
            icon_class = 'dlc'
        elif cat == 'update':
            icon = '⬆️'
            icon_class = 'update'
        else:
            icon = '🎮'
            icon_class = ''

        drive_label = 'D:' if game['drive'] == 'd' else 'E:'
        drive_class = 'drive-d' if game['drive'] == 'd' else 'drive-e'
        type_class = 'type-nsp' if game['type'] == 'nsp' else 'type-xci'
        cat_class = 'type-dlc' if cat == 'dlc' else ('type-update' if cat == 'update' else 'type-base')
        cat_label = 'Base' if cat == 'base' else ('DLC' if cat == 'dlc' else 'Update')

        name_escaped = game['name'].replace('&', '&').replace('<', '<').replace('>', '>').replace('"', '"')

        # File size
        size_mb = game.get('size_mb', 0)
        if size_mb >= 1024:
            size_str = f"{size_mb/1024:.2f} GB"
        else:
            size_str = f"{size_mb:.0f} MB"

        # Imagen: local si existe, si no placeholder SVG
        if game.get('image') and cat == 'base':
            img_path = game['image']
            # Verificar si el archivo existe
            img_html = f'<img class="game-image" src="{img_path}" alt="{name_escaped}" loading="lazy" onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'flex\'"><div class="game-image-placeholder" style="display:none">{PLACEHOLDER_SVGS.get(cat, PLACEHOLDER_SVGS["base"])}</div>'
        else:
            if cat == 'base' and game['type'] == 'xci':
                placeholder = PLACEHOLDER_SVGS['xci']
            else:
                placeholder = PLACEHOLDER_SVGS.get(cat, PLACEHOLDER_SVGS['base'])
            img_html = f'<div class="game-image-placeholder">{placeholder}</div>'

        html += f'''            <article class="game-card" data-name="{name_escaped.lower()}" data-category="{cat}" data-type="{game['type']}" data-drive="{game['drive']}">
                {img_html}
                <div class="game-content">
                    <div class="game-header">
                        <div class="game-icon {icon_class}">{icon}</div>
                        <div class="game-title">
                            <h3 title="{name_escaped}">{name_escaped}</h3>
                            <span class="game-type">{cat_label}</span>
                        </div>
                    </div>
                    <div class="game-meta">
                        <span class="meta-tag {drive_class}">{drive_label}</span>
                        <span class="meta-tag {type_class}">{game['type'].upper()}</span>
                        <span class="meta-tag {cat_class}">{cat_label}</span>
                        <span class="meta-tag type-size">💾 {size_str}</span>
                    </div>
                </div>
            </article>
'''

    html += '''        </div>

        <div class="no-results" id="no-results" style="display: none;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="8" x2="14" y2="14"></line><line x1="14" y1="8" x2="8" y2="14"></line></svg>
            <h3>No se encontraron resultados</h3>
            <p>Intenta cambiar los filtros o la busqueda</p>
        </div>
    </div>

    <script>
        const allGames = document.querySelectorAll('.game-card');
        const searchInput = document.getElementById('search-input');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const viewBtns = document.querySelectorAll('.view-btn');
        const grid = document.getElementById('game-grid');
        const resultsCount = document.getElementById('results-count');
        const activeFiltersEl = document.getElementById('active-filters');
        const noResults = document.getElementById('no-results');

        let currentView = 'grid';
        let activeFilter = 'all';
        let searchTerm = '';

        function getCategory(el) { return el.dataset.category; }
        function getType(el) { return el.dataset.type; }
        function getDrive(el) { return el.dataset.drive; }
        function getName(el) { return el.dataset.name; }

        function filterGames() {
            let visible = 0;
            allGames.forEach(el => {
                const nameMatch = getName(el).includes(searchTerm.toLowerCase());
                let filterMatch = true;
                const cat = getCategory(el);

                if (activeFilter === 'base') filterMatch = cat === 'base';

                if (nameMatch && filterMatch) {
                    el.style.display = '';
                    visible++;
                } else {
                    el.style.display = 'none';
                }
            });

            if (visible === 0) {
                grid.style.display = 'none';
                noResults.style.display = 'block';
            } else {
                grid.style.display = 'grid';
                noResults.style.display = 'none';
            }

            resultsCount.textContent = `Mostrando ${visible.toLocaleString()} de {total:,} juegos base`;
            updateActiveFilters();
        }

        function updateActiveFilters() {{
            const labels = {{ 'base': 'Juegos Base' }};
            let activeLabels = [];
            if (activeFilter !== 'base') activeLabels.push(labels[activeFilter]);
            if (searchTerm) activeLabels.push(`Busqueda: "${{searchTerm}}"`);
            activeFiltersEl.textContent = activeLabels.length ? `Filtros: ${{activeLabels.join(' • ')}}` : '';
        }}

        searchInput.addEventListener('input', (e) => {{ searchTerm = e.target.value; filterGames(); }});

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeFilter = btn.dataset.filter;
                filterGames();
            }});
        }});

        viewBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                viewBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentView = btn.dataset.view;
                grid.classList.toggle('list-view', currentView === 'list');
            }});
        }});

        document.addEventListener('keydown', (e) => {{
            if (e.target === searchInput) return;
            if (e.key === '/') {{ e.preventDefault(); searchInput.focus(); }}
            if (e.key === 'Escape') {{ searchInput.value = ''; searchTerm = ''; searchInput.blur(); filterGames(); }}
        }});

        filterGames();
    </script>
</body>
</html>'''

    with open('catalogo-juegos-switch-completo.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[OK] HTML generado: catalogo-juegos-switch-completo.html")


def main():
    print("=" * 60)
    print("REGENERANDO HTML CON IMAGENES LOCALES")
    print("=" * 60)

    with open('catalogo-juegos-switch-completo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    games = data['games']

    total = data['metadata']['totalGames']
    d_count = data['metadata']['driveD']
    e_count = data['metadata']['driveE']
    nsp_count = data['metadata']['byFormat']['NSP']
    xci_count = data['metadata']['byFormat']['XCI']
    base_count = data['metadata']['byCategory']['base']
    dlc_count = data['metadata']['byCategory']['dlc']
    update_count = data['metadata']['byCategory']['update']

    # Verificar imágenes locales
    images_dir = Path('images')
    local_images = list(images_dir.glob('*')) if images_dir.exists() else []
    print(f"Imagenes locales en images/: {len(local_images)}")

    generate_html(games, total, d_count, e_count, nsp_count, xci_count, base_count, dlc_count, update_count)

    with_images = sum(1 for g in games if g.get('image'))
    print(f"Juegos con imagen en JSON: {with_images}/{base_count} (base)")


if __name__ == '__main__':
    main()