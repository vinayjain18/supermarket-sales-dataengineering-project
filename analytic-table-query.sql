CREATE or replace table `data-analytics-project-388113.supermarket_dataengineering_project.tbl_analytics` AS (
select 
f.Id,
f.Invoice_ID,
b.Branch,
c.City,
g.Gender,
cust.Customer_type,
t.Time,
t.purchase_hour,
d.Date,
d.purchase_day,
d.purchase_month,
d.purchase_year,
prod.Product_line,
p.Payment,
f.Unit_price,
f.Quantity,
f.Tax_5_percent,
f.Total,
f.cogs,
f.gross_margin_percentage,
f.gross_income,
f.Rating

from `data-analytics-project-388113.supermarket_dataengineering_project.fact_table` f   
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.branch_dim` b ON b.branch_id=f.branch_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.city_dim` c ON c.city_id=f.city_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.customer_type_dim` cust ON cust.customer_type_id=f.customer_type_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.date_dim` d ON d.date_id=f.date_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.time_dim` t ON t.time_id=f.time_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.gender_dim` g ON g.gender_id=f.gender_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.payment_type_dim` p ON p.payment_type_id=f.payment_type_id
JOIN `data-analytics-project-388113.supermarket_dataengineering_project.product_type_dim` prod ON prod.product_type_id=f.product_type_id);
