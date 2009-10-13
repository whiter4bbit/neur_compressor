all:
	python setup.py build
	python setup.py install
	python matr_test.py
frontend:
	pyuic4 ui/main.ui > ui/main.py

