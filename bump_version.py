#!/usr/bin/env python3
"""
bump_version.py — Atualiza a versão do pacote (pyproject.toml) automaticamente.

Analisa os commits do branch atual e sobe a versão semestrial (SemVer):
  - commit `feat:`   => minor bump   (0.2.0 -> 0.3.0)
  - commit `fix:`    => patch bump   (0.2.0 -> 0.2.1)
  - commit `docs:`    => no bump     (mantém a versão)

Uso:
    python3 bump_version.py            # mostra o próximo versionamento
    python3 bump_version.py --apply    # sobe a versão e grava no pyproject.toml

Dependências: apenas stdlib (re, tomllib).

Exemplo de saída:
    Proximo versionamento: 0.2.1 (fix)
    Aplica: pyproject.toml version = "0.2.1"
"""

import re
import subprocess
import sys
from pathlib import Path

PYPROJECT = Path("pyproject.toml")
CHANGELOG = Path("CHANGELOG.md")

# Regex para extrair a versão "major.minor.patch" de um string semestrial.
SEMVER = re.compile(r"(\d+)\.(\d+)\.(\d+)")


def git(*args, cwd="."):
    """Executa `git <args>` e devolve a saída em texto limpo."""
    result = subprocess.run(
        ["git", *args], cwd=cwd,
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def current_version():
    """Lê a versão atual de pyproject.toml sem depender de tomllib."""
    text = PYPROJECT.read_text(encoding="utf-8")
    match = SEMVER.search(text)
    if not match:
        raise SystemExit("pyproject.toml: versão não encontrada")
    return tuple(int(g) for g in match.groups())


def commits_since(base="HEAD~5"):
    """Devolve a lista de commits do `base` até `HEAD` (mais novo primeiro).
    Cada item: (short_hash, full_hash, subject)."""
    log = git("log", "--reverse", f"{base}..HEAD",
              "--format=%h %H %s", cwd=".")
    commits = []
    for line in log.strip().splitlines():
        short_hash, full_hash, subject = line.partition(" ")
        commits.append((short_hash, full_hash, subject))
    return commits


def classify(commit_message):
    """Classifica o tipo de commit pela convenção `type:`.
    Devolve um dos: 'feat', 'fix', 'docs', 'test', ou None (sem bump)."""
    lowered = commit_message.lower()
    if "fix" in lowered:
        return "fix"
    if "feat" in lowered:
        return "feat"
    if "docs" in lowered:
        return "docs"
    if "test" in lowered:
        return "test"
    return None


def compute_next_version(current, commit_types):
    """Calcula a próxima versão a partir da versão atual + tipos de commits."""
    major, minor, patch = current
    if commit_types:
        patch += 1
    else:
        minor += 1
    return (major, minor, patch)


def changelog_entry(version, commit_types):
    """Gera uma seção de CHANGELOG.md a partir da versão + commits."""
    major, minor, patch = (int(g) for g in version.split("."))
    lines = [f"## [{major}.{minor}.{patch}] — (esta versão)", "",
             "### Mudanças desta versão", ""]
    for short_hash, _, message in commit_types:
        lines.append(f"- **{short_hash}** — {message}")
    return "\n".join(lines)


def main(apply=False, commits=None):
    version = current_version()
    major, minor, patch = version
    base = commits or "HEAD~5"
    commit_lines = commits_since(base)
    commit_types = [classify(msg) for _, _, msg in commit_lines]
    bumped = commit_types  # tipos que resultam em bump (fix/feat)

    next_version = compute_next_version(version, commit_types)
    next_str = ".".join(map(str, next_version))
    bump_type = "fix" if commit_types else "minor"

    print(f"Versão atual:  {major}.{minor}.{patch}")
    print(f"Comits analisados (últimos 5):")
    for short_hash, _, message in commit_lines:
        print(f"  {short_hash} {message}")
    print()
    print(f"Próximo versionamento: {next_str} ({bump_type})")

    if not apply:
        return

    # Aplica a nova versão em pyproject.toml.
    content = PYPROJECT.read_text(encoding="utf-8")
    old = f'version = "{major}.{minor}.{patch}"'
    new = f'version = "{next_str}"'
    if old not in content:
        raise SystemExit(f"pyproject.toml: linha 'version =' não encontrada")
    content = content.replace(old, new)
    PYPROJECT.write_text(content, encoding="utf-8")
    print(f"Aplicado: pyproject.toml version = \"{next_str}\"")

    # Atualiza CHANGELOG.md com a nova seção no topo.
    if CHANGELOG.exists():
        next_str = ".".join(map(str, next_version))
        changelog_entry(next_str, commit_lines)


if __name__ == "__main__":
    apply = "--apply" in sys.argv
    main(apply=apply, commits=None)
