#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);
{
	long int size = PyList_Size(p);
	int i;
	PyListobject *obj = (pyListObject *)p;
	printf("[*] Size of the Python List = %1i\n", size);
	printf("[*] Allocated = %1i\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, py_Type (obj->ob_item[i])->tp_name);
