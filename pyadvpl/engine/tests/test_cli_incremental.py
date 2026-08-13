import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from pyadvpl.engine import cli

SRC_A = "def u_A():\n    return 1\n"
SRC_B = "def u_B():\n    return 2\n"


def make_project(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    (src / "a.py").write_text(SRC_A, encoding="utf-8")
    (src / "b.py").write_text(SRC_B, encoding="utf-8")
    return src


def spy_transpile(monkeypatch):
    calls = []
    original = cli.transpile_file

    def spy(input_file, output_file, direction):
        calls.append(Path(input_file).name)
        return original(input_file, output_file, direction)

    monkeypatch.setattr(cli, "transpile_file", spy)
    return calls


def read_cache(dist):
    cache_file = dist / cli.CACHE_FILE
    assert cache_file.exists()
    return json.loads(cache_file.read_text(encoding="utf-8"))


def test_primeiro_build_incremental_transpila_tudo(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)

    assert sorted(calls) == ["a.py", "b.py"]
    assert (dist / "a.prw").exists()
    assert (dist / "b.prw").exists()


def test_build_incremental_pula_arquivos_inalterados(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)
    calls.clear()

    cli.process_transpile(src, dist, "py2adv", incremental=True)

    assert calls == []


def test_build_incremental_recompila_apenas_modificado(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)
    calls.clear()

    (src / "a.py").write_text("def u_A():\n    return 100\n", encoding="utf-8")
    cli.process_transpile(src, dist, "py2adv", incremental=True)

    assert calls == ["a.py"]


def test_build_incremental_regera_saida_apagada(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)
    calls.clear()

    (dist / "a.prw").unlink()
    cli.process_transpile(src, dist, "py2adv", incremental=True)

    assert calls == ["a.py"]
    assert (dist / "a.prw").exists()


def test_build_incremental_poda_cache_de_fontes_removidas(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)
    calls.clear()

    (src / "b.py").unlink()
    cli.process_transpile(src, dist, "py2adv", incremental=True)

    assert calls == []
    cache = read_cache(dist)
    assert set(cache) == {"a.py"}


def test_build_incremental_cria_arquivo_de_cache(tmp_path):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"

    cli.process_transpile(src, dist, "py2adv", incremental=True)

    cache = read_cache(dist)
    assert set(cache) == {"a.py", "b.py"}
    assert all(len(h) == 64 for h in cache.values())


def test_build_completo_atualiza_cache_para_incremental_seguinte(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)
    (src / "a.py").write_text("def u_A():\n    return 5\n", encoding="utf-8")
    calls.clear()

    cli.process_transpile(src, dist, "py2adv", incremental=False)

    assert sorted(calls) == ["a.py", "b.py"]

    calls.clear()
    cli.process_transpile(src, dist, "py2adv", incremental=True)
    assert calls == []


def test_convert_nao_cria_cache(tmp_path):
    legacy = tmp_path / "legacy"
    legacy.mkdir()
    (legacy / "x.prw").write_text("USER FUNCTION U_X()\nRETURN\n", encoding="latin-1")
    out = tmp_path / "out"

    cli.process_transpile(legacy, out, "adv2py")

    assert not (out / cli.CACHE_FILE).exists()


def test_build_incremental_arquivo_unico(tmp_path, monkeypatch):
    src = tmp_path / "src"
    src.mkdir()
    single = src / "c.py"
    single.write_text("def u_C():\n    return 3\n", encoding="utf-8")
    out = tmp_path / "out" / "c.prw"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(single, out, "py2adv", incremental=True)
    assert calls == ["c.py"]
    assert out.exists()

    calls.clear()
    cli.process_transpile(single, out, "py2adv", incremental=True)
    assert calls == []


def test_build_incremental_nao_cacheia_falha(tmp_path, monkeypatch):
    src = make_project(tmp_path)
    dist = tmp_path / "dist"
    calls = spy_transpile(monkeypatch)

    cli.process_transpile(src, dist, "py2adv", incremental=True)
    assert sorted(calls) == ["a.py", "b.py"]

    (src / "a.py").write_text("def u_A():\n    return 100\n", encoding="utf-8")

    def failing(input_file, output_file, direction):
        calls.append(Path(input_file).name)
        return False

    monkeypatch.setattr(cli, "transpile_file", failing)
    cli.process_transpile(src, dist, "py2adv", incremental=True)

    cache = read_cache(dist)
    assert cache["a.py"] != cli.file_hash(src / "a.py")


def test_cmd_build_repassa_flag_incremental(monkeypatch):
    captured = {}

    def fake_process(input_path, output_path, direction, incremental=False):
        captured["incremental"] = incremental

    monkeypatch.setattr(cli, "process_transpile", fake_process)
    monkeypatch.setattr(cli, "load_config", lambda: {})

    cli.cmd_build(argparse.Namespace(input=None, output=None, incremental=True))
    assert captured["incremental"] is True


def test_cli_parseia_flag_incremental(monkeypatch, tmp_path):
    captured = {}

    def fake_process(input_path, output_path, direction, incremental=False):
        captured["incremental"] = incremental

    monkeypatch.setattr(cli, "process_transpile", fake_process)
    monkeypatch.setattr(cli, "load_config", lambda: {})
    monkeypatch.setattr(sys, "argv", ["pyadvpl", "build", "--incremental"])
    monkeypatch.chdir(tmp_path)

    cli.main()
    assert captured["incremental"] is True
