
#################################

library(reticulate)

# Force reticulate to use the correct virtual environment
Sys.setenv(RETICULATE_PYTHON = "/cloud/project/r-reticulate/bin/python")

# Load reticulate after setting the environment
library(reticulate)

# Verify that Python is set correctly
py_config()

# Now you can safely import and use copernicusmarine
py_run_string("import copernicusmarine")



############################# install 
library(reticulate)

# Ensure we are using the correct Python environment
use_virtualenv("r-reticulate", required = TRUE)

# Install matplotlib in the r-reticulate virtual environment
py_install("cartopy", envname = "r-reticulate")


