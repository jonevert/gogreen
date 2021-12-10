/*
Gagnagrunns föll sem þarf að hafa
*/


CREATE FUNCTION updateCars() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL
AS $$
BEGIN
   insert into cars (plate_nr, model, make, year, color, co2) 
      (select permno, model, make, extract(year from timestamp), color, co2  from samgongustofa
      where id = (select max(id) from samgongustofa));
return NEW;
END;
$$


CREATE TRIGGER samgongustofaInsert 
   AFTER INSERT 
   ON samgongustofa
   FOR EACH ROW 
       EXECUTE PROCEDURE updateCars();


CREATE FUNCTION instanceIsFalse() RETURNS void AS $$
BEGIN
  update instances 
  set isvalid = false
  where id = (select max(id)
    from instances);
END;
$$ LANGUAGE plpgsql;

INSERT INTO public.samgongustofa VALUES (2, 'NRX31', 'NRX31', 'MALAM51BABM857741', 'HYUNDAI', 'I10', 'Ljósgrár', '2011-04-14 14:48:00+00', 'Í lagi', NULL, 110, 0, 0, 0, 1405, 948);
INSERT INTO public.instances  VALUES (2, 'NRX31', 1, '2021-11-29 22:23:47.663333+00', 0, 'NRX31-2021-11-29-22:23:47.png', true);
INSERT INTO public.cars  VALUES (2, 'NRX31', 'HYUNDAI', 'I10', 2011, 'Ljósgrár', 110);

SELECT * FROM pg_catalog.pg_tables;

select * from auth_user_user_permissions;

select * from instances;

select * from location;

insert into location values(default, 'Penisville', 'whore country', 69)

select * from instances;

update location
set zip = 102
where id = 1;

insert into location values (default, 'Bílaplan HR - inngangur', 'Höfuðborgarsvæðið', 102)

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; 

delete from location
where id = 2;