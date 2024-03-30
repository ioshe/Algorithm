SELECT 
  CASE
    -- For even IDs, subtract 1 to swap with the previous ID
    WHEN MOD(id, 2) = 0 THEN id - 1
    -- For odd IDs, check if it's the last ID, if not, add 1 to swap with the next ID
    WHEN id = (SELECT MAX(id) FROM Seat) THEN id
    ELSE id + 1
  END AS id,
  student
FROM Seat
ORDER BY id ASC;