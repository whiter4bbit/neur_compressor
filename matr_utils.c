#include "Python.h"
#include "algo.h"

double **PyList_ToArray(PyObject *list)
{
  int n = PyList_Size(list);
  PyObject *first = PyList_GetItem(list, 0);
  int m = PyList_Size(first);
  double **matr = (double**)malloc(n*sizeof(size_t));
  int i,j;
  for(i=0;i<n;i++){
    PyObject* row = PyList_GetItem(list, i);
    Py_INCREF(row);
    matr[i] = (double*)malloc(m*sizeof(double));
    for(j=0;j<m;j++){
      PyObject *cell = PyList_GetItem(row, j);
      Py_INCREF(cell);
      double value = PyFloat_AsDouble(cell);
      matr[i][j] = value;
      Py_DECREF(cell);
    }
    Py_DECREF(row);
  }
  return matr;
}

PyObject *PyList_FromArray(double **matr, int n, int m)
{
  PyObject *list = PyList_New(n);
  int i,j;
  for(i=0;i<n;i++){
    PyObject *row = PyList_New(m);
    for(j=0;j<m;j++){
      double value = *(*(matr+i)+j);
      PyList_SetItem(row, j, PyFloat_FromDouble(value));
    }
    PyList_SetItem(list, i, row);
  }
  return list;
}

PyObject * normalize(PyObject *self, PyObject *arg)
{
  PyObject *matr;
  if(!PyArg_ParseTuple(arg, "O", &matr))
    return NULL;
  if(!PyList_Check(matr))
    return NULL;
  int n = PyList_Size(matr);
  PyObject *first = PyList_GetItem(matr, 0);
  if(!PyList_Check(first))
    return NULL;
  int m = PyList_Size(first);
  double **arr = PyList_ToArray(matr);
  if(!arr) return NULL;
  algo_normalize(arr, n, m);
  PyObject *res = PyList_FromArray(arr, n,m);
  return res;
}

static PyMethodDef my_methods[] = {
    {"normalize", (PyCFunction)normalize, METH_VARARGS, "some descr"},
};

void initmatr_utils(void)
{
  Py_InitModule("matr_utils", my_methods);
}


