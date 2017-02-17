import sys
inputs = sys.argv[1]

#make input files
#bunch of strings that will be unchanged between the files
simulation = "%%%%% SIMULATION PARAMETERS %%%%%%%%%%%%\nData_File_Name=TestIBDSim\n.txt_extension=true\nRun_Number=10\nRandom_Seeds=87144630\nPause=Final"

markers = "\n\n%%%%% MARKERS PARAMETERS %%%%%%%%%%%%%%%\nLocus_Number = 2, 1, 2, 1\nMutation_Rate = 0.001, 0.001, 0.001, 0.002\nMutation_Model = ISM, KAM, SMM, TN93\n\nVariable_Mutation_Rate = F, F, T, F\nPolymorphic_Loci_Only = T, F, F,T\nAllelic_Lower_Bound = NA, 3, 5, NA\nAllelic_Upper_Bound = NA, 20, 50, NA\nAllelic_State_MRCA = NA, 8, 6, NA\nRepeated_motif_size = NA, 1, 1, NA\nSMM_Probability_In_TPM = NA, 0.01, 0.2, NA\nGeometric_Variance_In_TPM = NA, 2.6, 3.5, NA\nGeometric_Variance_In_GSM = NA, 0.56, 0.93, NA\nPloidy=Diploid"

sequence = "\n\n%% SEQUENCE SPECIFIC SETTINGS\nMRCA_Sequence = AGCTAGCTAGCT\n%Note, Sequence_Size is redundant information here! %\nSequence_Size = 12\nTransition_Transversion_ratio = 0.7\nTransition1_Transition2_ratio = 1.2\nEquilibrium_Frequencies = 0.1 0.4 0.3 0.2"

output = "\n\n%%%%%% OUTPUT FILE FORMAT OPTIONS %%%%%%%\nGenepop=T\nMigrate=F\nMigrate_Letter=F\nNexus_file_format = Haplotypes_only"

computation = "\n\n%%%%%% VARIOUS COMPUTATION OPTION S%%%%%%%\n%The code below can be specified in a single line\nDiagnosticTables=Iterative_Identity_Probability,Hexp,Fis,Seq_stats\nDiagnosticTables=Prob_Id_Matrix,Effective_Dispersal,Iterative_statistics\n\n%%%%%%%% DEMOGRAPHIC OPTIONS %%%%%%%%%%%%%"

lattice = "\n\n%% LATTICE \nLattice_Boundaries=absorbing\nTotal_Range_Dispersal=F\nLattice_SizeX=100\nLattice_SizeY=50\nInd_Per_Pop=100\nVoid_Nodes=1\nSpecific_Density_Design=false\nZone=T\nVoid_Nodes_Zone=1\nInd_Per_Pop_Zone=50\nMin_Zone_CoordinateX=5\nMax_Zone_CoordinateX=15\nMin_Zone_CoordinateY=5\nMax_Zone_CoordinateY=15"

sample = "\n\n%% SAMPLE\n%% classical squared sample design:\nSample_SizeX=10\nSample_SizeY=10\nMin_Sample_CoordinateX=5\nMin_Sample_CoordinateY=5"

dispersal = "\n\n%% DISPERSAL\nDispersal_Distribution=1\nImmigration_Control=Simple1DProduct\nTotal_Emigration_Rate=0.1\nDist_max=48\nPareto_Shape=2.16574\nGeometric_Shape=0.75\nSichel_Gamma=-2.15\nSichel_Xi=20.72\nSichel_Omega=-1"

final = "\n\n%% CONTINUOUS CHANGE IN DENSITY\nContinuousDemeSizeVariation=F\n\n%% FIRST DEMOGRAPHIC CHANGE\nNewDemographicPhaseAt=50\nInd_Per_Pop=20\nLattice_SizeX=50\nLattice_SizeY=50\nRandom_Translation=true\n\nZone=false\n\n%%continuous change in deme size\nContinuousDemeSizeVariation=Exponential\n\n%% SECOND DEMOGRAPHIC CHANGE\nNewDemographicPhaseAt=200\nInd_Per_Pop=1\nLattice_SizeY=10\nRandom_Translation=true\n\n%%%%%% EndOfSettings %%%%%%%%"

#this may make a ton of new files so execute in independent folder
#this creates a bunch of identical files that can be executed by IBDSim
#need to put in variables for different dispersal scenarios

def makeIBDinput(inputs):
    for i in range(int(inputs)):
        f=open("IbdSettings_" + str(i) +".txt","w")
        f.write(simulation + markers + sequence + output + computation + lattice + sample + dispersal + final)
        f.close()

makeIBDinput(inputs)


