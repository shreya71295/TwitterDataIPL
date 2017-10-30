# TwitterDataIPL
This project aims at extracting live twitter data (use case IPL) and analyse it using R studio.

This project explores all the areas of Data mining, i.e. data extraction, data mining (cleaning and transformation), API’s,
search modules, python, tweepy and R. The analysis in this project deals with the various measures by which
popularity of IPL teams can be determined in comparison with each other.

The motivation behind this project is to see just how popular IPL is and which team wins the crown of the Most Popular IPL 
team. The analysis would show which teams makes people go crazy when they go on the field and battle for the ultimate IPL 
winner title. This project is yet to be extended to achieve this goal. but completes the data extraction part using Python.

# Implementation

The Implementation of this project has been broadly done in two parts:
- Extraction of data with the help of Python
- visualization of extracted data using R-studio.

# PART I: Extraction of data with the help of Python and Twitter APIs.

- Tokenisation 

After the authentication of the Twitter Application is done, the following python scripts are
run to extract data using Twitter APIs. The following are the different ways in which we can
interact with the twitter APIs to extract data:

- tw.py : It is used to collect the keywords from the streaming API. For all the twitter statuses which have the keywords 
          specified
- P12.py: This script not only collects the tweets but also saves them in a CSV format along with the time of the tweet
- Hh.py : Collects the raw data in JSON format. The tweepy library is intialized with the twitter API so that raw JSON tweets
          of a particular time can be collected, as mentioned in the script
- Jsl.py : Gathers more information but with an understanding that the tweets are in raw JSON format. The encoding here can
           be a bit challenging
           
I used Py.12 where analysis is in the CSV format rather than JSON, because CSV format is easier to read and
manipulate rather than JSON.

PRETTYTABLE ANALYSIS is done through ppp.py and team1.py

# PART II: Visualization of Extracted Data Using R Studio

For visualizing Twitter data in R, we first need to authenticate Twitter with our R studio.

To do so, the following packages are installed in R:
- twitteR- twitteR is an R package which provides access to the Twitter API. We
use it to extract data from Twitter by accessing Twitter API.
- devtools- The aim of devtools is to make package development easier by
providing R functions that simplify common tasks.
- rjson –This package is used to convert R object into JSON objects and vice-
versa.
- bit64 - Package 'bit64' provides serializable S3 atomic 64bit (signed) integers
that can be used in vectors, matrices, arrays and data frames
- httr - Configuration functions make it easy to control additional request
components (authenticate(), add_headers() and so on).

For graph analysis, the following R packages were installed:

- readr- Read flat/tabular text files from disk (or a connection).
- dplyr - is the next iteration of plyr, focussed on tools for working with data
frames (hence the d in the name).
- lubridate - The 'lubridate' package has a consistent and memorable syntax that
makes working with dates easy and fun.
- streamgraph - Streamgraphs are a generalization of stacked area graphs where
the baseline is free. By shifting the baseline, it is possible to minimize the
change in slope (or wiggle) in individual series, thereby making it easier to
perceive the thickness of any given layer across the data
- htmlwidget - The htmlwidget-Package offers a way to save the pieces for the
widget separately. htmlwidgets are designed to be R packages, so what makes
a good package also makes a good htmlwidget.
- Plotly - Plotly is an R package for creating interactive web-based graphs via
the open source JavaScript graphing library plotly.js

The BoxPlot R script is used for the comparison between various IPL teams for the required analysis.
