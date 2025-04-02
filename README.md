# Copernicus_downloader

**Tools for Mass-Downloading Copernicus Time Series Data**  

![unnamed-chunk-11-1](https://github.com/user-attachments/assets/b6601168-9b50-44da-a8ad-b72ea1c7be88)

## Overview  
This repository contains tools for efficiently downloading Copernicus marine service data for time-series analysis. The workflow integrates R and Python, allowing users to manage study metadata (sampling sites and dates) and automate data retrieval from Copernicus.

## Features  
✅ **Handles Study Metadata**: Uses R and Markdown to manage sampling sites, dates, and study design.  
✅ **Automated Data Download**: Python script programmatically fetches Copernicus data.  
✅ **Traceability & Reproducibility**: All is organized and documented in a Jupyter Notebook (`*.ipynb`) that serves as documentation to ensure transparency in data handling.

## Workflow  
0. **Clone the repo**, and set the virtual environment .venv for the project. 
1. **Prepare Metadata (R)**  
   - Open `*.ipynb` to organize and document study metadata.  
   - Define sampling sites, time range, study area, and any necessary parameters.  

2. **Download Data (Python)**  
   - Run the Python script within the Jupyter Notebook to fetch Copernicus data based on metadata.  
   - Automate requests and ensure batch processing.  

3. **Extract values and create visualizations**  
   - Use downloaded .nc files (containing rasters) to extract values of parameters of interest and create visualizations, including GIF animations.  

5. **Traceability**  
   - The **Jupyter notebook** document serves as a log of all operations for reproducibility.  


Contributing  

Contributions are welcome! Feel free to open issues or submit pull requests.

Cristian Correa 
<cristian@newatlantis.io> 
