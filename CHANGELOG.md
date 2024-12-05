### v0.1.7  

* Add `BigQueryCatalog`.

### v0.1.6  

* Refactor the `Catalog` class.

### v0.1.5  

* Improve efficiency of `PiiDetectionPipeline` by reusing the samples fetched from the tables.

### v0.1.4  

* Make database dependencies optional. This requires installing each database dependency as an extra. For example, `pip install detectpii[postgres]`