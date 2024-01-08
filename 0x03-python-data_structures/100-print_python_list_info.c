#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: the PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, mem_alloc;
	int a;
	PyObject *ptr;

	size = PY_SIZE(p);
	mem_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %d\n", mem_alloc);

    a = 0;
    while (a < size)
    {
        ptr = PyList_GetItem(p, a);
        printf("Element %ld: %s\n", a, Py_TYPE(ptr)->tp_name);
        a++;
    }
}
