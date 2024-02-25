-- Recovery enabled
select p.producer_id, niche, count(purchase_id) as sales from producer p
        join product on p.producer_id = product.producer_id
        join sales s on product.product_id = s.product_id
where YEAR(p.registry_date) >= 2020
and product.recovery_active = 1
group by p.producer_id, niche
order by sales desc;

-- Recovery disabled
select p.producer_id, niche, count(purchase_id) as sales from producer p
join product on p.producer_id = product.producer_id
join sales s on product.product_id = s.product_id
where YEAR(p.registry_date) >= 2020
 and product.recovery_active = 0
group by p.producer_id, niche
order by sales desc;