VPATH = examples
EXAMPLES = $(wildcard examples/*.py)
TEX_EXAMPLES = $(EXAMPLES:.py=.tex)
DESTTEX = ../DND-5e-LaTeX-Character-Sheet-Template/characters
export PYTHONPATH = .
.PHONY: venv test coverage

all: texfiles

%.tex: %.py
	-.venv/bin/python3 ./charsheets/main.py $< > $(DESTTEX)/$(notdir $*.tex)

texfiles: $(TEX_EXAMPLES)

venv:
	python3 -m venv .venv
	.venv/bin/pip3 install -U pip
	.venv/bin/pip3 install -U -r requirements-dev.txt

tests: test

test:
	pytest tests

coverage:
	pytest -n auto --no-cov-on-fail --cov-report term-missing --cov . tests
