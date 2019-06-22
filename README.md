# VAM test

Example of data processing from remote sources.

## Basic information

Two solutions are provided here, one easy and one more complex (in case requirements are to be intended on the hard side. See the design doc for more details).
This code assumes a local MongoDB exists with a `testdb` database instance.

### Easy version

Just invoke `easy.py` with a dataset id to read the current content of the dataset and save it in the db.

This represents a 'quick time to market with some value' solution, without making the system overly complex unless needed.

### Hard version

This involves a scheduler and a worker, plus a AWS configuration. While the code is provided here, a full working environment is out of scope.