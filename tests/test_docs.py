from pathlib import Path

from npe2 import PluginManifest

DOCS_DIR = Path(__file__).parent.parent / "_docs"


def test_example_manifest():
    example = DOCS_DIR / "example_manifest.yaml"
    assert PluginManifest.from_file(example)


def test_render_docs(tmp_path, monkeypatch):
    from _docs.render import main

    assert not list(tmp_path.glob("*.md"))
    main(tmp_path)
    assert list(tmp_path.glob("*.md"))
