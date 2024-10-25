SELECT
  c.Country as CustomerState,
  SUM(CASE WHEN YEAR(od2.OrderDate) = 2023 AND MONTH(od2.OrderDate) = 7 THEN od1.UnitPrice * od1.Quantity ELSE 0 END) AS JulySales2023,
  SUM(CASE WHEN YEAR(od2.OrderDate) = 2022 AND MONTH(od2.OrderDate) = 7 THEN od1.UnitPrice * od1.Quantity ELSE 0 END) AS JulySales2022
FROM
  Customers c, Orders od2, Order_Details od1
WHERE 
  c.CustomerID = od2.CustomerID
  AND od1.OrderID = od2.OrderID
GROUP BY
  c.Country;