# Calibration Workflows

This repo contains the calibration workflows developed to be used by the USGS New Mexico Water Science Center (NM-WSC), Hydrogeology and Geochemisty modeling group.

The model used is the groundwater model developed for the Middle Rio Grande Basin (MRGB), published under the title "SIMULATION OF GROUND-WATER FLOW IN THE MIDDLE RIO GRANDE BASIN BETWEEN COCHITI AND SAN ACACIA, NEW MEXICO", publicly available at:

https://pubs.er.usgs.gov/publication/wri20024200

The workflows include 4 main categories:

1). pest_run: This is a regular PEST run, which seeks to minimize the measurement objective function.

2). pilot_points_1: This sets up and runs the calibration for the groundwater model using pilot points for hydraulic conductivity.

3). err_var: Error Variance analysis workflow to evaluate the calibration.

4). gsa: Global Sensitivity Analysis workflow



### Software used

I've used the following Python, C++ and FORTRAN based software:

Parameter Estimation and Uncertainty Quantification software: pyEMU, PEST, PEST++

Groundwater Modeling software: FloPy, MODFLOW-2000/2005/NWT


### Disclaimer

While the workflows have been developed for USGS NM-WSC, and I have received input and feedback from USGS hydrologists, the workflows have been developed independently by me, and have not been approved for publication by USGS. Any errors are entirely my responsibility.


### Contact

If you notice any errors, or have any questions or feedback, please contact me at unbiased.modeler@gmail.com
