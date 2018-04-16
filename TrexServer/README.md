=====================
====  Trex Serv  ====
===   On Docker   ===
=====================


Explication :
-------------

B> : Bash
C> : Container
T> : Trex

Terminal 1
------------------------------------------------------------------------------------------------------------------
B> docker pull trexcisco/trex:2.36					|	Pull the Trex Docker		 |
B> docker run --rm -it --privileged --cap-add=ALL trexcisco/trex:2.36	|	Run the Trex iamge with Bash	 |
C> ./t-rex-64 -i							|	Start the server   		 |
	   									 -> (display the Port trafics)	 |
------------------------------------------------------------------------------------------------------------------

If you don't use the TrexGui Docker, open en new terminal inside the same computer

Terminal 2
------------------------------------------------------------------------------------------------------------------
B> docker exec -it 'Container ID' bash					|	Exec the container with Bash	 |
C> ./trex-console  	      	  					|	Start Client with Stateless mode |
   										      -> default localhost:4501  |
   										      -> -s 'ip server'		 |
										      -> -p 'port'		 |
T> start -f stl/imix.py -m 10kpps --port 0				|	Start trafic			 |
   	    		      	  	 					      -> with Imix mode		 |
										      -> with 10k connections	 |
										      -> on port 0		 |
T> tui									|	Show Stats			 |
------------------------------------------------------------------------------------------------------------------
