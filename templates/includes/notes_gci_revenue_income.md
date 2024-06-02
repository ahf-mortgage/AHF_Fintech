
I have created seven tabs John Sally Elif Douglas Ashton Sylvia and Peter

John sponsored Sally, Sally sponsored Elif, Elif sponsor Douglas, Douglas sponsored Ashton, Ashton sponsored Sylvia, Sylvia sponsored Peter, Peter sponsored Bob


I have created fake transactions for us to use in figuring out the distributions

GCI is split is currently 60/40 

with 2.75% the cap is  27500
60/40 gives 16500 to branch and 11000 to ahf

after GCI 27500 is meet balance of the GCI goes 100% to branch

with peter generates  $30,000 in GCI the split would go 16500 + 30000 - 27500 = 19000 to branch

11000 goes to ahf is what used for revenue share from Bob's production .

Bob's level 1 goes to Peter
Bob's level 2 goes to slyvia,
Bob's level 3 goes to Ashatan,
Bob's level 4 goest to Douglas,
Bob's level 5 goes to Elif
Bob's level 6 goes to Sally
Bob's level 7 goes to John

Peter's level 1 goes to slyvia,
Peter's level 2 goes to Ashatan,
Peter's level 3 goest to Douglas,
Peter's level 4 goes to Elif
Peter's level 5 goes to Sally
Peter's level 6 goes to John


slyvia's level 1 goes to Ashatan,
slyvia's level 2 goest to Douglas,
slyvia's level 3 goes to Elif
slyvia's level 4 goes to Sally
slyvia's level 5 goes to John



Ashatan's level 1 goest to Douglas,
Ashatan's level 2 goes to Elif
Ashatan's level 3 goes to Sally
Ashatan's level 4 goes to John


Douglas's level 1 goes to Elif
Douglas's level 2 goes to Sally
Douglas's level 3 goes to John


Elif's level 1 goes to Sally
Elif's level 2 goes to John

Sally's level 1 goes to John

John is sponsored by AHF so there is no revenue share the compnay keeps it.

we need to create a linked list to iterate to distrubute the revenue share.

bob.sponsor = peter
peter.sponsor = sylvia
sylvia.sponsor = ashaton
ashaton.sponsor = douglas
douglas.sponsor = elif
elif.sponsor = sally
sally.sponsor = john
john.sponsor = ahf

distrubting bob's revenue share.
for bob level 1,to 7 
	bob level 1 = bob.sponsor     --> peter  peter += bob level 1
	bob level 2 = peter.sponsor   --> bob.sponsor.sponsor(iterator)  ashaton += bob level 2
	bob level 3 = sylvia.sponsor  --> bob.sponsor.sponsor.sponsor.sponsor  douglas += bob level 3
	bob level 4 = ashaton.sponsor --> bob.sponsor.sponsor.sponsor.sponsor.sponsor
	bob level 5 = elif.sponsor    --> bob.sponsor.sponsor.sponsor.sponsor.sponsor.sponsor
	bob level 6 = sally.sponsor   --> bob.sponsor.sponsor.sponsor.sponsor.sponsor.sponsor.sponsor
	bob level 7 = john.sponsor    --> bob.sponsor.sponsor.sponsor.sponsor.sponsor.sponsor.sponsor.sponsor


distrubting sally's revenue share.
for sally leve 1 ,to 7
	sally level 1 = sally.sponsor --> john  john += sally level 1
	sally level 2 = john.sponsor --> ahf(breakpoint)

so, in general for example 
john get revenue share from all lower levels 
john += sally level 1 
john += elif level 2
john += douglas level 3
john += ashaton level 4
john += sylvia level 5
john += peter level 6
john += bob level 7


sally get revenue share from all lower levels 
sally += elif level 1
sally += douglas level 2
sally += ashaton level 3
sally += sylvia level 4
sally += peter level 5
sally += bob level 6


elif get revenue share from all lower levels 
elif += douglas level 1
elif += ashaton level 2
elif += sylvia level 3
elif += peter level 4
elif += bob level 5

elif get revenue share from all lower levels 

douglas += ashaton level 1
douglas += sylvia level 2
douglas += peter level 3
douglas += bob level 4

ashaton += sylvia level 1
ashaton += peter level 3
ashaton += bob level 4