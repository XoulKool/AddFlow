# AddFlow
The most basic test which was completed Summer 2016 on our system.  This test will calculate the amount
of time it takes to add a flow and for the servers in our system to achieve their connection.

To start, open a terminal and ssh into the Pica8 switch.  To ensure the consistency of this test, it is imperative to
delete the flows from any prior use of the switch after EVERY run of the test.  This way we can make sure we are really 
testing just the addition of the flow.  We can delete all the flows in the table using the command

`ovs-ofctl del-flows br0`

Another important note is that all tests, save the last one use OpenFlow Version 1.0.  To set this on the Pica8 switch use command

`ovs-vsctl set Bridge br0 protocols=OpenFlow10`

Now that all the preliminary steps are taken care of, the procedure for the test is as follows:


