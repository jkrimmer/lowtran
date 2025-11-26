# Lowtran in Python

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.213475.svg)](https://doi.org/10.5281/zenodo.213475)
![Actions Status](https://github.com/space-physics/lowtran/workflows/ci/badge.svg)
[![PyPi Download stats](http://pepy.tech/badge/lowtran)](http://pepy.tech/project/lowtran)

LOWTRAN7 atmospheric absorption extinction model.
Updated to be platform independent and easily accessible from Python and
[Matlab](#matlab).

The main LOWTRAN program is accessible from Python by using direct memory transfers instead of the cumbersome and error-prone process of writing/reading text files.
`xarray.Dataset` high-performance, simple N-D array data is passed out, with appropriate metadata.

## Gallery

See below for how to make these examples.

![Lowtran7 absorption](./gfx/lowtran.png)

## Install

Lowtran requires a Fortran compiler and CMake.
We use `f2py` (part of `numpy`) to seamlessly use Fortran libraries from Python by special compilation of the Fortran library with auto-generated shim code.
Make sure `meson` and the python devel headers & libraries are available on your system.

If a Fortran compiler is not already installed, install Gfortran:

* Linux: `apt install gfortran`
* Mac: `brew install gcc`
* Windows: Windows Subsystem for Linux

Install Python Lowtran code

```sh
pip install -e .
```

## Examples

In these examples, optionally write to HDF5 with the `-o` option.

We present Python [examples](./example) of:

* ground-to-space transmittance: TransmittanceGround2Space.py

  ![Lowtran Transmission](./doc/txgnd2space.png)
* sun-to-observer scattered radiance (why the sky is blue): ScatterRadiance.py

  ![Lowtran Scatter Radiance](./gfx/whyskyisblue.png)
* sun-to-observer irradiance: SolarIrradiance.py

  ![Lowtran Solar Irradiance](./gfx/irradiance.png)
* observer-to-observer solar single-scattering solar radiance (up-going) with custom Pressure, Temperature and partial pressure for 12 species: UserDataHorizontalRadiance.py
  ![Lowtran Solar Irradiance](./gfx/thermalradiance.png)
* observer-to-observer transmittance with custom Pressure, Temperature and partial pressure for 12 species: UserDataHorizontalTransmittance.py
* observer-to-observer transmittance: HorizontalTransmittance.py

  ![Lowtran Horizontal Path transmittance](./gfx/horizcompare.png)

### Matlab

Matlab users can seamlessly access Python modules, as demonstrated in
[RunLowtran.m](./RunLowtran.m).

Here's what's you'll need:

1. [Setup Python &harr; Matlab interface](https://www.scivision.dev/matlab-python-user-module-import/).
2. Install Lowtran in Python as at the top of this Readme.
3. From Matlab, verify everything is working by:

   ```matlab
   runtests('lowtran')
   ```

## Notes

### Card2 Aerosol Parameters

This implementation now supports Card2 parameters for configuring aerosol scattering and atmospheric conditions:

* **ihaze** (0-10): Aerosol model type
  * 0: No aerosol attenuation
  * 1: Rural, visibility 23 km
  * 2: Rural, visibility 5 km
  * 3: Maritime (visibility set by icstl)
  * 4: Maritime, visibility 23 km
  * 5: Urban, visibility 5 km
  * 6: Tropospheric, visibility 50 km
  * 8: Fog, visibility 0.2 km
  * 9: Fog, visibility 0.5 km
  * 10: Desert (visibility from wind speed)

* **iseasn** (0-2): Seasonal aerosol profile (2-30 km altitude)
  * 0: Same as model
  * 1: Spring-Summer
  * 2: Fall-Winter

* **ivulcn** (0-8): Volcanic aerosol profile and extinction
  * 0,1: Background stratospheric
  * 2: Moderate volcanic profile, Aged volcanic extinction
  * 3: High volcanic profile, Fresh volcanic extinction
  * 4: High volcanic profile, Aged volcanic extinction
  * 5: Moderate volcanic profile, Fresh volcanic extinction
  * 6: Moderate volcanic profile, Background strato extinction
  * 7: High volcanic profile, Background strato extinction
  * 8: Extreme volcanic profile, Fresh volcanic extinction

* **icstl** (1-10): Air mass character (only used with ihaze=3)
  * 1: Open ocean
  * 10: Strong continental influence

* **icld** (0-20): Cloud and rain models

See example/AerosolComparison.py for usage examples.

### LOWTRAN7 Documentation

LOWTRAN7
[User manual](https://apps.dtic.mil/sti/pdfs/ADA206773.pdf)
Refer to this to understand what parameters are set to default.

Right now a lot of configuration features aren't implemented, please request those you want.

### Reference

* Original 1994 Lowtran7 [Code](http://www1.ncdc.noaa.gov/pub/data/software/lowtran/)
* `LOWFIL` program in reference/lowtran7.10.f was not connected as we had previously implemented a filter function directly in  Python.
* `LOWSCAN` spectral sampling (scanning) program in `reference/lowtran7.13.f` was not connected as we had no need for coarser spectral resolution.
