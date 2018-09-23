import os

try:
    import numpy
except ImportError:
    exit('Error [lss]: cannot import numpy.')

try:
    from scipy.io import readsav
except ImportError:
    exit('Error [lss]: cannot import scipy.')





def FILE_SCAN(fname):

    try:
        f = readsav(fname)
    except:
        exit('Error [lss]: cannot access \'{fname}\'.'.format(fname=fname))

    vnames0 = f.keys()
    data_dict = {}
    for vname0 in vnames0:
        obj = f[vname0]
        if isinstance(obj, numpy.recarray):
            vnames1 = obj.dtype.names
            for vname1 in vnames1:
                vname = '{vname0}.{vname1}[0]'.format(vname0=vname0, vname1=vname1)
                obj_new   = obj[vname1][0]
                if isinstance(obj_new, numpy.ndarray):
                    data_dict[vname] = str(obj_new.shape)
                elif isinstance(obj_new, bytes):
                    data_dict[vname] = obj_new.decode('utf-8')
                else:
                    data_dict[vname] = str(obj_new)
        elif isinstance(obj, numpy.ndarray):
            vname = vname0
            data_dict[vname] = str(obj.shape)
        elif isinstance(obj, bytes):
            vname = vname0
            data_dict[vname] = obj.decode('utf-8')
        else:
            vname = vname0
            data_dict[vname] = str(obj)


    return data_dict




if __name__ == '__main__':

    fname_test = os.path.abspath('test/data/sample1.sav')
    data_dict  = FILE_SCAN(fname_test)
