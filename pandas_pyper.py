import pandas
import pyper

# Read the CSV file
df = pandas.read_csv("tmp.csv")

# Make the connection to R
r = pyper.R(use_pandas = True)

# load the data into R. The data that I load in is a pandas data frame.
r.r_data = df

# perform some R calculation. In this case, doing some loess smoothing.
r("r_mean <- r_data")
r("fit <- loess(r_data$value ~ r_data$coordinate)")
r("r_mean$fitted <- predict(fit)")

# extract the value from the r connection. Again, this is a pandas data frame.
output = r.r_mean
