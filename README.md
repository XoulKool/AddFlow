# AddFlow
### Note This Test Needs Debugging
The most basic test which was completed Summer 2016 on our system.  This test will calculate the amount
of time it takes to add a flow and for the servers in our system to achieve their connection.

To start, open a terminal and ssh into the Pica8 switch.  To ensure the consistency of this test, it is imperative to
delete the flows from any prior use of the switch after EVERY run of the test.  This way we can make sure we are really 
testing just the addition of the flow.  We can delete all the flows in the table using the command

`ovs-ofctl del-flows br0`

Another important note is that all tests, save the last, one use OpenFlow Version 1.0.  To set this on the Pica8 switch use command

`ovs-vsctl set Bridge br0 protocols=OpenFlow10`

Now that all the preliminary steps are taken care of, the procedure for the test is as follows:

Create a new terminal. ssh into grnlntrn 

[`ssh root@grnlntrn.cis.temple.edu`]

Create a new terminal.  ssh again into grnlntrn and then ssh into the Pica8 Switch 

[remember must use username admin - `ssh admin@10.2.0.2` - do this in grnlntrn server]

Create a new terminal. ssh into grnlntrn and then ssh into Server5 in our network 

[In grnlntrn server, run command `ssh 10.0.0.5`]

Create a new terminal.  ssh into grnlntrn and then ssh into Server6 in our network

[In grnlntrn server, run command `ssh 10.0.0.6`]

You should now have four terminals on display.  One for the Pica8 switch (which by default should be in OVS mode), one for the grnlntrn server, one for Server5, and one for Server6.

The final preliminary step is to delete any log files which may have been used for prior tests, just so you don't get confused with your data.  So on grnlntrn be sure to

`rm sslog1.txt` and
`rm sslog2.txt`

On Server5

`rm slog.txt`

and on Server6

`rm clog.txt`

Now we can run through tehe test procedure.

