# AddFlow
The most basic test which was completed Summer 2016 on our system.  This test will calculate the amount
of time it takes to add a flow and for the servers in our system to achieve their connection.

To start, open a terminal and ssh into the Pica8 switch.  To ensure the consistency of this test, it is imperative to
delete the flows from any prior use of the switch after EVERY run of the test.  This way we can make sure we are really 
testing just the addition of the flow.  We can delete all the flows in the table using the command
``
