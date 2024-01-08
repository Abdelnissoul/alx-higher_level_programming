#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: the PyObject list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t mem_alloc;
	Py_ssize_t a;
	PyObject *ptr;

	size = PyList_Size(p);
	mem_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, mem_alloc);

	a = 0;
	while (a < size)
	{
		ptr = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(ptr)->tp_name);
		a++;
	}
}
