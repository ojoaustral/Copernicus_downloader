# Copernicus_downloader

**Tools for Mass-Downloading Copernicus Time Series Data**  

## Overview  
This repository contains tools for efficiently downloading Copernicus marine service data for time-series analysis. The workflow integrates R and Python, allowing users to manage study metadata (sampling sites and dates) and automate data retrieval from Copernicus.

## Features  
✅ **Handles Study Metadata**: Uses R Markdown to manage sampling sites, dates, and study design.  
✅ **Automated Data Download**: Python script programmatically fetches Copernicus data.  
✅ **Traceability & Reproducibility**: The R Markdown document (`Monterey_env_mapping.Rmd`) serves as documentation to ensure transparency in data handling.  

## Workflow  
0. **Clone the repo**
1. **Prepare Metadata (R)**  
   - Open `Monterey_env_mapping.Rmd` to organize and document study metadata.  
   - Define sampling sites, time range, and any necessary parameters.  

2. **Download Data (Python)**  
   - Run the Python script to fetch Copernicus data based on metadata.  
   - Automate requests and ensure batch processing.  

3. **Traceability**  
   - The **Markdown document serves as a log** of all operations for reproducibility.  
