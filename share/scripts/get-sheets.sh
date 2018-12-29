#!/bin/sh

## this doesn't error check, if it breaks and destroys things I'm sorry

mkdir cheatsheets
cd cheatsheets
mkdir cheat tldr spool
git clone --recursive https://github.com/mechanicalAI/learnxinyminutes-docs
git clone --recursive https://github.com/mechanicalAI/cheat cheat-temp
mv cheat-temp/cheat/cheatsheets/* cheat
rm -rf cheat-temp
git clone --recursive https://github.com/mechanicalAI/tldr tldr-temp
mv tldr-temp/pages/* tldr
rm -rf tldr-temp
git clone --recursive https://github.com/mechanicalAI/cheat.sheets
mv cheat.sheets/sheets .