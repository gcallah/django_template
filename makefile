# A template makefile that works for static websites.
# Need to export as ENV var
export TEMPLATE_DIR = templates
DEV_DIR = django_template
PTML_DIR = html_src
UTILS_DIR = utils
TEST_DIR = tests
SITE_DIR = mysite
REPO = django_template
PY_LINT = flake8
PYLINT_FLAGS =
PYTHON_FILES = $(shell ls $(DEV_DIR)/*.py)
PYTHON_FILES += $(shell ls $(SITE_DIR)/*.py)
PYTHON_FILES += $(shell ls $(DEV_DIR)/$(TEST_DIR)/*.py)


INCS = $(TEMPLATE_DIR)/head.txt $(TEMPLATE_DIR)/logo.txt $(TEMPLATE_DIR)/menu.txt

HTMLFILES = $(shell ls $(PTML_DIR)/*.ptml | sed -e 's/.ptml/.html/' | sed -e 's/html_src\///')

FORCE:

prod: $(INCS) $(HTMLFILES) tests
	-git commit -a 
	git pull origin master
	git push origin master

tests: django_tests lint

django_tests: FORCE
	./pytests.sh

lint: $(patsubst %.py,%.pylint,$(PYTHON_FILES))

%.pylint:
	$(PY_LINT) $(PYLINT_FLAGS) $*.py

dev_local:
	pip3 install --upgrade pip
	pip3 install -r requirements-dev.txt

nocrud:
	rm *~
	rm .*swp
	rm $(PTML_DIR)/*~
	rm $(PTML_DIR)/.*swp

clean:
	touch $(PTML_DIR)/*.ptml; make local
