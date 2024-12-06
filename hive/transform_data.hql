INSERT INTO TABLE syed_sample
SELECT flight_id, carrier, origin, destination, dep_delay, arr_delay,
CASE
    WHEN dep_delay <= 0 AND arr_delay <= 0 THEN 'N'
    ELSE 'Y'
END AS delayed
FROM year_data
TABLESAMPLE (30 ROWS);
