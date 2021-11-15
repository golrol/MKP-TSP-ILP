/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Admin
 * Creation Date: 12 баев„ 2021 at 0:09:31
 *********************************************/

int NumOfVehicles = ...;
range VehiclesArrySize = 1..NumOfVehicles;
int Capacity[VehiclesArrySize] = ...;
int NumOfItems = ...;
range arraySize = 1..NumOfItems;
int Value[arraySize] = ...;
int Weight[arraySize] = ...;


dvar int x[arraySize][VehiclesArrySize] in 0..1;

maximize
  sum(i in arraySize, j in VehiclesArrySize) Value[i] * x[i][j];
 
 subject to {
  forall (j in VehiclesArrySize)
        cons1 : sum(i in arraySize) Weight[i]*x[i][j] <= Capacity[j];

  	forall (i in arraySize)
        cons2 : sum(j in VehiclesArrySize) x[i][j] <= 1;
}

execute{ 
	var ofile = new IloOplOutputFile("../knapSackOutput.txt");
	var totalWeight = 0;
	var itemIndex = 1;
	var totVal = 0;
	for (var i in VehiclesArrySize){
		ofile.writeln("Vehicle ID: ", i, " Capacity: ", Capacity[i], ".");
		itemIndex = 1;
		for (var j in arraySize){
			if (x[j][i] == 1){
				ofile.writeln(itemIndex++, " Item ID: ", j, " Weight: ", Weight[j], ". Value: ", Value[j], ".");
				totalWeight = totalWeight + Weight[j];
				totVal = totVal + Value[j];
			}
		}
		ofile.writeln("Vehicle ", i, ": ", "Total Weight:", totalWeight, ". Total Value:", totVal, ".");
		totalWeight = 0;
		totVal = 0;
		ofile.writeln();
	}

	var flag=0;
	ofile.writeln("Left in werehouse:");
	for (var i in arraySize){
		flag = 0;	
		for (var j in VehiclesArrySize){		
				if (x[i][j] == 1){
					flag = 1;			
				}
			}
			if (flag == 0){
					ofile.writeln(itemIndex++, "ID: ", i, " Weight: ", Weight[i], ". Value: ", Value[i], ".");	
		}
	}
	
	ofile.close();
	writeln("Finished!");
}

