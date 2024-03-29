parsers:
	mkdir -p python/libgarib/parsers
	mkdir -p python/libgarib/parsers/construct
	touch python/libgarib/parsers/__init__.py
	touch python/libgarib/parsers/construct/__init__.py

	mkdir -p js/parsers

	mkdir -p build_artifacts
	
	kaitai-struct-compiler --read-pos --outdir ./build_artifacts \
		-t javascript -t typescript -t python -t construct \
		formats/glover.lev.ksy \
		formats/glover.objbank.ksy \
		formats/glover.texbank.ksy

	mv build_artifacts/python/* python/libgarib/parsers
	mv build_artifacts/construct/* python/libgarib/parsers/construct
	mv build_artifacts/javascript/* js/parsers
	mv build_artifacts/typescript/* js/parsers

	rm -rf build_artifacts

fla2:
	gcc -o c/fla2-compress c/fla2.c c/fla2-compress-cli.c
	mkdir -p python/libgarib/cppcore
	touch python/libgarib/cppcore/__init__.py
	c++ -O3 -Wall -shared -std=c++11 -fPIC $(shell python3 -m pybind11 --includes) c/fla2.c c/fla2-python.cpp -o python/libgarib/cppcore/fla2$(shell python3-config --extension-suffix)

clean:
	rm -rf python/libgarib/parsers/*
	rm -rf js/parsers/*
	rm c/fla2-compress
	rm python/libgarib/cppcore/fla2$(shell python3-config --extension-suffix)