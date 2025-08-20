use jen;
select * from salesmans;
create table customer(customer_id int,cust_name varchar(40),city varchar(50),grade int,salesmans_id int);
insert into customer values(3002,"Nick Rimando","New York",100,5001),(3005,"Graham Zusi","California",200,5002),(3001,"Brad Guzan","London",null,5005),(3004,"Fabian Johns","Paris",300,5006),(3007,"Brad Davis","New York",200,5001),
(3009,"Geoff Camero","Berlin",100,5003),(3008,"Julian Green","London",300,5002),(3003,"Jozy Altidor","Moscow",200,5007);
select* from customer;
create table orders(ord_no int,purch_amt float,ord_date date,customer_id int,salesmans_id int);
insert into orders values(70001,150.5,"2012-10-05",3005,5002),(70009,270.65,"2012-09-10",3001,5005),

(70002,65.26,"2012-10-05",3002,5001),(70004,110.5,"2012-08-17",3009,5003),
(70007,948.5,"2012-09-10",3005,5002),
(70005,2400.6,"2012-07-27",3007,5001),(70008,5760,"2012-09-10",3002,5001),
(70010,1983.43,"2012-10-10",3004,5006),
(70003,2480.4,"2012-10-10",3009,5003),
(70012,250.45,"2012-06-27",3008,5002),
(70011,75.29,"2012-08-17",3003,5007),
(70013,3045.6,"2012-04-25",3002,5001);
select * from orders;
select name,city from salesmans where city="paris";
select *from customer where grade=200;
select ord_no,ord_date,purch_amt from orders where salesmans_id=5001;
select * from orders cross join customer;
create table employees(emp_id int primary key,name varchar(50),manager_id int);
insert into employees values(1,"ammu",1),(2,"anu",1),(3,"jess",1);
select e.name as employee_name,m.name as manager_name from employees e inner join employees m on e.manager_id=m.emp_id;
