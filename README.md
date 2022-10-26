# pntCloud

Download zip file that contains 3 patients. For each patient, open each .ucd file in excel (or open in text edit and copy/paste to excel). Delete line 1, delete first column, and delete all rows after 937. (we only want nodalx, y, z data). Save as .txt file. (This has already been done for frames 18-26 for pt1, see zipped folder called pt1.zip)

Open a patient folder, manually rename files from .ucd to .txt 

Run txtPly.py to convert files in that folder from .txt to .ply

Run volumePty to convert to point cloud data and calculate convex hull and volume. 
