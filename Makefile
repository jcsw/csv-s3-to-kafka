init:
	pip install -r requirements.txt
test:
	py.test tests
itest:
	py.test itests