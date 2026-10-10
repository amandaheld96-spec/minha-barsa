"""Nome das áreas e disciplinas no menu = título (# ...) do index.md da pasta.

Assim o menu mostra "Estatística" (com acento) em vez do nome da pasta.
"""
import re


def _titulo(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            for linha in f:
                m = re.match(r"#\s+(.+)", linha)
                if m:
                    return m.group(1).strip()
    except OSError:
        pass
    return None


def _percorrer(itens):
    for item in itens:
        if item.is_section:
            for filho in item.children:
                if filho.is_page and filho.file.name == "index":
                    titulo = _titulo(filho.file.abs_src_path)
                    if titulo:
                        item.title = titulo
                    break
            _percorrer(item.children)


def on_nav(nav, config, files):
    _percorrer(nav.items)
    return nav
