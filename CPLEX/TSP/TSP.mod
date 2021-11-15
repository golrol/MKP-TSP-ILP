/*********************************************
 * OPL 12.8.0.0 Model
 * Author: Admin
 * Creation Date: 26 баев 2021 at 18:32:22
 *********************************************/
 
 // (n^2 - n) / 2 = number of edges

 /*****************************************************************************
 *
 * DATA
 * 
 *****************************************************************************/
int		Vehicle	= ...;
int     n       = ...;//number of cities from data
range   Cities  = 1..n;
int		IndexArray[Cities] = ...;

// Edges -- sparse set
int dist[Cities][Cities] = ...;

// Decision variables
dvar boolean X[Cities][Cities];
dvar int+ U[Cities];

 
 
 
 
 /*****************************************************************************
 *
 * MODEL
 * 
 *****************************************************************************/
 
 
minimize sum (i, j in Cities) dist[i][j] * X[i][j];
subject to {
   
   //self edge distance
   forall (i in Cities) X[i][i] == 0;
   
   //exactly one edge enters and one edge leaves
   forall (i in Cities)
     sum (j in Cities) X[i][j] == 1;
      
     forall (j in Cities)
       sum (i in Cities) X[i][j] == 1;
   
    //no circles check
    forall(i, j in Cities : j != 1)
      U[i] - U[j] + n*X[i][j] <= n-1;
      
      U[1] == 0;
};

// Print result
execute {
	var fileName = "../TSPOutput" + Vehicle + ".txt"
	var ofile = new IloOplOutputFile(fileName);

    for (var i in Cities)
        for (var j in Cities)
            if (X[i][j] > 0){
            	write(IndexArray[i], " -> ", IndexArray[j], "\n");
            	ofile.writeln(IndexArray[i], " -> ", IndexArray[j]);	
           }
}