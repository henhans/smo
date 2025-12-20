set style data dots
set nokey
set xrange [0: 4.23874]
set yrange [  4.27517 : 23.29907]
set arrow from  0.56100,   4.27517 to  0.56100,  23.29907 nohead
set arrow from  1.12200,   4.27517 to  1.12200,  23.29907 nohead
set arrow from  1.91537,   4.27517 to  1.91537,  23.29907 nohead
set arrow from  2.32337,   4.27517 to  2.32337,  23.29907 nohead
set arrow from  2.88437,   4.27517 to  2.88437,  23.29907 nohead
set arrow from  3.44537,   4.27517 to  3.44537,  23.29907 nohead
set xtics ("G"  0.00000,"X"  0.56100,"M"  1.12200,"G"  1.91537,"Z"  2.32337,"R"  2.88437,"A"  3.44537,"Z"  4.23874)
 plot "smo_band.dat"
