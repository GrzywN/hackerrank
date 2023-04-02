SELECT ROUND(Long_w, 4) FROM Station WHERE Lat_n IN (SELECT MAX(Lat_n) AS max_lat_n FROM Station WHERE Lat_n < 137.2345);
