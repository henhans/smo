set style data dots
set nokey
set xrange [0: 4.21691]
set yrange [  4.15307 : 19.20392]
set arrow from  0.55960,   4.15307 to  0.55960,  19.20392 nohead
set arrow from  1.11921,   4.15307 to  1.11921,  19.20392 nohead
set arrow from  1.91061,   4.15307 to  1.91061,  19.20392 nohead
set arrow from  2.30631,   4.15307 to  2.30631,  19.20392 nohead
set arrow from  2.86591,   4.15307 to  2.86591,  19.20392 nohead
set arrow from  3.42551,   4.15307 to  3.42551,  19.20392 nohead
set xtics ("G"  0.00000,"X"  0.55960,"M"  1.11921,"G"  1.91061,"Z"  2.30631,"R"  2.86591,"A"  3.42551,"Z"  4.21691)
 plot "smo_band.dat"
