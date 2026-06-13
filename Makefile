.PHONY: verify verify-python verify-typescript

verify: verify-python verify-typescript

verify-python:
	python3 -m compileall -q week1 week2 week3 week4

verify-typescript:
	@for f in week*/*.ts; do \
		tsc --noEmit --target ES2020 --module commonjs --skipLibCheck "$$f" || exit 1; \
	done
