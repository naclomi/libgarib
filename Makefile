PYTHON-BIN ?= python3

PYINSTALLER-FLAGS = --clean --noconfirm

KAITAI_BIN ?= kaitai-struct-compiler
KAITAI_LANGUAGES = -t javascript -t python -t construct
ifeq "$(KAITAI_COMPILE_TYPESCRIPT)" "1"
    KAITAI_LANGUAGES += -t typescript
endif

parsers:
	mkdir -p python/libgarib/parsers
	mkdir -p python/libgarib/parsers/construct
	touch python/libgarib/parsers/__init__.py
	touch python/libgarib/parsers/construct/__init__.py

	mkdir -p js/parsers

	mkdir -p build_artifacts
	
	$(KAITAI_BIN) --read-pos --outdir ./build_artifacts \
		$(KAITAI_LANGUAGES) \
		formats/glover.lev.ksy \
		formats/glover.objbank.ksy \
		formats/glover.texbank.ksy

	$(PYTHON-BIN) ./python/scripts/ksy-patcher.py formats/*.ksy --compiled-directory build_artifacts/python

	mv build_artifacts/python/* python/libgarib/parsers
	mv build_artifacts/construct/* python/libgarib/parsers/construct
	mv build_artifacts/javascript/* js/parsers

	if [ -n "$(KAITAI_COMPILE_TYPESCRIPT)" ]; then	\
		mv build_artifacts/typescript/* js/parsers; \
	fi

	$(PYTHON-BIN) ./tools/level-tool.py xml-schema formats/glover.lev.ksy > formats/glover.lev.rng
	cp formats/glover.lev.rng python/libgarib/parsers

	rm -rf build_artifacts

fla2:
	c++ -o c/fla2-compress c/fla2.cpp c/fla2-compress-cli.cpp
	mkdir -p python/libgarib/cppcore
	touch python/libgarib/cppcore/__init__.py
	c++ -O3 -Wall -shared -std=c++11 -fPIC $(shell $(PYTHON-BIN) -m pybind11 --includes) c/fla2.cpp c/fla2-python.cpp -o python/libgarib/cppcore/fla2$(shell $(PYTHON-BIN) -c "from distutils import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))")

python-package: clean parsers
	$(PYTHON-BIN) -m build

standalone-tools:
	$(PYTHON-BIN) -m PyInstaller $(PYINSTALLER-FLAGS) tools/tools.spec

clean:
	rm -rf python/libgarib/parsers/*
	rm -rf js/parsers/*
	rm -rf dist/
	rm -rf libgarib.egg-info/
	rm -f formats/glover.lev.rng
	rm -f c/fla2-compress
	rm -f python/libgarib/cppcore/fla2.*.so