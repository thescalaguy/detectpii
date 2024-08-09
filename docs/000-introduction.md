detectpii is a library that aims to find PII stored in tables. It does so by scanning the table's schema and values for potentially PII values.

<p align="center">
    <img src="./img/detectpii.png" />
</p>

The library consists of three main components -- the `PiiDetectionPipeline`, the `Scanner`s, and `Catalog`s. Their relationship is shown in the diagram above. 
A pipeline consists of a catalog, which describes the table and columns, and scanners, which scan the tables and columns. The two scanners that the 
library ships with scan the column name and column values using regular expressions. These are built on top of piicatcher and CommonRegex. To add more catalogs and scanners, 
simply inherit from the `Catalog` and `Scanner` class, and implement the appropriate methods.

<p align="center">
    <img src="./img/resolver.png" />
</p>

Similarly, there are `Resolver`s which are used to fetch the credentials from an external store.   

By default, every catalog uses the `PlaintextResolver` which requires that all credentials be passed in plaintext. This is only 
meant for use within the development environment and poses a security risk when used in production. Other resolvers can be added 
for secure stores like SSM, etc.
