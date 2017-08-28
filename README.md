# AddFlow

I just made a change from the Yang’s computer

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

Now we can run through the test procedure.

On Server5, run command 

`python AFServer.py`

to begin listening Server.

Then on grnlntrn server run command [well first do `cd app` so you are in the right directory] 

`ryu-manager --verbose add_flow.py`

and now wait until you see on the grnlntrn terminal that the switch has entered into main mode.  Once it has, on Server6 run command

`python AFClient.py`

You should see that the flows were installed and the connections were made.  Then to compare the times view sslog1.txt in grnlntrn terminal and view clog.txt in Server6 terminal.  The time (in EPOCH mircoseconds) should be slightly smaller in clog.txt than in sslog1.txt.  This is because the client asks for its connection first.  and the reason why we are looking at sslog1.txt first is because once the flow from server6 to server5 is installed first will.  Once you are done analyzing these two times, take a look at sslog2.txt and slog.txt.  The time in sslog2.txt should be slightly smaller than in slog.txt because the connection between the two servers will not be fully functional until the fnal flow is installed.
So the times should look like client-grnlntrn-grnlntrn-listening server.
If you would like to repeat this test then be sure to delete the flows and run through this procedure as many times as you would like.


