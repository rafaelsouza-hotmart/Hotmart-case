# data de registro do usuario = p.registry_date
# recovery_active
# p.producer_id
# purchase_id

SELECT p.producer_id, p.registry_date, recovery_active, count(purchase_id) as sales
FROM producer p
         join product pr on p.producer_id = pr.producer_id
         join sales s on pr.product_id = s.product_id
WHERE YEAR(p.registry_date) >= 2020 and recovery_active = 1
group by p.producer_id, p.registry_date, recovery_active
order by sales desc
limit 10

select p.producer_id, recovery_active, p.registry_date from producer p
                  join product pr on p.producer_id = pr.producer_id
WHERE YEAR(p.registry_date) >= 2020
group by p.producer_id, recovery_active, p.registry_date
order by p.registry_date asc



