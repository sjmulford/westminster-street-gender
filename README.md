Westminster Street Gender
==========================

For Open Data Day we decided to copy a project someone else had done (http://atunombre.uy/) and count/compare the genders of streetnames in our locale. We chose City of Westminster to begin with. 

First we downloaded Westminster street names from http://maposmatic.org/maps/186775

That data is in CityofWestminsterLondres.csv

Then we created a Python script for looping through the rows, picking out the words in the street name and then calculating a gender score for them. 

To do this we used the Python library 'SexMachine' - https://pypi.python.org/pypi/SexMachine/

You can see the script in basic.py

In order to calculate a score for each street name, we split the whole name up into words and then for each word we would add 1 to the score if the word was considered male, subtracted 1 from the score if it was female and left the score alone if the word was neutral. 

In the case of Adam and Eve Street for example, it would calculate +1 (for Adam) +0 (for and ) -1 (for Eve) and +0 (for Street) thus leading to a gender neutral final score i.e. 0.

More Data
=========
In order to georeference the streets, we used an existing dataset which another member of the team had extracted for a previous project which contained 12000 streets (london_streets.kml). The Ordnance Survey Meridian2 was used but as this is being discontinued, OpenRoads (https://www.ordnancesurvey.co.uk/business-and-government/products/os-open-roads.html) could be used instead.

The roads data was downloaded in Shapefile format from the OS and loaded into QGis. In QGis, the road data covered by the study area selected and exported to a KML file (http://gis.stackexchange.com/questions/110352/save-selection-option-in-qgis-2-4-0).

This new file was then exported again as a CSV, and this is the file which the gender-assigning Python script was run.

The street names had been joined to a postcode district to avoid ambiguity of location (streets with the same name in different places). The Sexmachine script was run again on the streetnames from this dataset (second_streets.csv). The script had to be adapted (second_script.py) in order to properly capitalize the full caps lock format of the street names and to make sure it handled the new column types etc.

Results of running the script on the new data can be found in second_results.csv

The gender scores in the resulting CSV were converted to descriptions ('male', 'female', 'neutral') in Excel to make the map's legend more understandable. Once the gender was assigned to each road, both the new KML file (containing road names and geometry) and the CSV (containing road names and gender) were loaded into Cartodb. Here we did a join on the road names using CartoDB’s ‘Column Join’ function (http://docs.cartodb.com/cartodb-editor/managing-your-data/#merge-by-column-join)

In CartoDB the streets were colour coded according to the gender field - orange for female, blue for male. (http://docs.cartodb.com/tutorials/conditional_styling/)

Observations
============

We had to do quite a bit of cleaning of the data to compensate for the algorithm's idiosyncracies. For example, it would not recognise a name if there was "apostrophe s" at the end e.g. St Anne's. 

St Jude and St Augustine and Bevan were incorrectly considered female and 'The' is considered a female name. These have been manually vetoed in the script
'Lane' was considered a male name, again this has been vetoed in the script. 


Results
========
The file, results.csv, contains the finalised results in 3 columns. The first is the streetname, the 2nd column is the 2nd part of the post code (these are all City of Westminster post codes so the start should be the same), and the 3rd column is the score: if it's negative the street name is female, positive is male and 0 signifies gender neutral.

The results of the larger dataset are in second_results.csv. These are also 3 columns. The first is the streetname and the first half of the postcode, the second is the gender score (postive for male, negative for female, 0 for gender neutral). The 3rd column has some XML stuff in it - I wouldn't worry about that.
