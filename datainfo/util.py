import os
from collections import OrderedDict
from datainfo.file_hdf5   import FILE_SCAN as GET_DATA_DICT_H5
from datainfo.file_hdf4   import FILE_SCAN as GET_DATA_DICT_H4
from datainfo.file_idl    import FILE_SCAN as GET_DATA_DICT_IDL
from datainfo.file_netcdf import FILE_SCAN as GET_DATA_DICT_NC



def GET_DATA_INFO(args):

    fname = os.path.abspath(args.fname[0])
    if not os.path.exists(fname):
        exit('Error [lss]: cannot locate file \'{fname}\'.'.format(fname=fname))

    if args.format != None:

        dataType = args.format.lower()

    else:

        filename = os.path.basename(fname)
        try:

            words = filename.split('.')

            if len(words) == 1:
                exit('Error [lss]: cannot determine the data type of file \'{filename}\'.'.format(filename=filename))
            else:
                dataType = words[-1].lower()

        except ValueError:

            exit('Error [lss]: cannot determine the data type of file \'{filename}\'.'.format(filename=filename))

    dataTypeDict = {
            'h5'  : 'HDF5',
            'hdf5': 'HDF5',

            'hdf' : 'HDF4',
            'h4'  : 'HDF4',
            'hdf4': 'HDF4',

            'out' : 'IDL',
            'sav' : 'IDL',
            'idl' : 'IDL',

            'nc'     : 'netCDF',
            'netcdf' : 'netCDF',
            'cdf'    : 'netCDF',
            'n4'     : 'netCDF',
            'nc4'    : 'netCDF'
            }

    if dataType in dataTypeDict.keys():
        return fname, dataTypeDict[dataType]
    else:
        exit('Error [lss]: do NOT support the data type of file \'{filename}\'.'.format(filename=filename))




def GET_DATA_DICT(fname, dataType):

    if dataType == 'HDF5':
        data_dict = GET_DATA_DICT_H5(fname)
    elif dataType == 'HDF4':
        data_dict = GET_DATA_DICT_H4(fname)
    elif dataType == 'IDL':
        data_dict = GET_DATA_DICT_IDL(fname)
    elif dataType == 'netCDF':
        data_dict = GET_DATA_DICT_NC(fname)

    return data_dict





def PROCESS_DATA_DICT(data_dict):

    vnames = sorted(data_dict.keys())
    data_dict_new = OrderedDict()

    for vname in vnames:

        if '(' in data_dict[vname] and ')' in data_dict[vname]:
            data_dict_new[vname] = 'Dataset  {shape}'.format(shape=data_dict[vname])
        else:
            data_dict_new[vname] = 'Data     {value}'.format(value=data_dict[vname])

    return data_dict_new





def CREATE_MESSAGE(data_dict, dataType, dash_extra=2):

    dataType = dataType.upper()
    header   = '+ %s\n' % dataType
    footer   = '-'

    vnames = data_dict.keys()
    Nmax = max([len(vname) for vname in vnames]) + dash_extra

    body = ''
    for vname in vnames:
        dashed_line = '-'*(Nmax-len(vname))
        data_info   = data_dict[vname]
        line = '{vname} {dashed_line} : {data_info}\n'.format(vname=vname, dashed_line=dashed_line, data_info=data_info)
        body += line

    message = header + body + footer

    return message





if __name__ == '__main__':

    pass

