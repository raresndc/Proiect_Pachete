PROC IMPORT DATAFILE="/home/u63359198/Proiect/AirPod_annual_sales.csv"
            OUT=dataset_airPod
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

PROC PRINT DATA=dataset_airPod;
	TITLE 'AirPod annual sales';
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/Apple_watch_sales.csv"
            OUT=dataset_appleWatch
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

PROC PRINT DATA=dataset_appleWatch;
	TITLE 'Apple Watch annual sales';
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/HomePod_annual_sales.csv"
            OUT=dataset_homePod
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

PROC PRINT DATA=dataset_homePod;
	TITLE 'HomePod annual sales';
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/iPad_annual_sales.csv"
            OUT=dataset_iPad
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

PROC PRINT DATA=dataset_iPad;
	TITLE 'iPad annual sales';
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/iPhone_annual_sales.csv"
            OUT=dataset_iPhone
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

PROC PRINT DATA=dataset_iPhone;
	TITLE 'iPhone annual sales';
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/Mac_annual_sales.csv"
            OUT=dataset_Mac
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

PROC PRINT DATA=dataset_Mac;
	TITLE 'Macbook annual sales';
RUN;

/*---------------------------subseturi de date---------------------------*/

DATA airPod_subset;
	SET dataset_airPod;
	WHERE year > 2017;
RUN;

PROC PRINT DATA=airpod_subset;
	TITLE 'Subset Air Pod (year > 2017)';
RUN;

/*---------------------------appleWatch---------------------------*/

DATA appleWatch_subset;
   SET dataset_appleWatch;
   WHERE year > 2017;
RUN;

PROC PRINT DATA=appleWatch_subset;
	TITLE 'Subset Apple Watch (year > 2017)';
RUN;

/*---------------------------iPad---------------------------*/

DATA iPad_subset;
   SET dataset_iPad;
   WHERE year > 2017;
RUN;

PROC PRINT DATA=iPad_subset;
	TITLE 'Subset iPad (year > 2017)';
RUN;

/*---------------------------iPhone---------------------------*/

DATA iPhone_subset;
   SET dataset_iPhone;
   WHERE year > 2017;
RUN;

PROC PRINT DATA=iPhone_subset;
	TITLE 'Subset iPhone (year > 2017)';
RUN;

/*---------------------------Mac---------------------------*/

DATA MacBook_subset;
   SET dataset_Mac;
   WHERE year > 2017;
RUN;

PROC PRINT DATA=MacBook_subset;
	TITLE 'Subset MacBook (year > 2017)';
RUN;

/*---------------------------combinare seturi de date---------------------------*/

/*---------------------------airpod---------------------------*/
DATA airPod_subset_redenumit;
	SET airPod_subset;
	RENAME 'Sales (mm)'n = 'airpod_subset_Sales(mm)'n;
RUN;

PROC SORT DATA=airPod_subset_redenumit;
	BY year;
RUN;

/*---------------------------apple watch---------------------------*/

DATA appleWatch_subset_redenumit;
	SET appleWatch_subset;
	RENAME 'Sales (mm)'n = 'appleWatch_subset_Sales(mm)'n;
RUN;

PROC SORT DATA=appleWatch_subset_redenumit;
	BY year;
RUN;

/*---------------------------home pod---------------------------*/

DATA homePod_subset_redenumit;
	SET dataset_homePod;
	RENAME 'Sales (mm)'n = 'homePod_subset_Sales(mm)'n;
RUN;

PROC SORT DATA=homePod_subset_redenumit;
	BY year;
RUN;

/*---------------------------iPad---------------------------*/

DATA iPad_subset_redenumit;
	SET ipad_subset;
	RENAME 'Sales (mm)'n = 'ipad_subset_Sales(mm)'n;
RUN;

PROC SORT DATA=iPad_subset_redenumit;
	BY year;
RUN;

/*---------------------------iPhone---------------------------*/

DATA iPhone_subset_redenumit;
	SET iphone_subset;
	RENAME 'Sales (mm)'n = 'iphone_subset_Sales(mm)'n;
RUN;

PROC SORT DATA=iPhone_subset_redenumit;
	BY year;
RUN;

/*---------------------------mac---------------------------*/

DATA macbook_subset_redenumit;
	SET MacBook_subset;
	RENAME 'Sales (mm)'n = 'macbook_Sales(mm)'n;
RUN;

PROC SORT DATA=macbook_subset_redenumit;
	BY year;
RUN;

/*---------------------------combinare seturi redenumite---------------------------*/

DATA subset_combinat;
   MERGE airPod_subset_redenumit (IN=a) appleWatch_subset_redenumit (IN=b) 
   homePod_subset_redenumit (IN=c) iPad_subset_redenumit (IN=d) 
   iPhone_subset_redenumit(IN=e) macbook_subset_redenumit (IN=f); 
   BY Year;
RUN;

PROC PRINT DATA=subset_combinat;
	TITLE 'Subset de date combinat (year > 2017)';
RUN;

/*---------------------------combinare seturi prin procedura SQL---------------------------*/

/*redenumiri*/
/*airpod*/

DATA dataset_airPod_redenumit;
	SET dataset_airPod;
	RENAME 'Sales (mm)'n = 'airpod_dataset_Sales(mm)'n;
RUN;

/*apple watch*/

DATA dataset_appleWatch_redenumit;
	SET dataset_appleWatch;
	RENAME 'Sales (mm)'n = 'dataset_appleWatch_Sales(mm)'n;
RUN;

/*home pod*/

DATA dataset_homePod_redenumit;
	SET dataset_homePod;
	RENAME 'Sales (mm)'n = 'dataset_homePod_Sales(mm)'n;
RUN;

/*iPad*/

DATA dataset_iPad_redenumit;
	SET dataset_iPad;
	RENAME 'Sales (mm)'n = 'dataset_ipad_Sales(mm)'n;
RUN;

/*iPhone*/

DATA dataset_iPhone_redenumit;
	SET dataset_iPhone;
	RENAME 'Sales (mm)'n = 'dataset_iphone_Sales(mm)'n;
RUN;

/*Mac*/

DATA dataset_macbook_redenumit;
	SET dataset_Mac;
	RENAME 'Sales (mm)'n = 'dataset_macbook_Sales(mm)'n;
RUN;

/*combinare date prin procedura SQL*/

PROC SQL;
	CREATE TABLE dataset_combinat AS
	SELECT *
	FROM dataset_iPhone_redenumit
	FULL JOIN dataset_macbook_redenumit ON dataset_iPhone_redenumit.Year = dataset_macbook_redenumit.Year
	FULL JOIN dataset_airPod_redenumit ON dataset_iPhone_redenumit.Year = dataset_airPod_redenumit.Year
	FULL JOIN dataset_appleWatch_redenumit ON dataset_iPhone_redenumit.Year = dataset_appleWatch_redenumit.Year
	FULL JOIN dataset_homePod_redenumit ON dataset_iPhone_redenumit.Year = dataset_homePod_redenumit.Year
	FULL JOIN dataset_iPad_redenumit ON dataset_iPhone_redenumit.Year = dataset_iPad_redenumit.Year;
QUIT;

PROC PRINT DATA=dataset_combinat;
	TITLE 'Dataset combinat';
RUN;

/*-----------------------suma pe coloane-----------------------*/

/* PROC MEANS DATA=dataset_combinat SUM MISSING; */
/*     VAR dataset_iphone_Sales(mm)-dataset_ipad_Sales(mm); */
/*     CLASS year; */
/*     OUTPUT OUT=suma_coloane (DROP=_TYPE_ _FREQ_) SUM=; */
/* RUN; */

DATA dataset_combinat_redenumit;
	SET dataset_combinat;
	RENAME 'dataset_iphone_Sales(mm)'n= 'sales1'n
	'dataset_macbook_Sales(mm)'n= 'sales2'n
	'airpod_dataset_Sales(mm)'n= 'sales3'n
	'dataset_appleWatch_Sales(mm)'n= 'sales4'n
	'dataset_homePod_Sales(mm)'n= 'sales5'n
	'dataset_ipad_Sales(mm)'n= 'sales6'n;
RUN;

PROC PRINT DATA=dataset_combinat_redenumit;
	TITLE 'dataset_combinat_redenumit';
RUN;

PROC UNIVARIATE DATA=dataset_combinat_redenumit noprint;
  VAR sales3;
  HISTOGRAM ;
  TITLE "Histograma pentru revenue iPhone";
RUN;



/*---------------suma pe liniile care nu au valori lipsa---------------*/

DATA suma_coloane;
    SET dataset_combinat_redenumit;

    array col_array(*) sales1-sales6;

    suma = 0;

    DO i = 1 TO dim(col_array);
        suma = suma + col_array(i);
    END;

    KEEP year suma;

RUN;

PROC PRINT DATA=suma_coloane;
	TITLE 'Suma sales pentru anii comuni';
RUN;

/*---------------suma pe toate liniile---------------*/

DATA suma_coloane1;
    SET dataset_combinat_redenumit;

    suma = SUM(of sales1-sales6);

    KEEP year suma;

RUN;

PROC PRINT DATA=suma_coloane1;
	TITLE 'Suma sales pentru toti anii';
RUN;

/*---------------calcul valori lipsa in dataset---------------*/

DATA valori_lipsa;
	set dataset_combinat_redenumit;
	numar_valori_lipsa = NMISS(sales1, sales2, sales3, sales4, sales5, sales6);
RUN;

PROC PRINT DATA=valori_lipsa;
RUN;

/*---------------calcul medii---------------*/

proc means data = dataset_combinat_redenumit noprint;
var sales1 sales2 sales3 sales4 sales5 sales6;
output out=calcul_medii;
run;

PROC PRINT DATA=calcul_medii;
	TITLE 'Medie pe categorii de produse';
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/iPad_annual_revenue.csv"
            OUT=dataset_iPad
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

DATA dataset_iPad_redenumit;
	SET dataset_iPad;
	RENAME 'Revenue'n = 'iPadRevenue'n;
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/iPhone_annual_revenue.csv"
            OUT=dataset_iPhone
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

DATA dataset_iPhone_redenumit;
	SET dataset_iPhone;
	RENAME 'Revenue'n = 'iPhoneRevenue'n;
RUN;

PROC IMPORT DATAFILE="/home/u63359198/Proiect/Mac_annual_revenue.csv"
            OUT=dataset_Mac
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

DATA dataset_Mac_redenumit;
	SET dataset_Mac;
	RENAME 'Revenue'n = 'MacRevenue'n;
RUN;


PROC IMPORT DATAFILE="//home/u63359198/Proiect/Wearable_home_and_accessories_annual_revenue.csv"
            OUT=dataset_Wearable_and_accessories
            DBMS=CSV
            REPLACE;
    GETNAMES=YES;
RUN;

DATA dataset_W_and_A_redenumit;
	SET dataset_Wearable_and_accessories;
	RENAME 'Revenue'n = 'WearableAndAccessoriesRevenue'n;
RUN;

PROC SQL;
	CREATE TABLE dataset_revenues AS
	SELECT *
	FROM dataset_iPhone_redenumit
	FULL JOIN dataset_Mac_redenumit ON dataset_iPhone_redenumit.Year = dataset_Mac_redenumit.Year
	FULL JOIN dataset_iPad_redenumit ON dataset_iPhone_redenumit.Year = dataset_iPad_redenumit.Year
	FULL JOIN dataset_W_and_A_redenumit ON dataset_iPhone_redenumit.Year = dataset_W_and_A_redenumit.Year;
QUIT;

PROC PRINT DATA=dataset_revenues;
	TITLE 'Dataset revenues';
RUN;

proc format;
value iPhoneRevenue low-50 = 'Revenue slab' 50-100 = 'Revenue mediu' 100-150 ='Revenue mare' 150-high = 'Revenue semnificativ';
run;

title "Date cu format";
proc print data = dataset_iPhone_redenumit;
var iPhoneRevenue;
format iPhoneRevenue iPhoneRevenue.;
run;

DATA suma_coloane_revenues;
    SET dataset_revenues;

    array col_array(*) iPhoneRevenue MacRevenue iPadRevenue WearableAndAccessoriesRevenue;

    suma = 0;

    DO i = 1 TO dim(col_array);
        suma = suma + col_array(i);
    END;

    KEEP year suma;

RUN;

PROC PRINT DATA=suma_coloane_revenues;
	TITLE 'Suma revenue pentru anii comuni';
RUN;

DATA suma_coloane_revenues2;
    SET dataset_revenues;

    suma = SUM(of iPhoneRevenue MacRevenue iPadRevenue WearableAndAccessoriesRevenue);

    KEEP year suma;

RUN;

PROC PRINT DATA=suma_coloane_revenues2;
	TITLE 'Suma revenue pentru toti anii';
RUN;

proc format;
value suma low-100 = 'Revenue slab' 100-150 = 'Revenue mediu' 150-250 ='Revenue mare' 250-high = 'Revenue semnificativ';
run;

title "Suma revenue pentru toti anii cu format";
proc print data = suma_coloane_revenues2;
var suma;
format suma suma.;
run;
