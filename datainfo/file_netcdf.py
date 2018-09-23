import os

try:
    import netCDF4 as nc4
except ImportError:
    exit('Error [lss]: cannot import netCDF4.')




def GET_VARIABLE_NAMES(obj, prefix=''):

    keys = list(obj.variables.keys()) + list(obj.groups.keys())

    for key in keys:
        try:
            item = obj.groups[key]
            path = '{prefix}.groups[\'{key}\']'.format(prefix=prefix, key=key)
            yield from GET_VARIABLE_NAMES(item, prefix=path)
        except KeyError:
            item = obj.variables[key]
            path = '{prefix}.variables[\'{key}\']'.format(prefix=prefix, key=key)
            yield path, item





def FILE_SCAN(fname):

    try:
        f = nc4.Dataset(fname, 'r')
    except:
        exit('Error [lss]: cannot access \'{fname}\'.'.format(fname=fname))

    vnames = []
    objs   = []
    for vname, obj in GET_VARIABLE_NAMES(f):
        vnames.append(vname[1:])
        objs.append(obj)

    data_dict = {}
    for i, vname in enumerate(vnames):
        data_dict[vname] = str(objs[i].shape)

    f.close()

    return data_dict




if __name__ == '__main__':

    fname_test = os.path.abspath('test/data/sample.nc4')
    data_dict  = FILE_SCAN(fname_test)
