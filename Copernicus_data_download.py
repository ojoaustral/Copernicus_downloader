##################################
#
# Mass-download Copernicus data sets for time series 
# 
# Cristian Correa, March 2025.
#
# Requires Phython >3.9
#
#################################

os.chdir("./MontereyBay/")
os.getcwd()

# Clear all variables from the current environment
for name in dir():
    if not name.startswith('_'):
        del globals()[name]

import os
import copernicusmarine
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from datetime import datetime, timedelta

# User credentials
user_ = "ccorrea"
pass_ = "Galax1as"

# Specify a dataset
# Datasets can be found https://data.marine.copernicus.eu/products
# Use filters to narrow down the search (e.g., by date range) > choose Product > Data access > Dateset (table) > Form (under Subset column).
# Go to Automate tab > Phython API. There you will find an snippet that can be modified and used to download the desired data. 

# Example to download Net Primary Productivity data for the Monterrey POC. 

dataset_id = "cmems_mod_glo_bgc_my_0.083deg-lmtl_PT1D-i"  
dataset_version = "202411"
variables = ["npp"]

# Define geographic extent
# longitude_bounds = (-122, -121)
# latitude_bounds = (36, 37)

longitude_bounds = (-122.431, -121.771)
latitude_bounds = (36.285, 37.385)


# Define date range (daily intervals)
start_date = datetime(2016, 9, 26)
end_date = datetime(2016, 11, 16)
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Ensure output directory exists
output_dir = "Monterrey_imagery_NPP"
os.makedirs(output_dir, exist_ok=True)

# Loop over each date (daily downloads)
for date in date_range:
    # Define start and end times (one-day period)
    start_str = date.strftime("%Y-%m-%dT00:00:00")
    end_str = date.strftime("%Y-%m-%dT23:59:59")
    
    # Define output filename for this day
    output_filename = f"nppv_{date.strftime('%Y%m%d')}.nc"
    output_path = os.path.join(output_dir, output_filename)
    
    # Skip download if the file already exists
    if os.path.exists(output_path):
        print(f"File {output_filename} already exists, skipping download.")
        continue

    # Download data for this day
    try:
        response = copernicusmarine.subset(
            dataset_id=dataset_id,
            dataset_version=dataset_version,
            variables=variables,
            minimum_longitude=longitude_bounds[0],
            maximum_longitude=longitude_bounds[1],
            minimum_latitude=latitude_bounds[0],
            maximum_latitude=latitude_bounds[1],
            start_datetime=start_str,
            end_datetime=end_str,
            coordinates_selection_method="strict-inside",
            minimum_depth=0,
            maximum_depth=10,
            disable_progress_bar=False,
            username=user_,
            password=pass_
        )

        # Ensure the response contains a file path
        if hasattr(response, "file_path") and os.path.exists(response.file_path):
            os.rename(response.file_path, output_path)
            print(f"Saved daily data for {start_str} as {output_filename}")
        else:
            print(f"Download failed or file not found for {start_str}")

    except Exception as e:
        print(f"Error downloading data for {start_str}: {e}")


# The forlder is populated by *.nc files (one per date in the time series).

# Get a description of the data set 
catalogue = copernicusmarine.describe(dataset_id = "cmems_mod_glo_bgc_my_0.083deg-lmtl_PT1D-i")
# Filter the output
catalogue_dict = catalogue.model_dump(
    exclude_none=True, 
    exclude_unset=True, 
    exclude={"products": {"__all__": {"datasets": True, "description": True, "keywords": True}}}
    )
catalogue_dict["products"][0]



