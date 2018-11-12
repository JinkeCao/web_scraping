SELECT s, count(1)
FROM etl.idata_log
LATERAL VIEW explode(split(running_services,"\;")) a AS s
GROUP BY s;
