cat > tests/test_main.py <<'PY'
# tests/test_main.py
from app.main import add
import runpy

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 0) == 0

def test_main_block(capsys):
    """Exécute le module comme __main__ et vérifie la sortie."""
    runpy.run_module("app.main", run_name="__main__")
    output = capsys.readouterr().out
    assert "Exemple: add(2,3)" in output
PY
