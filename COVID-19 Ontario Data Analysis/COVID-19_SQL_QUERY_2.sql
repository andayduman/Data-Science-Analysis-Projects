select * from correctionsinmatecases;
/*columns of table is Reporting Date, Region, Institution, Total Ongoing Active Inmate Cases, Cumulative Number of Resolved Inmate Cases, Cumulative Number of Positive Inmate Cases Released from Custody*/
/*which regions values are in this table?*/

select distinct Region from correctionsinmatecases; /*Regions are Central, Eastern, Northern, Toronto and Western */

/*what are the unique institutions in this table and the Region where they are located? */

select distinct Institution, Region from correctionsinmatecases order by 2;

/*Eastern has Central East Correctional Centre, Central has Hamilton Wentworth Det Centre, Maplehurst Correctional Complex, Milton-Vanier Centre For Women, Niagara Detention Centre, Ontario Correctional Institute.  
Northern has Kenora Jail, Monteith Correctional Centre. Toronto has Toronto South Detention Centre. Western has Central North Correctional Centre, Elgin-Middlesex Det. Centre*/
/*How many ongoing cases were there on the oldest reporting date?*/

select max(Total_Ongoing_Active_Inmate_Cases_as_of_Reporting_Date), Institution from correctionsinmatecases where Reporting_Date = '2020-05-08 00:00:00.0000000' group by Institution;

/* The institution with the most ongoing inmate cases on first reported date was 71 cases at Ontario Correctional Institute in the Central region */

select max(Total_Ongoing_Active_Inmate_Cases_as_of_Reporting_Date), Institution from correctionsinmatecases where Reporting_Date = '2020-08-09 00:00:00.0000000' group by Institution;

/* the institution with the most ongoing inmate cases on latest reported date is only 1 case at Central East Correctional Centre in the Eastern region, all other values are NULL*/
/*what institution at which date had the most ongoing active inmate cases? */

select Institution, max(Total_Ongoing_Active_Inmate_Cases_as_of_Reporting_Date),Reporting_Date from correctionsinmatecases group by Institution, Reporting_Date order by 2 desc ; 

/*Ontario Correctional Institute had the most active cases at any given point with 76 active cases on May 15 and May 19 */

/*How many institutions have 'Ontario' in the name?*/
select count(distinct Institution) from correctionsinmatecases where Institution like '%Ontario%'; /*Only one institution has string 'Ontario' in its name */

/*How many times did each institution have no active inmate cases?*/
select Institution, count(*) from correctionsinmatecases where Total_Ongoing_Active_Inmate_Cases_as_of_Reporting_Date is null group by Institution order by 2 desc; 

/*Monteith Correctional Centre had most dates with no ongoing active inmate cases with 63 dates, Central North Correctional Centre with 35 dates*/

/*Merging tables*/

select * from correctionsinmatecases 
left join covidinmatetesting on
correctionsinmatecases.Reporting_Date = covidinmatetesting.Reporting_Date;

