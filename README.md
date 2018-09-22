### Description

This code can be used to explore data with the following format:

- HDF4 (support extensions of `.h4`, `.hdf`, `.hdf4`)
- __HDF5 [Done] (support extensions of `.h5`, `.hdf5`)__
- __netCDF, netCDF4 [Done] (support extensions of `.nc`, `.netcdf`, `.cdf`, `.n4`, `.nc4`)__
- IDL save file (support extensions of `.idl`, `.sav`, `.out`)
- geoTIFF
- png

---
### Dependencies

- Python 3.6
  - [h5py](http://www.h5py.org/)
  - [pyhdf](http://fhs.github.io/python-hdf4/)
  - [scipy.io](https://docs.scipy.org/doc/scipy/reference/io.html)
  - [netCDF4](http://unidata.github.io/netcdf4-python/)
- [gdal](http://www.gdal.org/)
- [imgcat](https://www.iterm2.com/documentation-images.html) (only support iTerm2)

---
### How to use

1. Install the dependencies;
2. Put this code under one of the system `$PATH` directories, e.g., `/usr/local/bin`.
3. Reopen a terminal, go to a directory that has data, e.g, for file `MCD43C3.A2015337.005.2015365205333.hdf`,

  ```bash
  lss MCD43C3.A2015337.005.2015365205333.hdf
  ```

  ```bash
  +
  Albedo_BSA_Band1 ----- : Dataset  (3600, 7200)
  Albedo_BSA_Band2 ----- : Dataset  (3600, 7200)
  Albedo_BSA_Band3 ----- : Dataset  (3600, 7200)
  Albedo_BSA_Band4 ----- : Dataset  (3600, 7200)
  Albedo_BSA_Band5 ----- : Dataset  (3600, 7200)
  Albedo_BSA_Band6 ----- : Dataset  (3600, 7200)
  Albedo_BSA_Band7 ----- : Dataset  (3600, 7200)
  Albedo_BSA_nir ------- : Dataset  (3600, 7200)
  Albedo_BSA_shortwave - : Dataset  (3600, 7200)
  Albedo_BSA_vis ------- : Dataset  (3600, 7200)
  Albedo_WSA_Band1 ----- : Dataset  (3600, 7200)
  Albedo_WSA_Band2 ----- : Dataset  (3600, 7200)
  Albedo_WSA_Band3 ----- : Dataset  (3600, 7200)
  Albedo_WSA_Band4 ----- : Dataset  (3600, 7200)
  Albedo_WSA_Band5 ----- : Dataset  (3600, 7200)
  Albedo_WSA_Band6 ----- : Dataset  (3600, 7200)
  Albedo_WSA_Band7 ----- : Dataset  (3600, 7200)
  Albedo_WSA_nir ------- : Dataset  (3600, 7200)
  Albedo_WSA_shortwave - : Dataset  (3600, 7200)
  Albedo_WSA_vis ------- : Dataset  (3600, 7200)
  BRDF_Quality --------- : Dataset  (3600, 7200)
  Local_Solar_Noon ----- : Dataset  (3600, 7200)
  Percent_Inputs ------- : Dataset  (3600, 7200)
  Percent_Snow --------- : Dataset  (3600, 7200)
  -
  ```

4. For data that has unclear file type extension, e.g., `test.idlsav`,

  ```bash
  lss test.idlsav idl
  ```
