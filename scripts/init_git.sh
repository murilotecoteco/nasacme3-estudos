#!/usr/bin/env bash
set -euo pipefail

git init -b main
git remote get-url origin >/dev/null 2>&1 || \
  git remote add origin "https://github.com/murilotecoteco/nasacme3-estudos.git"
git config core.hooksPath .githooks
echo "Git configurado: branch main, remoto origin e hooks .githooks"
