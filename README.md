# Calibration Workflows

This repo contains the calibration workflows developed by me, for the purpose of hydrological modeling.

The model used is the groundwater model developed for the Middle Rio Grande Basin (MRGB), published under the title "SIMULATION OF GROUND-WATER FLOW IN THE MIDDLE RIO GRANDE BASIN BETWEEN COCHITI AND SAN ACACIA, NEW MEXICO", publicly available at:

https://pubs.er.usgs.gov/publication/wri20024200

A program to convert MF-2000 files to MF-2005 is available at:

https://water.usgs.gov/nrp/gwsoftware/mf2ktomf05uc/mf2ktomf05uc.html

The workflows include 4 main categories (and are based on the workflows in the pyEMU repo):

1). pest_run: This is a regular PEST run, which seeks to minimize the measurement objective function.

2). pilot_points_1: This sets up and runs the calibration for the groundwater model using pilot points for hydraulic conductivity.

3). err_var: Error Variance analysis workflow to evaluate the calibration.

4). gsa: Global Sensitivity Analysis workflow



### Software used

I've used the following Python, C++ and FORTRAN based software:

Parameter Estimation and Uncertainty Quantification software: pyEMU, PEST, PEST++

Groundwater Modeling software: FloPy, MODFLOW-2000/2005/NWT


### Disclaimer

 The workflows have been developed independently by me, and have not been approved for publication by USGS. Any errors are entirely my responsibility. I'm still in the process of completing the workflows.


### Contact

If you notice any errors, or have any questions or feedback, please contact me at unbiased.modeler@gmail.com
