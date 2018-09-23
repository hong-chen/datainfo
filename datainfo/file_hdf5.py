import os

try:
    import h5py
except ImportError:
    exit('Error [lss]: cannot import h5py.')




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
        f = h5py.File(fname, 'r')
    except:
        exit('Error [lss]: cannot access \'{fname}\'.'.format(fname=fname))

    vnames = []
    for vname in GET_VARIABLE_NAMES(f):
        vnames.append(vname[1:])

    data_dict = {}
    for vname in vnames:
        obj = f[vname]
        data_dict[vname] = str(obj.shape)

    f.close()

    return data_dict




if __name__ == '__main__':

    fname_test = os.path.abspath('test/data/sample.h5')
    data_dict  = FILE_SCAN(fname_test)
