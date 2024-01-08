#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: the PyObject list
 */
void print_python_list_info(PyObject *p)
{

	int obj;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (obj = 0; obj < Py_SIZE(p); obj++)
	{
		printf("Element %d: %s\n", obj, Py_TYPE(PyList_GetItem(p, obj))->tp_name);
	}
}
