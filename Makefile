VPATH = examples
EXAMPLES = $(wildcard examples/*.py)
TEX_EXAMPLES = $(EXAMPLES:.py=.tex)
DESTTEX = ../DND-5e-LaTeX-Character-Sheet-Template/characters
.PHONY: venv test coverage

%.tex: %.py
	.venv/bin/python3 ./charsheets/main.py $< > $(DESTTEX)/$(notdir $*.tex)

stuff: $(TEX_EXAMPLES)
	for pyfile in $?; do \
  		texfile = `basename $$pyfile`.tex; \
  		python3 ./charsheets/main.py $(pyfile) > $(DESTTEX)/$(texfile) ;\
  		done

venv:
	python3 -m venv .venv
	.venv/bin/pip3 install -U pip
	.venv/bin/pip3 install -U -r requirements-dev.txt


test:
	PYTHONPATH=. pytest tests

coverage:
	PYTHONPATH=. pytest -n auto --no-cov-on-fail --cov-report term-missing --cov . tests
