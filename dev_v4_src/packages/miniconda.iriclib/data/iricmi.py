# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

import numpy as np
from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _iricmi
else:
    import _iricmi

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


def _checkErrorCode(ier):
    if ier == 0: return

    raise Exception('Error code ier={0}'.format(ier))

class IntContainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _iricmi.IntContainer_swiginit(self, _iricmi.new_IntContainer())

    def value(self):
        return _iricmi.IntContainer_value(self)

    def setValue(self, v):
        return _iricmi.IntContainer_setValue(self, v)

    def pointer(self):
        return _iricmi.IntContainer_pointer(self)
    __swig_destroy__ = _iricmi.delete_IntContainer

# Register IntContainer in _iricmi:
_iricmi.IntContainer_swigregister(IntContainer)

class RealContainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _iricmi.RealContainer_swiginit(self, _iricmi.new_RealContainer())

    def value(self):
        return _iricmi.RealContainer_value(self)

    def setValue(self, v):
        return _iricmi.RealContainer_setValue(self, v)

    def pointer(self):
        return _iricmi.RealContainer_pointer(self)
    __swig_destroy__ = _iricmi.delete_RealContainer

# Register RealContainer in _iricmi:
_iricmi.RealContainer_swigregister(RealContainer)

class IntArrayContainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, size):
        _iricmi.IntArrayContainer_swiginit(self, _iricmi.new_IntArrayContainer(size))
    __swig_destroy__ = _iricmi.delete_IntArrayContainer

    def size(self):
        return _iricmi.IntArrayContainer_size(self)

    def value(self, index):
        return _iricmi.IntArrayContainer_value(self, index)

    def setValue(self, index, v):
        return _iricmi.IntArrayContainer_setValue(self, index, v)

    def pointer(self):
        return _iricmi.IntArrayContainer_pointer(self)

    def get(self):
        ret = np.zeros(self.size(), dtype=np.int32)
        for i in range(self.size()):
            ret[i] = self.value(i)
        return ret

    def set(self, vals):
        for i in range(self.size()):
            self.setValue(i, int(vals[i]))

# Register IntArrayContainer in _iricmi:
_iricmi.IntArrayContainer_swigregister(IntArrayContainer)

class RealArrayContainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, size):
        _iricmi.RealArrayContainer_swiginit(self, _iricmi.new_RealArrayContainer(size))
    __swig_destroy__ = _iricmi.delete_RealArrayContainer

    def size(self):
        return _iricmi.RealArrayContainer_size(self)

    def value(self, index):
        return _iricmi.RealArrayContainer_value(self, index)

    def setValue(self, index, v):
        return _iricmi.RealArrayContainer_setValue(self, index, v)

    def pointer(self):
        return _iricmi.RealArrayContainer_pointer(self)

    def get(self):
        ret = np.zeros(self.size(), dtype=np.float64)
        for i in range(self.size()):
            ret[i] = self.value(i)
        return ret

    def set(self, vals):
        for i in range(self.size()):
            self.setValue(i, float(vals[i]))

# Register RealArrayContainer in _iricmi:
_iricmi.RealArrayContainer_swigregister(RealArrayContainer)


def iricmi_check_cancel():
    ier, canceled = _iricmi.iricmi_check_cancel()
    _checkErrorCode(ier)

    return canceled

def iricmi_model_init():
    ier = _iricmi.iricmi_model_init()
    _checkErrorCode(ier)

def iricmi_model_terminate():
    ier = _iricmi.iricmi_model_terminate()
    _checkErrorCode(ier)

def iricmi_model_sync():
    ier = _iricmi.iricmi_model_sync()
    _checkErrorCode(ier)

def iricmi_model_dump():
    ier = _iricmi.iricmi_model_dump()
    _checkErrorCode(ier)

def iricmi_calc_init():
    ier = _iricmi.iricmi_calc_init()
    _checkErrorCode(ier)

def iricmi_calc_terminate():
    ier = _iricmi.iricmi_calc_terminate()
    _checkErrorCode(ier)

def iricmi_calc_sync_receive():
    ier = _iricmi.iricmi_calc_sync_receive()
    _checkErrorCode(ier)

def iricmi_calc_sync_send():
    ier = _iricmi.iricmi_calc_sync_send()
    _checkErrorCode(ier)

def iricmi_calc_dump():
    ier = _iricmi.iricmi_calc_dump()
    _checkErrorCode(ier)

def iricmi_error_print():
    _iricmi.iricmi_error_print()

def iricmi_error_print_and_exit():
    _iricmi.iricmi_error_print_and_exit()

def iricmi_read_integer(name):
    ier, value = _iricmi.iricmi_read_integer(name)
    _checkErrorCode(ier)

    return value

def iricmi_read_real(name):
    ier, value = _iricmi.iricmi_read_real(name)
    _checkErrorCode(ier)

    return value

def iricmi_read_string(name):
    ier, value = _iricmi.iricmi_read_string(name)
    _checkErrorCode(ier)

    return value

def iricmi_read_functional_size(name):
    ier, value = _iricmi.iricmi_read_functional_size(name)
    _checkErrorCode(ier)

    return value

def iricmi_read_functional_vals(name):
    size = iricmi_read_functional_size(name)

    x = RealArrayContainer(size)
    y = RealArrayContainer(size)

    ier = _iricmi.iricmi_read_functional_vals(name, x, y)
    _checkErrorCode(ier)

    return (x.get(), y.get())

def iricmi_read_functional_valwithname(name, paramname):
    size = iricmi_read_functional_size(name)

    val = RealArrayContainer(size)

    ier = _iricmi.iricmi_read_functional_valwithname(name, paramname, val)
    _checkErrorCode(ier)

    return val.get()

def iricmi_read_grid_node_count():
    ier, value = _iricmi.iricmi_read_grid_node_count()
    _checkErrorCode(ier)

    return value

def iricmi_read_grid_cell_count():
    ier, value = _iricmi.iricmi_read_grid_cell_count()
    _checkErrorCode(ier)

    return value

def iricmi_read_grid2d_str_size():
    ier, isize, jsize = _iricmi.iricmi_read_grid2d_str_size()
    _checkErrorCode(ier)

    return (isize, jsize)

def iricmi_read_grid2d_unstr_size():
    ier, value = _iricmi.iricmi_read_grid2d_unstr_size()
    _checkErrorCode(ier)

    return value

def iricmi_read_grid2d_unstr_cellsize():
    ier, value = _iricmi.iricmi_read_grid2d_unstr_cellsize()
    _checkErrorCode(ier)

    return value

def iricmi_read_grid2d_unstr_cells(cells):
    ier, value = _iricmi.iricmi_read_grid2d_unstr_cells(cells)
    _checkErrorCode(ier)

    return value

def iricmi_read_grid2d_coords():
    count = iricmi_read_grid_node_count()

    x = RealArrayContainer(count)
    y = RealArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_coords(x, y)
    _checkErrorCode(ier)

    return x.get(), y.get()

def iricmi_read_grid2d_integer_node(name):
    count = iricmi_read_grid_node_count()

    vals = IntArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_integer_node(name, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_grid2d_real_node(name):
    count = iricmi_read_grid_node_count()

    vals = RealArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_real_node(name, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_grid2d_complex_node(name):
    count = iricmi_read_grid_node_count()

    vals = IntArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_complex_node(name, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_grid2d_integer_cell(name):
    count = iricmi_read_grid_cell_count()

    vals = IntArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_integer_cell(name, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_grid2d_real_cell(name):
    count = iricmi_read_grid_cell_count()

    vals = RealArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_real_cell(name, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_grid2d_complex_cell(name):
    count = iricmi_read_grid_cell_count()

    vals = IntArrayContainer(count)
    ier = _iricmi.iricmi_read_grid2d_complex_cell(name, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_bc_count(type):
    ier, value = _iricmi.iricmi_read_bc_count(type)
    _checkErrorCode(ier)

    return value

def iricmi_read_bc_indicessize(type, num):
    ier, value = _iricmi.iricmi_read_bc_indicessize(type, num)
    _checkErrorCode(ier)

    return value

def iricmi_read_bc_indices(type, num, indices):
    count = iricmi_read_bc_indicessize(type, num)

    vals = IntArrayContainer(count)
    ier = _iricmi.iricmi_read_bc_indices(type, num, vals)
    _checkErrorCode(ier)

    return vals.get()

def iricmi_read_bc_integer(type, num, name):
    ier, value = _iricmi.iricmi_read_bc_integer(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_bc_real(type, num, name):
    ier, value = _iricmi.iricmi_read_bc_real(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_bc_string(type, num, name):
    ier, value = _iricmi.iricmi_read_bc_string(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_bc_functional_size(type, num, name):
    ier, value = _iricmi.iricmi_read_bc_functional_size(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_bc_functional_vals(type, num, name):
    size = iricmi_read_bc_functional_size(type, num, name)
    x = RealArrayContainer(size)
    y = RealArrayContainer(size)

    ier = _iricmi.iricmi_read_bc_functional_vals(type, num, name, x, y)
    _checkErrorCode(ier)

    return (x.get(), y.get())

def iricmi_read_bc_functional_valwithname(type, num, name, paramname):
    size = iricmi_read_bc_functional_size(type, num, name)
    val = RealArrayContainer(size)

    ier = _iricmi.iricmi_read_bc_functional_valwithname(type, num, name, paramname, val)
    _checkErrorCode(ier)

    return val.get()

def iricmi_read_complex_count(type):
    ier, value = _iricmi.iricmi_read_complex_count(type)
    _checkErrorCode(ier)

    return value

def iricmi_read_complex_integer(type, num, name):
    ier, value = _iricmi.iricmi_read_complex_integer(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_complex_real(type, num, name):
    ier, value = _iricmi.iricmi_read_complex_real(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_complex_string(type, num, name):
    ier, value = _iricmi.iricmi_read_complex_string(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_complex_functional_size(type, num, name):
    ier, value = _iricmi.iricmi_read_complex_functional_size(type, num, name)
    _checkErrorCode(ier)

    return value

def iricmi_read_complex_functional_vals(type, num, name):
    size = iricmi_read_complex_functional_size(type, num, name)
    x = RealArrayContainer(size)
    y = RealArrayContainer(size)

    ier = _iricmi.iricmi_read_complex_functional_vals(type, num, name, x, y)
    _checkErrorCode(ier)

    return (x.get(), y.get())

def iricmi_read_complex_functional_valwithname(type, num, name, paramname, val):
    size = iricmi_read_complex_functional_size(type, num, name)
    val = RealArrayContainer(size)

    ier = _iricmi.iricmi_read_complex_functional_valwithname(type, num, name, paramname, val)
    _checkErrorCode(ier)

    return val.get()

def iricmi_rin_time(t):
    ier = _iricmi.iricmi_rin_time(t)
    _checkErrorCode(ier)

def iricmi_rin_dump_interval(interval):
    ier = _iricmi.iricmi_rin_dump_interval(interval)
    _checkErrorCode(ier)

def iricmi_rin_integer(name, val):
    ier = _iricmi.iricmi_rin_integer(name, val)
    _checkErrorCode(ier)

def iricmi_rin_real(name, val):
    ier = _iricmi.iricmi_rin_real(name, val)
    _checkErrorCode(ier)

def iricmi_rin_bc_integer(type, index, name, val):
    ier = _iricmi.iricmi_rin_bc_integer(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rin_bc_real(type, index, name, val):
    ier = _iricmi.iricmi_rin_bc_real(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rin_complex_integer(type, index, name, val):
    ier = _iricmi.iricmi_rin_complex_integer(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rin_complex_real(type, index, name, val):
    ier = _iricmi.iricmi_rin_complex_real(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rin_grid2d_integer_node(name, vals):
    ier = _iricmi.iricmi_rin_grid2d_integer_node(name, vals)
    _checkErrorCode(ier)

def iricmi_rin_grid2d_real_node(name, vals):
    ier = _iricmi.iricmi_rin_grid2d_real_node(name, vals)
    _checkErrorCode(ier)

def iricmi_rin_grid2d_integer_cell(name, vals):
    ier = _iricmi.iricmi_rin_grid2d_integer_cell(name, vals)
    _checkErrorCode(ier)

def iricmi_rin_grid2d_real_cell(name, vals):
    ier = _iricmi.iricmi_rin_grid2d_real_cell(name, vals)
    _checkErrorCode(ier)

def iricmi_rout_time(t):
    ier = _iricmi.iricmi_rout_time(t)
    _checkErrorCode(ier)

def iricmi_rout_exchange_interval(interval):
    ier = _iricmi.iricmi_rout_exchange_interval(interval)
    _checkErrorCode(ier)

def iricmi_rout_dump_interval(interval):
    ier = _iricmi.iricmi_rout_dump_interval(interval)
    _checkErrorCode(ier)

def iricmi_rout_integer(name, val):
    ier = _iricmi.iricmi_rout_integer(name, val)
    _checkErrorCode(ier)

def iricmi_rout_real(name, val):
    ier = _iricmi.iricmi_rout_real(name, val)
    _checkErrorCode(ier)

def iricmi_rout_bc_integer(type, index, name, val):
    ier = _iricmi.iricmi_rout_bc_integer(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rout_bc_real(type, index, name, val):
    ier = _iricmi.iricmi_rout_bc_real(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rout_complex_integer(type, index, name, val):
    ier = _iricmi.iricmi_rout_complex_integer(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rout_complex_real(type, index, name, val):
    ier = _iricmi.iricmi_rout_complex_real(type, index, name, val)
    _checkErrorCode(ier)

def iricmi_rout_grid2d_integer_node(name, vals):
    ier = _iricmi.iricmi_rout_grid2d_integer_node(name, vals)
    _checkErrorCode(ier)

def iricmi_rout_grid2d_real_node(name, vals):
    ier = _iricmi.iricmi_rout_grid2d_real_node(name, vals)
    _checkErrorCode(ier)

def iricmi_rout_grid2d_integer_cell(name, vals):
    ier = _iricmi.iricmi_rout_grid2d_integer_cell(name, vals)
    _checkErrorCode(ier)

def iricmi_rout_grid2d_real_cell(name, vals):
    ier = _iricmi.iricmi_rout_grid2d_real_cell(name, vals)
    _checkErrorCode(ier)