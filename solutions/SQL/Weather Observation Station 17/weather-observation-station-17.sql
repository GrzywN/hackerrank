SELECT ROUND(Long_w, 4) FROM Station WHERE Lat_n IN (SELECT MIN(Lat_n) FROM Station WHERE Lat_n > 38.7780);
