# aqui tenho o sum de cada venda que foi vendida ou cancelada
select p.producer_id, sum(case when s.cancelled = 1 or s.refund = 1 then s.product_price else 0 end) as total_money_lost,
       SUM(CASE WHEN s.cancelled = 1 THEN s.product_price ELSE 0 END) AS total_money_lost_canceled,
       SUM(CASE WHEN s.refund = 1 THEN s.product_price ELSE 0 END) AS total_money_lost_refund
from producer p
         join product p2 on p.producer_id = p2.producer_id
         join sales s on p2.product_id = s.product_id
group by p.producer_id
order by total_money_lost desc


# considerando com o recovery ativado
select p.producer_id, sum(case when s.cancelled = 1 or s.refund = 1 then s.product_price else 0 end) as total_money_lost,
       sum(CASE WHEN s.cancelled = 1 THEN s.product_price ELSE 0 END) AS canceled,
       sum(CASE WHEN s.refund = 1 THEN s.product_price ELSE 0 END) AS refund
from producer p
         join product p2 on p.producer_id = p2.producer_id
         join sales s on p2.product_id = s.product_id
where p2.recovery_active = 1
group by p.producer_id
order by producer_id asc

select p.producer_id, sum(case when s.cancelled = 1 or s.refund = 1 then s.product_price else 0 end) as total_money_lost,
       sum(CASE WHEN s.cancelled = 1 THEN s.product_price ELSE 0 END) AS canceled,
       sum(CASE WHEN s.refund = 1 THEN s.product_price ELSE 0 END) AS refund
from producer p
         join product p2 on p.producer_id = p2.producer_id
         join sales s on p2.product_id = s.product_id
where p2.recovery_active = 0
group by p.producer_id
order by producer_id asc

