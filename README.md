__1.nMAP__

  A novel microarray data analysis program (nMAP) is a free script for SNP genotype determination without normalization. This program is available for CEL file data generated using the Affymetrix Genome-Wide Human SNP Array 6.0 platform.




__2.Requirement__

 ・python3

 ・The data of 95% confidence interval for Strength and Log Ratio (These data for 866,970 SNPs are uploaded separately by chromosome.)



__3.Usage__

  python3 nMAP_genotype_determination.py "input file" "output file" "minimum cluster size"


  

__4.Test sample and Result__

  We prepared the test sample (nMAP_test_sample.txt). When the minimum cluster size is set as 20 and 160, the genotype result and summary files are uploaded.
  
 ・result_20.txt
  
 ・result_160.txt
  
 ・Summury_Of_Genotype_Determination_Minimum_Cluster_Size_20.txt
  
 ・Summury_Of_Genotype_Determination_Minimum_Cluster_Size_160.txt
  

__5.Reference__




__6.Contact__
  
  Kayoko Yagasaki: k-yagasaki@umin.ac.jp

