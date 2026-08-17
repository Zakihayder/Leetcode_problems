# Write your MySQL query statement below
(
    select u.name as results
    from Users u
    join MovieRating r
        on u.user_id = r.user_id
    group by u.user_id
    order by count(*) desc, u.name asc
    limit 1
)

union all
(
    select m.title as results
    from Movies m
    join MovieRating r
        on m.movie_id = r.movie_id
    where r.created_at >= '2020-02-01'
      and r.created_at < '2020-03-01'
    group by m.movie_id
    order by avg(r.rating) desc, m.title asc
    limit 1
);