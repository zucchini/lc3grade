VERSION = $(shell git describe)

.PHONY: clean

# Produce an executable zip file full of Python code
# More info:
# https://docs.python.org/3/library/zipapp.html#the-python-zip-application-archive-format
# Why I didn't just use the zipapp module:
# https://bugs.python.org/issue26277
../lc3grade: $(wildcard lc3grade/**/*.py lc3grade/*.py)
	printf 'import runpy\nrunpy.run_module("lc3grade", init_globals={"VERSION": "%s"})\n' $(VERSION) >__main__.py
	rm -f lc3grade.zip
	zip -x '*/.*' '*.pyc' '*/__pycache__/' -r lc3grade.zip __main__.py lc3grade/
	rm __main__.py
	printf '#!/usr/bin/env python3\n' >$@
	cat lc3grade.zip >>$@
	rm lc3grade.zip
	chmod +x $@

clean:
	rm -f __main__.py lc3grade.zip ../lc3grade
