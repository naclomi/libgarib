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


clean:
	rm -rf python/libgarib/parsers/*
	rm -rf js/parsers/*