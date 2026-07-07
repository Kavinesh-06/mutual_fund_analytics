SELECT
    f.scheme_name,
    a.aum
FROM fact_aum a
JOIN dim_fund f
ON a.fund_id = f.fund_id
ORDER BY a.aum DESC
LIMIT 5;

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    f.scheme_name,
    p.expense_ratio
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id=f.fund_id
WHERE expense_ratio<1;

SELECT
    f.scheme_name,
    p.return_5y
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id=f.fund_id
ORDER BY return_5y DESC
LIMIT 10;

SELECT
    f.category,
    AVG(p.return_3y) AS average_return
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id=f.fund_id
GROUP BY f.category;

SELECT
    f.fund_house,
    AVG(n.nav) AS average_nav
FROM fact_nav n
JOIN dim_fund f
ON n.fund_id=f.fund_id
GROUP BY f.fund_house
ORDER BY average_nav DESC;

SELECT
    transaction_id,
    amount,
    transaction_type
FROM fact_transactions
ORDER BY amount DESC
LIMIT 1;

SELECT
    category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;
