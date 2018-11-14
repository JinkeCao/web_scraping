SELECT s, count(1)
FROM etl.idata_log
LATERAL VIEW explode(split(running_services,"\;")) a AS s
GROUP BY s;

select c.ser, c.con,count(distinct c.dvc) 
from (
select b.dvc as dvc, b.s as ser, count(distinct b.day_time) as con 
from (
select dvc, s, day_time
from etl.idata_log
lateral view explode(split(running_services,"\;")) a as s
) b
group by b.dvc, b.s
) c
group by c.ser, c.con
