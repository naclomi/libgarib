parsers:
	mkdir -p python/parsers
	touch python/parsers/__init__.py

	mkdir -p js/parsers

	mkdir -p build_artifacts
	
	kaitai-struct-compiler --read-pos -t javascript -t typescript -t python --outdir ./build_artifacts \
		formats/glover.lev.ksy \
		formats/glover.objbank.ksy \
		formats/glover.texbank.ksy

	mv build_artifacts/python/* python/parsers
	mv build_artifacts/javascript/* js/parsers
	mv build_artifacts/typescript/* js/parsers

	rm -rf build_artifacts


clean:
	rm -rf python/parsers/*
	rm -rf js/parsers/*