select * from covidinmatetesting; /*total 305 entries in table */
/*oldest reporting date is May 8 2020, latest reporting date is August 5 2020*/

/*query to determine table columns */
select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'covidinmatetesting';
/* the columns in this database are Reporting Date, Region (in Ontario), Cumulative Number of Tests as of Reporing Date (in the specified region), Cumulative Number of Positive Tests as of Reporting Date,
Cumulative number of Negative tests, Total Number of tests pending on date, Total number of inmates refusing swab as of date, Total number of inmates in medical isolation as of date. */

/*query to determine unique Region values */
select distinct Region from covidinmatetesting;
/*distinct regions are Central, Eastern, Northern, Toronto and Western*/

/*query to determine most number of pending tests on a single date for each region*/
select Region, MAX(Total_Number_of_Pending_Tests_on_Reporting_Date) from covidinmatetesting group by Region order by 2 desc;
/*Western region had the most pending tests in one day with 211 tests, followed by Eastern with 211, Toronto with 204, Central with 149 and Northern with 129. */

/*query what is the total number of tests done in each region as of the latest reported date?*/
select Region, MAX(Cumulative_Number_of_Tests_as_of_Reporting_Date) from covidinmatetesting group by Region order by 2 desc;
/*Central region had the most number of tests done in total with 2084 tests, followed by Eastern with 2006, Western with 1467, Northern in 1138 and Toronto with 1092.*/

/*querying all entries of Toronto region in database */
select * from covidinmatetesting where Region = 'Toronto'
/* 61 total entries,  oldest reporting date listed 109 total tests done, latest reporting date listed 1092 total tests done*/

/*does receiving positive tests correlate with the number of inmates in medical isolation in Toronto?*/
select Reporting_Date, Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date as 'Number of positive tests as of date', Total_Inmates_on_Medical_Isolation_as_of_Reporting_Date as 'Number of inmates in isolation' from covidinmatetesting where Region = 'Toronto';
/*No clear correlation between increase in positive tests and number of inmates kept in medical isolation. Number of inmates in isolation dramatically increases or decreases regardless in the increase of positive tests.*/
 
 /*What is the trend of Toronto inmates refusing swabs for testing?*/
 select Reporting_Date, Total_Inmates_that_Refused_Swab_as_of_Reporting_Date as 'Total inmates refusing swabs' from covidinmatetesting where Region = 'Toronto';
 /*From May 8 to May 22, no inmates were recorded refusing swabs, May 25 has 13 recorded refusals and May 26 has 655 recorded refusals with continued increase since to the latest date.
 Cause of significant increase on May 26 is unknown.
 From latest reporting date total number of inmates that have refused swabs in Toronto area is 1119.*/

 select * from covidinmatetesting where Region='Northern'; /*shows all entries with Northern region*/
 /* what is the difference between the oldest date of number of tests and latest date number of tests? */
 select MAX(Cumulative_Number_of_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Northern';
 /*1066 tests have been done from the oldest to latest reported dates*/
 /*How many more positive cases have been confirmed?*/
 select MAX(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Northern';
 /*Only four additional positive cases were confirmed from the oldest to latest reported date.
 How many negative cases were confirmed? */
 select MAX(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Northern';
 /*1022 additional negatice cases were confirmed from the oldest to latest reported date.
 How many pending tests were there by the latest reported date?*/
select Reporting_Date, Total_Number_of_Pending_Tests_on_Reporting_Date from covidinmatetesting where Region = 'Northern'; /*Number of pending tests on the latest date were 41 tests*/
 /*Are these numbers similar to the other Ontario regions?*/
 select MAX(Cumulative_Number_of_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Eastern';
 select MAX(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Eastern';
 select MAX(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Eastern';
 select Reporting_Date, Total_Number_of_Pending_Tests_on_Reporting_Date from covidinmatetesting where Region = 'Eastern'
 /*difference of number of cases from oldest to latest date in Eastern region is 1922 cases*/
 /*difference of number of positive cases from oldest to latest date in Eastern region is 2 cases*/
 /*difference of number of negative cases from oldest to latest date in Eastern region is 1839 cases*/
 /*Number of pending tests on the latest date in Eastern region were 81 tests*/
 select MAX(Cumulative_Number_of_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Central';
 select MAX(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Central';
 select MAX(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Central';
 select Reporting_Date, Total_Number_of_Pending_Tests_on_Reporting_Date from covidinmatetesting where Region = 'Central'
 /*difference in number of cases was 1754, number of new positive cases is 21, number of negative cases is 1683, total number of pending tests on latest date is 73 cases*/
 select MAX(Cumulative_Number_of_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Western';
 select MAX(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Western';
 select MAX(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Western';
 select Reporting_Date, Total_Number_of_Pending_Tests_on_Reporting_Date from covidinmatetesting where Region = 'Western'
 /*difference in number of cases was 1385, number of new positive cases is 3, number of negative cases is 1288, total number of pending tests on latest date is 92 cases*/
 select MAX(Cumulative_Number_of_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Toronto';
 select MAX(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Positive_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Toronto';
 select MAX(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) - MIN(Cumulative_Number_of_Negative_Tests_as_of_Reporting_Date) from covidinmatetesting where Region = 'Toronto';
 select Reporting_Date, Total_Number_of_Pending_Tests_on_Reporting_Date from covidinmatetesting where Region = 'Toronto'
 /*difference in number of cases was 983, number of new positive cases is 11, number of negative cases is 778, total number of pending tests on latest date is 198 cases*/

 /*Loading up table into COVID-19 database titled 'Status of COVID-19 cases in Ontario’s Provincial Correctional Institutions */


