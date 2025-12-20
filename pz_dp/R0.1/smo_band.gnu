set style data dots
set nokey
set xrange [0: 4.21691]
set yrange [  4.14859 : 19.12965]
set arrow from  0.55960,   4.14859 to  0.55960,  19.12965 nohead
set arrow from  1.11921,   4.14859 to  1.11921,  19.12965 nohead
set arrow from  1.91061,   4.14859 to  1.91061,  19.12965 nohead
set arrow from  2.30631,   4.14859 to  2.30631,  19.12965 nohead
set arrow from  2.86591,   4.14859 to  2.86591,  19.12965 nohead
set arrow from  3.42551,   4.14859 to  3.42551,  19.12965 nohead
set xtics ("G"  0.00000,"X"  0.55960,"M"  1.11921,"G"  1.91061,"Z"  2.30631,"R"  2.86591,"A"  3.42551,"Z"  4.21691)
 plot "smo_band.dat"
