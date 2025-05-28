SELECT id, fish_name, length
FROM (
  SELECT id, fish_name, length,
         RANK() OVER (PARTITION BY fish_name ORDER BY length DESC) AS rnk
  FROM fish_info
  NATURAL JOIN fish_name_info
) AS ranked
WHERE rnk = 1
ORDER BY id ASC