-- List number of records with same score in second_table hbtn_0c_0
SELECT score, COUNT(score) AS number FROM second_table AS C
GROUP BY score
ORDER BY score DESC;
