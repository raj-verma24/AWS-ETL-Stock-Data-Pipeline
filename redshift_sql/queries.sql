-- Retrieve highest stock price for each day
SELECT trade_time, stock_price 
FROM stock_prices
WHERE stock_price = (SELECT MAX(stock_price) FROM stock_prices GROUP BY trade_time);

-- Find the average stock price per day
SELECT trade_time, AVG(stock_price) AS avg_price 
FROM stock_prices
GROUP BY trade_time;

-- Identify potential stock price trends
SELECT trade_time, stock_price, 
       LAG(stock_price) OVER (ORDER BY trade_time) AS previous_price,
       stock_price - LAG(stock_price) OVER (ORDER BY trade_time) AS price_change
FROM stock_prices;