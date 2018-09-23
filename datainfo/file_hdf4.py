import os

try:
    from pyhdf.SD import SD, SDC
except ImportError:
    exit('Error [lss]: cannot import pyhdf.')




def GET_VARIABLE_NAMES(obj, prefix=''):

    for key in obj.keys():

        item = obj[key]
        path = '{prefix}/{key}'.format(prefix=prefix, key=key)
        if isinstance(item, h5py.Dataset):
            yield path
        elif isinstance(item, h5py.Group):
            yield from GET_VARIABLE_NAMES(item, prefix=path)




def FILE_SCAN(fname):

    try:
        f = SD(fname, SDC.READ)
    except:
        exit('Error [lss]: cannot access \'{fname}\'.'.format(fname=fname))

    vnames = f.datasets().keys()

    data_dict = {}
    for vname in vnames:
        obj = f.select(vname)
        info = obj.info()
        if info[1] == 1:
            data_dict[vname] = str((info[2],))
        elif info[1] > 1:
            data_dict[vname] = str(tuple(info[2]))

    f.end()

    return data_dict




if __name__ == '__main__':

    fname_test = os.path.abspath('test/data/sample.hdf')
    data_dict  = FILE_SCAN(fname_test)
