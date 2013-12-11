#!/usr/bin/python

motifs = ["mfFourComplete", "mfFourLine", "mfFourSquare",
"mfFourSquareDiag", "mfFourStar", "mfFourTriangleEdge", "mtThreeClosed",
"mtThreeOpen"]

for m in motifs:
    print "\\begin{figure}[p]"
    print "\centering"
    print "\includegraphics[width=3in]{Figures/motif_error-pwr-power-" + m + ".eps}"
    print "\caption{Experiment 2, network pwr-power, motif " + m + ".}"
    print "\label{fig:exp2-pwr-power-" + m + "}"
    print "\end{figure}"
    print
