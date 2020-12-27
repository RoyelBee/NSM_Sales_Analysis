
import Functions.db_connection as dbc 
import pandas as pd

df = pd.read_sql_query(""" 
DECLARE @DATE AS SMALLDATETIME = GETDATE()
DECLARE @FIRSTDATEOFMONTH AS SMALLDATETIME = CONVERT(SMALLDATETIME, CONVERT(CHAR(4),YEAR(@DATE)) + '-' + CONVERT(CHAR(2),MONTH(@DATE)) + '-01')
DECLARE @YESTERDAY AS SMALLDATETIME = DATEADD(d,-1,@DATE)

DECLARE @FIRSTDATEOFMONTH_STR AS CHAR(8)=CONVERT(VARCHAR(10), @FIRSTDATEOFMONTH , 112)
DECLARE @YESTERDAY_STR AS CHAR(8)=CONVERT(VARCHAR(10), @YESTERDAY , 112)

select NSMNAME, FF.RSMTR,right(TRANSDATE, 2) as TRANSDATE,
ITEM,ItemName,BRAND, isnull(SalesQTY, 0) as SalesQTY, isnull(SalesValue, 0) as SalesValue, isnull(retval,0) as retval,
isnull(TarQTY, 0) TarQTY, isnull(TarVal,0) as  TarVal
from (select distinct RSMTR, NSMNAME from RFieldForce
where YEARMONTH=left(@FIRSTDATEOFMONTH_STR,6)) as FF
left join 
(select RSMTR,ITEM, TRANSDATE,SUM(QTYSHIPPED) as SalesQTY,SUM(EXTINVMISC) as SalesValue,
SUM(case when TRANSTYPE=2 then EXTINVMISC end) as retval
from OESalesDetails
where TRANSDATE between @FIRSTDATEOFMONTH_STR and @YESTERDAY_STR 
group by RSMTR,ITEM,TRANSDATE) as sales
on ff.RSMTR=sales.RSMTR
left join 
(select ITEMNO, [DESC] as ItemName, BRAND from PRINFOSKF) as item
on  item.ITEMNO=sales.ITEM
left join 
(select RSMTR, ITEMNO, SUM(QTY) as TarQTY, SUM([VALUE]) as TarVal from [ARCSECONDARY].dbo.RfieldForceProductTRG
where YEARMONTH=left(@FIRSTDATEOFMONTH_STR,6) 
group by RSMTR, ITEMNO) as tar
on sales.ITEM=tar.ITEMNO and sales.RSMTR=tar.RSMTR
where ITEM='1667' and FF.RSMTR='RN'
order by TRANSDATE asc
""", dbc.connection)

df.to_csv('Data/Master_data.csv', index=False)