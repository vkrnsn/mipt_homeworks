create table if not exists customers (
  id serial primary key,
  first_name varchar(20) not null,
  last_name varchar(20),
  gender varchar(6) not null,
  dob date,
  job_title text,
  job_industry_category text,
  wealth_segment text not null,
  deceased_indicator char(1) not null,
  owns_car varchar(3) not null
)

create table if not exists addresses (
  id serial primary key,
  address text not null,
  postcode char(4) not null,
  state varchar(20) not null,
  country varchar(20) not null,
  property_valuation smallint not null,
  customer_id int references customers(id)
)

create table if not exists products (
  id serial primary key,
  legacy_product_id int,
  brand varchar(15),
  line varchar(10),
  class varchar(10),
  size varchar(10),
  list_price money not null,
  standard_cost money
)

create table if not exists transactions (
  id serial primary key,
  date date,
  online_order bool,
  order_status varchar(10),
  product_id int references products(id),
  customer_id int references customers(id)
)
