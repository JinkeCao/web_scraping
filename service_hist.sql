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

create table jkcao.service_day(dvc string, serivice_day map<string,string>);
insert into table jkcao.service_day
select c.dvc, str_to_map(
    concat_ws(
        ",",collect_set(
            concat_ws(
                ":",c.ser, cast(c.con as string)
            )
        )
    )
)
from (
    select b.dvc as dvc, b.s as ser, count(distinct b.day_time) as con 
    from (
        select dvc, s, day_time
        from etl.idata_log
        lateral view explode(
            split(running_services,"\;")
        ) a as s
    ) b
    group by b.dvc, b.s
) c
group by c.dvc;
