SELECT
    p.ProductName,
	SUM(CASE WHEN YEAR(o.OrderDate) = 2022 AND MONTH(o.OrderDate) = 6 THEN (p.Price * od.Quantity) ELSE 0 END) AS June2022,
    SUM(CASE WHEN YEAR(o.OrderDate) = 2022 AND MONTH(o.OrderDate) = 7 THEN (p.Price * od.Quantity) ELSE 0 END) AS July2022,
    CASE
        WHEN SUM(CASE WHEN YEAR(o.OrderDate) = 2022 AND MONTH(o.OrderDate) = 6 THEN (p.Price * od.Quantity) ELSE 0 END) = 0
        THEN '100%'
        ELSE
            CONCAT(ROUND((((SUM(CASE WHEN YEAR(o.OrderDate) = 2022 AND MONTH(o.OrderDate) = 7 THEN (p.Price * od.Quantity) ELSE 0 END) - 
                SUM(CASE WHEN YEAR(o.OrderDate) = 2022 AND MONTH(o.OrderDate) = 6 THEN (p.Price * od.Quantity) ELSE 0 END)) / 
                (SUM(CASE WHEN YEAR(o.OrderDate) = 2022 AND MONTH(o.OrderDate) = 6 THEN (p.Price * od.Quantity) ELSE 0 END))) * 100), 2), '%')
    END AS Growth
FROM
    Products p
INNER JOIN Order_Details od ON p.ProductID = od.ProductID
INNER JOIN Orders o ON od.OrderID = o.OrderID
GROUP BY
    p.ProductName;