# Fingerprint-Classification-System-Through-LENET
Fingerprint classification system using fingerprint orientantion feature vectors of ROI images obtained after passing through different modules of a LENET CNN system - Universidad Nacional de San Agustin (Arequipa - 2018).
#Course
- Topics of Artificial Intelligence
#Authors
- Ruben Edwin Hualla Quispe
- Patrick Lazo Colque
# Modules
# Data Storage Module
- NIST4 database
# Data Preprocessing Module
- Preprocessing stages:
  * Fingerprint Histogram Equalization
  * Fingerprint Gabor Enhancement
  * Fingerprint Threshold Binarization
  * Fingerprint Thinning
- Final results:
  * NIST4 4000 thinned fingerprint images
# Data Feature Extraction Module
- Two features extracted:
  * Region of Interes extraction through ANN detection algorithm
  * Orientation Map 100 and 400 features extraction algorithm
- Final results:
  * Manually extracted training database for roi block detection.
  * NIST4 4000 roi fingerprint images of 200x200px
  * 2 dat files containing:
        * 4000 NIST4 features vectors of 400 values from roi orientation map.
        * 4000 NIST4 features vectors of 100 values from roi orientation map.
# Data Processing and Results Gathering( Classification and Results  Module )
- Fingerprint classification system:
  * Fingerprint classification 
- Final results:
  * Results from experiments of classification system using a  LENET CNN.
  * Nice classification model of more than 90% accuracy found during experimentation available and ready to be loaded in keras.
