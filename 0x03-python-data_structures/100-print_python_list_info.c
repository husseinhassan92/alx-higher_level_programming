#include <Python.h>

/*
includes object.h
VIEW HEADER-> https://docs.python.org/3.4/c-api/structures.html)
VIEW MANUAL-> https://github.com/python/cpython/blob/master/Include/object.h
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n",
		       i,
		       (PY_TYPE(PyList_GetItem(p, i)))->tp_name);
	}
}