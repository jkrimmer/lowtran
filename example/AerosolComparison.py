"""
Example demonstrating the use of Card2 aerosol parameters in LOWTRAN7

Card2 parameters control aerosol scattering and atmospheric conditions:
- ihaze: Aerosol model (0-10)
- iseasn: Seasonal aerosol profile (0-2)
- ivulcn: Volcanic aerosol profile and extinction (0-8)
- icstl: Air mass character for maritime model (1-10, only with ihaze=3)
- icld: Cloud and rain models (0-20)
"""

import lowtran
import matplotlib.pyplot as plt
from typing import Any

# Configuration for comparing different aerosol models
configs: list[dict[str, Any]] = [
    {'name': 'No Aerosol', 'ihaze': 0},
    {'name': 'Rural (23 km vis)', 'ihaze': 1},
    {'name': 'Rural (5 km vis)', 'ihaze': 2},
    {'name': 'Urban (5 km vis)', 'ihaze': 5},
    {'name': 'Tropospheric (50 km vis)', 'ihaze': 6},
]

# Base configuration
base_config = {
    'wlshort': 300,      # 300 nm
    'wllong': 2500,      # 2500 nm (2.5 microns)
    'wlstep': 20,
    'model': 5,          # Subarctic Winter
    'itype': 3,          # Vertical/slant path from ground to space
    'iemsct': 0,         # Transmittance mode
    'im': 1,             # Multiple scattering
    'iseasn': 0,         # Same as model
    'ivulcn': 0,         # Background stratospheric
    'icstl': 0,
    'icld': 0,
    'h1': 0,             # Ground level
    'angle': 0,          # Zenith angle
}

# Calculate transmittance for each aerosol model
plt.figure(figsize=(12, 8))

for config in configs:
    c = base_config.copy()
    c['ihaze'] = int(config['ihaze'])

    TR = lowtran.golowtran(c)
    wavelength = TR.wavelength_nm.values
    transmission = TR.transmission.values.squeeze()

    plt.plot(wavelength, transmission, label=config['name'], linewidth=2)

plt.xlabel('Wavelength (nm)', fontsize=12)
plt.ylabel('Transmission', fontsize=12)
plt.title('Atmospheric Transmittance for Different'
          ' Aerosol Models\n(Subarctic Winter, Ground to Space)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(300, 2500)
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
