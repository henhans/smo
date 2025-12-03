set style data dots
set nokey
set xrange [0: 4.21691]
set yrange [  4.14807 : 19.17077]
set arrow from  0.55960,   4.14807 to  0.55960,  19.17077 nohead
set arrow from  1.11921,   4.14807 to  1.11921,  19.17077 nohead
set arrow from  1.91061,   4.14807 to  1.91061,  19.17077 nohead
set arrow from  2.30631,   4.14807 to  2.30631,  19.17077 nohead
set arrow from  2.86591,   4.14807 to  2.86591,  19.17077 nohead
set arrow from  3.42551,   4.14807 to  3.42551,  19.17077 nohead
set xtics ("G"  0.00000,"X"  0.55960,"M"  1.11921,"G"  1.91061,"Z"  2.30631,"R"  2.86591,"A"  3.42551,"Z"  4.21691)
 plot "smo_band.dat"
