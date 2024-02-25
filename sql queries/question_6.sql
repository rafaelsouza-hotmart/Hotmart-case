# If you need to create a ranking of the top creators of 2023, which variables do
#     you consider crucial for ranking them? You can also
#     create variables from the data. You must explain your reasoning and
#         your choice of variables and show how this reflects in your SQL code.


#selecionar tudoo
select * from producer p
                  join product p2 on p.producer_id = p2.producer_id
                  join sales s on p2.product_id = s.product_id

acho interessante saber quais creators mais faturaram, que incluse é
         a forma que a hotmart reconhece seus cretors atualmente
         por meio de uma x quantidade de comissao ao longo de sua jornada na hotmart.
             então olharia apenas para a comissão dos mesmos, e faria um sum

# top users from 2023 (top comission)

select p.producer_id, round(sum(comission_value)) all_time_comission from producer p
                  join product p2 on p.producer_id = p2.producer_id
                  join sales s on p2.product_id = s.product_id
group by p.producer_id
order by all_time_comission desc
