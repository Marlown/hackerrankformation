--Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.--
--The CITY table is described as follows:--
select c.* from city c
where
c.population > 100000
and
c.countrycode = 'USA';

-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.--
select name from city c
where
c.population > 120000 
and
c.countrycode = 'USA';

--Query all columns (attributes) for every row in the CITY table.The CITY table is described as follows:  --
select * from city.c

--Query all columns for a city in CITY with the ID 1661. --
select * from city.c
where
c.id= 1661;

--Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN. --
SELECT * FROM city.c WHERE C.COUNTRYCODE='JPN';

-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN. --
SELECT name FROM city.c WHERE c.COUNTRYCODE='JPN';

-- Query a list of CITY and STATE from the STATION table. --
SELECT CITY,STATE FROM STATION;

-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer. --
SELECT DISTINCT CITY from STATION WHERE  MOD(ID,2)=0;

-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table. --
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;