parsers:
	mkdir -p python/parsers
	mkdir -p python/parsers/construct
	touch python/parsers/__init__.py
	touch python/parsers/construct/__init__.py

	mkdir -p js/parsers

	mkdir -p build_artifacts
	
	kaitai-struct-compiler --read-pos --outdir ./build_artifacts \
		-t javascript -t typescript -t python -t construct \
		formats/glover.lev.ksy \
		formats/glover.objbank.ksy \
		formats/glover.texbank.ksy

	mv build_artifacts/python/* python/parsers
	mv build_artifacts/construct/* python/parsers/construct
	mv build_artifacts/javascript/* js/parsers
	mv build_artifacts/typescript/* js/parsers

	rm -rf build_artifacts


clean:
	rm -rf python/parsers/*
	rm -rf js/parsers/*