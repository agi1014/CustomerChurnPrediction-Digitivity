import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var0 = 0.26447973
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < 0.12883902:
                            if input[7] < 0.8726697:
                                var0 = -0.2977298
                            else:
                                var0 = -0.3383104
                        else:
                            if input[0] < 0.05038005:
                                var0 = 0.2640966
                            else:
                                var0 = -0.33127046
                    else:
                        var0 = 0.2643839
                else:
                    var0 = 0.26442465
            else:
                var0 = 0.26445195
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var0 = 0.26443225
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var0 = 0.25964865
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var0 = -0.32664385
                            else:
                                var0 = 0.24656539
                        else:
                            var0 = 0.25316787
                else:
                    var0 = 0.2643538
        else:
            var0 = 0.26449117
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var1 = 0.23787151
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < 0.12883902:
                                var1 = -0.2849147
                            else:
                                var1 = -0.2340099
                        else:
                            if input[7] < 0.8726697:
                                var1 = 0.29609144
                            else:
                                var1 = -0.2772528
                    else:
                        var1 = 0.23778914
                else:
                    var1 = 0.23782419
            else:
                var1 = 0.23784767
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var1 = 0.23783073
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var1 = 0.23372029
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var1 = -0.2723876
                            else:
                                var1 = 0.2225024
                        else:
                            var1 = 0.22815965
                else:
                    var1 = 0.23776327
        else:
            var1 = 0.23788138
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var2 = 0.2192655
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var2 = -0.25321212
                            else:
                                var2 = -0.22077037
                        else:
                            if input[7] < 0.8726697:
                                var2 = 0.25903183
                            else:
                                var2 = -0.24272
                    else:
                        var2 = 0.21918759
                else:
                    var2 = 0.21922073
            else:
                var2 = 0.21924292
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var2 = 0.21922691
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var2 = 0.21535425
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var2 = -0.23817988
                            else:
                                var2 = 0.2049022
                        else:
                            var2 = 0.21015301
                else:
                    var2 = 0.21916315
        else:
            var2 = 0.21927477
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var3 = 0.20562336
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < 0.12883902:
                            if input[6] < 0.17672138:
                                var3 = -0.22522466
                            else:
                                var3 = -0.19304417
                        else:
                            if input[0] < 0.05038005:
                                var3 = 0.27246842
                            else:
                                var3 = -0.22462627
                    else:
                        var3 = 0.20554498
                else:
                    var3 = 0.20557831
            else:
                var3 = 0.20560063
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var3 = 0.20558454
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var3 = 0.20170484
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var3 = -0.21431318
                            else:
                                var3 = 0.19140752
                        else:
                            var3 = 0.19655044
                else:
                    var3 = 0.20552036
        else:
            var3 = 0.20563273
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var4 = 0.19528043
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var4 = -0.21170332
                            else:
                                var4 = -0.17917821
                        else:
                            if input[7] < 0.8726697:
                                var4 = 0.25128034
                            else:
                                var4 = -0.20381555
                    else:
                        var4 = 0.19519816
                else:
                    var4 = 0.19523314
            else:
                var4 = 0.1952566
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var4 = 0.19523971
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var4 = 0.19119047
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var4 = -0.19646792
                            else:
                                var4 = 0.18066221
                        else:
                            var4 = 0.18588243
                else:
                    var4 = 0.19517232
        else:
            var4 = 0.19529031
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var5 = 0.18724267
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var5 = -0.16832234
                            else:
                                var5 = -0.1987194
                        else:
                            if input[0] < -0.7533263:
                                var5 = 0.36016318
                            else:
                                var5 = -0.1801598
                    else:
                        var5 = 0.18715377
                else:
                    var5 = 0.18719159
            else:
                var5 = 0.18721691
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var5 = 0.18719864
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var5 = 0.18285537
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var5 = -0.18239605
                            else:
                                var5 = 0.17182614
                        else:
                            var5 = 0.17724927
                else:
                    var5 = 0.18712588
        else:
            var5 = 0.1872533
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var6 = 0.18087743
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var6 = -0.18898311
                            else:
                                var6 = -0.1532878
                        else:
                            if input[7] < 0.8726697:
                                var6 = 0.24148081
                            else:
                                var6 = -0.17886145
                    else:
                        var6 = 0.18077958
                else:
                    var6 = 0.18082118
            else:
                var6 = 0.18084906
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var6 = 0.18082894
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var6 = 0.17608425
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var6 = -0.17079867
                            else:
                                var6 = 0.16434878
                        else:
                            var6 = 0.17006555
                else:
                    var6 = 0.18074885
        else:
            var6 = 0.18088913
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var7 = 0.17576194
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < 0.12883902:
                            if input[6] < 0.17672138:
                                var7 = -0.17572188
                            else:
                                var7 = -0.14068073
                        else:
                            if input[0] < 0.05038005:
                                var7 = 0.27587688
                            else:
                                var7 = -0.17516746
                    else:
                        var7 = 0.17565271
                else:
                    var7 = 0.17569916
            else:
                var7 = 0.17573026
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var7 = 0.17570782
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var7 = 0.17046058
                    else:
                        if input[4] < 0.97290224:
                            if input[2] < -1.3751659:
                                var7 = 0.38459638
                            else:
                                var7 = -0.15621287
                        else:
                            var7 = 0.163932
                else:
                    var7 = 0.17561847
        else:
            var7 = 0.17577499
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var8 = 0.17160231
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var8 = -0.13499987
                            else:
                                var8 = -0.17400318
                        else:
                            if input[0] < -0.7533263:
                                var8 = 0.34457064
                            else:
                                var8 = -0.15024419
                    else:
                        var8 = 0.17147931
                else:
                    var8 = 0.17153162
            else:
                var8 = 0.17156665
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var8 = 0.17154136
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var8 = 0.16569042
                    else:
                        if input[10] < 2.0151885:
                            if input[2] < -1.3751659:
                                var8 = 0.3027573
                            else:
                                var8 = -0.14856899
                        else:
                            var8 = 0.16573913
                else:
                    var8 = 0.17144077
        else:
            var8 = 0.17161703
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var9 = 0.16818772
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var9 = -0.1685709
                            else:
                                var9 = -0.12603319
                        else:
                            if input[7] < 0.8726697:
                                var9 = 0.24590112
                            else:
                                var9 = -0.15649131
                    else:
                        var9 = 0.16804832
                else:
                    var9 = 0.16810758
            else:
                var9 = 0.1681473
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var9 = 0.16811863
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var9 = 0.16155902
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var9 = -0.14514944
                            else:
                                var9 = 0.15653369
                        else:
                            var9 = 0.15975952
                else:
                    var9 = 0.1680046
        else:
            var9 = 0.16820444
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var10 = 0.16536292
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < -0.19687115:
                            if input[6] < 0.17672138:
                                var10 = -0.16335696
                            else:
                                var10 = -0.11978811
                        else:
                            if input[0] < -0.7533263:
                                var10 = 0.32213774
                            else:
                                var10 = -0.13497396
                    else:
                        var10 = 0.16520405
                else:
                    var10 = 0.1652716
            else:
                var10 = 0.16531682
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var10 = 0.1652842
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var10 = 0.15790467
                    else:
                        if input[4] < 0.97290224:
                            if input[2] < -1.3751659:
                                var10 = 0.3016698
                            else:
                                var10 = -0.1332175
                        else:
                            var10 = 0.15481311
                else:
                    var10 = 0.1651543
        else:
            var10 = 0.16538194
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var11 = 0.16301084
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var11 = -0.15872513
                            else:
                                var11 = -0.11127463
                        else:
                            if input[7] < 0.8726697:
                                var11 = 0.23587054
                            else:
                                var11 = -0.14536497
                    else:
                        var11 = 0.16282919
                else:
                    var11 = 0.16290638
            else:
                var11 = 0.16295812
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var11 = 0.1629208
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var11 = 0.1546022
                    else:
                        if input[10] < 2.0151885:
                            if input[4] < 0.97290224:
                                var11 = -0.13113672
                            else:
                                var11 = 0.14589083
                        else:
                            var11 = 0.15734623
                else:
                    var11 = 0.16277231
        else:
            var11 = 0.16303259
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var12 = 0.1610417
            else:
                if input[3] < -0.19687115:
                    if input[0] < -1.476662:
                        if input[11] < 1.2236042:
                            if input[6] < 0.060390886:
                                var12 = -0.059901435
                            else:
                                var12 = 0.08013376
                        else:
                            if input[2] < 0.95414454:
                                var12 = 0.37608945
                            else:
                                var12 = 0.034400634
                    else:
                        if input[0] < 0.8540864:
                            if input[4] < 0.97290224:
                                var12 = -0.04243229
                            else:
                                var12 = 0.13208939
                        else:
                            if input[0] < 0.93445706:
                                var12 = 0.03639035
                            else:
                                var12 = 0.13956104
                else:
                    if input[0] < -0.67295563:
                        var12 = 0.23834711
                    else:
                        if input[3] < 0.12883902:
                            if input[0] < 0.21112132:
                                var12 = -0.03206819
                            else:
                                var12 = 0.06368379
                        else:
                            if input[4] < -1.0856943:
                                var12 = 0.2445187
                            else:
                                var12 = 0.04184685
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var12 = -0.1050844
                            else:
                                var12 = -0.15525167
                        else:
                            if input[0] < -0.7533263:
                                var12 = 0.30199283
                            else:
                                var12 = -0.12213268
                    else:
                        var12 = 0.16083103
                else:
                    var12 = 0.16092053
            else:
                var12 = 0.16098034
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var12 = 0.16093849
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var12 = 0.15155274
                    else:
                        if input[10] < 2.0151885:
                            if input[2] < -1.3751659:
                                var12 = 0.26974753
                            else:
                                var12 = -0.1216531
                        else:
                            var12 = 0.15238898
                else:
                    var12 = 0.16076826
        else:
            var12 = 0.1610667
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var13 = 0.15938556
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var13 = -0.1512591
                            else:
                                var13 = -0.09814931
                        else:
                            if input[7] < 0.8726697:
                                var13 = 0.22651142
                            else:
                                var13 = -0.13417909
                    else:
                        var13 = 0.1591501
                else:
                    var13 = 0.1592513
            else:
                var13 = 0.15932415
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var13 = 0.15926687
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var13 = 0.14867665
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var13 = -0.11802597
                            else:
                                var13 = 0.14449051
                        else:
                            var13 = 0.1477004
                else:
                    var13 = 0.15907134
        else:
            var13 = 0.15941426
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var14 = 0.15798697
            else:
                if input[0] < -1.476662:
                    if input[11] < 1.2236042:
                        if input[4] < 0.36743265:
                            if input[1] < -0.07280697:
                                var14 = 0.015251123
                            else:
                                var14 = -0.06877087
                        else:
                            var14 = 0.08964083
                    else:
                        if input[2] < 0.95414454:
                            if input[7] < 0.8726697:
                                var14 = 0.111837246
                            else:
                                var14 = 0.38416362
                        else:
                            var14 = 0.07105107
                else:
                    if input[3] < -0.19687115:
                        if input[0] < 0.8540864:
                            if input[4] < 0.97290224:
                                var14 = -0.025717419
                            else:
                                var14 = 0.12330518
                        else:
                            if input[11] < 1.2236042:
                                var14 = 0.13709293
                            else:
                                var14 = 0.03025665
                    else:
                        if input[0] < -0.67295563:
                            var14 = 0.22629713
                        else:
                            if input[3] < 0.12883902:
                                var14 = 0.018225323
                            else:
                                var14 = 0.10733515
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < 0.12883902:
                            if input[6] < 0.17672138:
                                var14 = -0.13906418
                            else:
                                var14 = -0.086813845
                        else:
                            if input[0] < 0.05038005:
                                var14 = 0.3133274
                            else:
                                var14 = -0.13872698
                    else:
                        var14 = 0.15770833
                else:
                    var14 = 0.15782663
            else:
                var14 = 0.15790571
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var14 = 0.15785033
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var14 = 0.14590897
                    else:
                        if input[2] < -1.3751659:
                            var14 = 0.2434647
                        else:
                            if input[4] < 0.97290224:
                                var14 = -0.108605854
                            else:
                                var14 = 0.14232258
                else:
                    var14 = 0.15762536
        else:
            var14 = 0.15802002
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var15 = 0.15680158
            else:
                if input[10] < 2.0151885:
                    if input[0] < -1.476662:
                        if input[11] < 1.2236042:
                            if input[1] < -0.420518:
                                var15 = 0.07345547
                            else:
                                var15 = -0.065208
                        else:
                            if input[2] < 0.95414454:
                                var15 = 0.2631014
                            else:
                                var15 = 0.0634443
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < 0.8540864:
                                var15 = -0.022944666
                            else:
                                var15 = 0.09690078
                        else:
                            if input[0] < -0.67295563:
                                var15 = 0.21163093
                            else:
                                var15 = 0.039102215
                else:
                    var15 = 0.14221543
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var15 = -0.12633003
                            else:
                                var15 = 0.21754931
                        else:
                            if input[3] < -0.19687115:
                                var15 = -0.14487794
                            else:
                                var15 = -0.07911192
                    else:
                        var15 = 0.15648057
                else:
                    var15 = 0.15661682
            else:
                var15 = 0.15670794
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var15 = 0.1566441
            else:
                if input[0] < 0.93445706:
                    if input[10] < 2.0151885:
                        if input[4] < 0.97290224:
                            if input[2] < -1.3751659:
                                var15 = 0.2218265
                            else:
                                var15 = -0.10509946
                        else:
                            var15 = 0.14198218
                    else:
                        var15 = 0.14903846
                else:
                    var15 = 0.15638494
        else:
            var15 = 0.1568397
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var16 = 0.15579364
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var16 = -0.079997666
                            else:
                                var16 = -0.14037238
                        else:
                            if input[0] < -0.7533263:
                                var16 = 0.31320566
                            else:
                                var16 = -0.099208236
                    else:
                        var16 = 0.15544182
                else:
                    var16 = 0.15559743
            else:
                var16 = 0.1557007
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var16 = 0.15561187
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.5175034:
                        if input[5] < -0.55487835:
                            var16 = 0.14242902
                        else:
                            if input[1] < -0.014855128:
                                var16 = 0.09457109
                            else:
                                var16 = -0.060749646
                    else:
                        if input[6] < 0.17672138:
                            if input[2] < -1.3751659:
                                var16 = 0.17721772
                            else:
                                var16 = -0.13415985
                        else:
                            if input[7] < 0.8726697:
                                var16 = 0.77379805
                            else:
                                var16 = -0.12647739
                else:
                    var16 = 0.15531307
        else:
            var16 = 0.1558376
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var17 = 0.15493374
            else:
                if input[6] < -1.4519056:
                    if input[2] < 0.837679:
                        var17 = -0.09726504
                    else:
                        var17 = -0.02448186
                else:
                    if input[1] < 0.6226151:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var17 = 0.21894565
                            else:
                                var17 = 0.08469506
                        else:
                            if input[0] < -1.3159207:
                                var17 = 0.16150911
                            else:
                                var17 = 0.026170341
                    else:
                        if input[0] < 0.8540864:
                            if input[6] < -1.2192446:
                                var17 = 0.09533616
                            else:
                                var17 = -0.018874375
                        else:
                            if input[2] < 0.13888589:
                                var17 = 0.15805985
                            else:
                                var17 = 0.0058411933
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var17 = -0.1385101
                            else:
                                var17 = -0.0716302
                        else:
                            if input[7] < 0.8726697:
                                var17 = 0.20966817
                            else:
                                var17 = -0.11552249
                    else:
                        var17 = 0.15450615
                else:
                    var17 = 0.1546875
            else:
                var17 = 0.15480886
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var17 = 0.15472384
            else:
                if input[0] < 0.93445706:
                    if input[10] < 2.0151885:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var17 = -0.11605573
                            else:
                                var17 = 0.5944505
                        else:
                            if input[4] < 0.97290224:
                                var17 = -0.13336463
                            else:
                                var17 = 0.123616055
                    else:
                        var17 = 0.14492005
                else:
                    var17 = 0.15437908
        else:
            var17 = 0.15498456
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var18 = 0.15419786
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < -0.19687115:
                            if input[6] < 0.17672138:
                                var18 = -0.13385685
                            else:
                                var18 = -0.069887586
                        else:
                            if input[0] < -0.7533263:
                                var18 = 0.28984457
                            else:
                                var18 = -0.08784984
                    else:
                        var18 = 0.15372717
                else:
                    var18 = 0.15393469
            else:
                var18 = 0.15407324
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var18 = 0.15395525
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.5175034:
                        if input[5] < -0.55487835:
                            var18 = 0.13895625
                        else:
                            var18 = 0.023877177
                    else:
                        if input[6] < 0.17672138:
                            if input[2] < -1.3751659:
                                var18 = 0.17323126
                            else:
                                var18 = -0.12430959
                        else:
                            if input[7] < 0.8726697:
                                var18 = 0.4610434
                            else:
                                var18 = -0.11632613
                else:
                    var18 = 0.15355726
        else:
            var18 = 0.15425664
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var19 = 0.15356594
            else:
                if input[6] < -1.4519056:
                    var19 = -0.079304054
                else:
                    if input[0] < -1.476662:
                        if input[11] < 1.2236042:
                            if input[4] < 0.36743265:
                                var19 = -0.03846907
                            else:
                                var19 = 0.08727481
                        else:
                            if input[2] < -0.21051069:
                                var19 = 0.2991213
                            else:
                                var19 = 0.104903415
                    else:
                        if input[3] < 0.12883902:
                            if input[1] < -0.53642166:
                                var19 = 0.08159815
                            else:
                                var19 = 0.0108271185
                        else:
                            if input[0] < 0.05038005:
                                var19 = 0.235264
                            else:
                                var19 = 0.052228983
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[0] < 0.93445706:
                        if input[3] < 0.12883902:
                            if input[7] < 0.8726697:
                                var19 = -0.05186252
                            else:
                                var19 = -0.11901254
                        else:
                            if input[0] < 0.05038005:
                                var19 = 0.34526002
                            else:
                                var19 = -0.12053091
                    else:
                        var19 = 0.15299511
                else:
                    var19 = 0.1532369
            else:
                var19 = 0.15339902
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var19 = 0.15328543
            else:
                if input[0] < 0.93445706:
                    if input[10] < 2.0151885:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var19 = -0.104354106
                            else:
                                var19 = 0.36425605
                        else:
                            if input[4] < 0.97290224:
                                var19 = -0.12489754
                            else:
                                var19 = 0.12176484
                    else:
                        var19 = 0.14266372
                else:
                    var19 = 0.1528258
        else:
            var19 = 0.15363397
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var20 = 0.1530213
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[6] < 0.17672138:
                        if input[3] < -0.19687115:
                            if input[0] < 0.93445706:
                                var20 = -0.12735382
                            else:
                                var20 = 0.15055864
                        else:
                            if input[0] < -0.7533263:
                                var20 = 0.27885664
                            else:
                                var20 = -0.096662916
                    else:
                        if input[7] < 0.8726697:
                            if input[0] < 0.93445706:
                                var20 = 0.2059361
                            else:
                                var20 = 0.14994906
                        else:
                            if input[3] < -0.19687115:
                                var20 = -0.12467886
                            else:
                                var20 = -0.038195852
                else:
                    var20 = 0.15266712
            else:
                var20 = 0.15285273
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var20 = 0.15269677
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.5175034:
                        if input[5] < -0.55487835:
                            var20 = 0.13644439
                        else:
                            var20 = 0.027050668
                    else:
                        if input[10] < 2.0151885:
                            if input[7] < 0.8726697:
                                var20 = -0.009739785
                            else:
                                var20 = -0.12110412
                        else:
                            var20 = 0.13449575
                else:
                    var20 = 0.15216589
        else:
            var20 = 0.15310003
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var21 = 0.15254982
            else:
                if input[6] < -1.4519056:
                    var21 = -0.07210911
                else:
                    if input[1] < 0.6226151:
                        if input[2] < -0.67637277:
                            if input[0] < 0.45223323:
                                var21 = 0.1784592
                            else:
                                var21 = 0.052941326
                        else:
                            if input[0] < -1.3159207:
                                var21 = 0.15598163
                            else:
                                var21 = 0.03429687
                    else:
                        if input[0] < 0.8540864:
                            if input[6] < -1.2192446:
                                var21 = 0.11358739
                            else:
                                var21 = -0.008026715
                        else:
                            if input[2] < 0.022420364:
                                var21 = 0.1574601
                            else:
                                var21 = 0.011009429
        else:
            if input[10] < 2.0151885:
                if input[0] < 0.93445706:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var21 = -0.047826063
                            else:
                                var21 = 1.029741
                        else:
                            if input[1] < -1.4636511:
                                var21 = 0.013954116
                            else:
                                var21 = -0.090868115
                    else:
                        if input[4] < 0.97290224:
                            if input[6] < 0.17672138:
                                var21 = -0.12203323
                            else:
                                var21 = -0.056252863
                        else:
                            var21 = 0.15125555
                else:
                    var21 = 0.15241173
            else:
                var21 = 0.15232629
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var21 = 0.15217428
            else:
                if input[0] < 0.93445706:
                    if input[4] < 0.97290224:
                        if input[6] < 0.17672138:
                            if input[2] < -1.3751659:
                                var21 = 0.17242405
                            else:
                                var21 = -0.112498626
                        else:
                            if input[7] < 0.8726697:
                                var21 = 0.3026531
                            else:
                                var21 = -0.10433902
                    else:
                        var21 = 0.13880591
                else:
                    var21 = 0.15156105
        else:
            var21 = 0.15264098
    if input[3] < 0.12883902:
        if input[5] < -0.55487835:
            var22 = 0.1520915
        else:
            if input[10] < 2.0151885:
                if input[0] < 0.93445706:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[0] < -0.7533263:
                                var22 = -0.054052226
                            else:
                                var22 = -0.12742232
                        else:
                            if input[4] < 0.97290224:
                                var22 = 0.19650201
                            else:
                                var22 = 0.14782418
                    else:
                        if input[0] < -0.7533263:
                            if input[3] < -0.19687115:
                                var22 = -0.10310395
                            else:
                                var22 = 0.30719173
                        else:
                            if input[1] < -0.36256617:
                                var22 = -0.078434244
                            else:
                                var22 = -0.15087341
                else:
                    var22 = 0.151727
            else:
                var22 = 0.15180245
    else:
        if input[0] < 0.05038005:
            if input[3] < 0.45454916:
                if input[0] < -0.7533263:
                    var22 = 0.15798339
                else:
                    if input[5] < -0.55487835:
                        var22 = 0.14787118
                    else:
                        if input[10] < 2.0151885:
                            if input[4] < 0.97290224:
                                var22 = 0.38960865
                            else:
                                var22 = 0.13821082
                        else:
                            var22 = 0.14249837
            else:
                var22 = 0.15217681
        else:
            if input[3] < 0.45454916:
                if input[0] < 0.93445706:
                    if input[5] < -0.53826725:
                        if input[5] < -0.55487835:
                            var22 = 0.14814648
                        else:
                            if input[4] < -1.0856943:
                                var22 = 0.19008015
                            else:
                                var22 = -0.052534353
                    else:
                        if input[6] < 0.17672138:
                            if input[10] < 2.0151885:
                                var22 = -0.13764091
                            else:
                                var22 = 0.13445288
                        else:
                            if input[7] < 0.8726697:
                                var22 = 0.20587005
                            else:
                                var22 = -0.12230052
                else:
                    var22 = 0.15120286
            else:
                if input[3] < 0.7802593:
                    if input[0] < 0.93445706:
                        if input[0] < 0.8540864:
                            var22 = 0.15034914
                        else:
                            if input[5] < -0.5175034:
                                var22 = 0.11786157
                            else:
                                var22 = -0.051667877
                    else:
                        var22 = 0.15099663
                else:
                    var22 = 0.15217313
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var23 = 0.15178066
            else:
                if input[6] < -1.4519056:
                    var23 = -0.061933093
                else:
                    if input[6] < -1.2192446:
                        if input[0] < -0.35147312:
                            if input[1] < -0.420518:
                                var23 = 0.084854454
                            else:
                                var23 = -0.07658782
                        else:
                            if input[4] < -0.96460044:
                                var23 = 0.04952215
                            else:
                                var23 = 0.26918438
                    else:
                        if input[0] < -1.476662:
                            if input[11] < 1.2236042:
                                var23 = 0.020350683
                            else:
                                var23 = 0.18812105
                        else:
                            if input[0] < 0.8540864:
                                var23 = 0.028372841
                            else:
                                var23 = 0.12931675
        else:
            if input[4] < 0.97290224:
                if input[0] < 0.93445706:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var23 = -0.04092487
                            else:
                                var23 = 0.9220417
                        else:
                            if input[1] < -1.4636511:
                                var23 = 0.017417677
                            else:
                                var23 = -0.08455798
                    else:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var23 = -0.060689926
                            else:
                                var23 = -0.1430638
                        else:
                            if input[0] < -0.7533263:
                                var23 = 0.24944647
                            else:
                                var23 = -0.08277196
                else:
                    var23 = 0.15143965
            else:
                var23 = 0.15181632
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var23 = 0.15127753
            else:
                if input[0] < 0.93445706:
                    if input[10] < 2.0151885:
                        if input[4] < 0.97290224:
                            if input[6] < 0.17672138:
                                var23 = -0.104669064
                            else:
                                var23 = 0.009018569
                        else:
                            var23 = 0.13237152
                    else:
                        var23 = 0.1376749
                else:
                    var23 = 0.1504593
        else:
            var23 = 0.15190284
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var24 = 0.1514636
        else:
            if input[10] < 2.0151885:
                if input[4] < 0.97290224:
                    if input[6] < 0.17672138:
                        if input[3] < -0.19687115:
                            if input[1] < -0.36256617:
                                var24 = -0.058566798
                            else:
                                var24 = -0.14016375
                        else:
                            if input[0] < -0.7533263:
                                var24 = 0.2383246
                            else:
                                var24 = -0.07878249
                    else:
                        if input[7] < 0.8726697:
                            if input[0] < 0.93445706:
                                var24 = 0.19202326
                            else:
                                var24 = 0.14607501
                        else:
                            if input[3] < 0.12883902:
                                var24 = -0.09796516
                            else:
                                var24 = 0.025755059
                else:
                    var24 = 0.15131135
            else:
                var24 = 0.15139055
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var24 = 0.1508812
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.55487835:
                        var24 = 0.1314702
                    else:
                        if input[2] < -1.3751659:
                            var24 = 0.1916404
                        else:
                            if input[6] < 0.17672138:
                                var24 = -0.10092573
                            else:
                                var24 = 0.013284782
                else:
                    var24 = 0.14993674
        else:
            var24 = 0.15160525
    if input[3] < 0.12883902:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var25 = 0.15110648
            else:
                if input[4] < -0.96460044:
                    if input[3] < -0.84829146:
                        var25 = -0.085682385
                    else:
                        if input[0] < -0.43184376:
                            if input[1] < -0.18871064:
                                var25 = -0.025737029
                            else:
                                var25 = 0.13387313
                        else:
                            if input[2] < -0.09404516:
                                var25 = 0.031175258
                            else:
                                var25 = -0.089797564
                else:
                    if input[1] < 0.79647064:
                        if input[1] < -0.94208455:
                            if input[0] < -0.029990584:
                                var25 = -0.05246818
                            else:
                                var25 = 0.12254233
                        else:
                            if input[1] < -0.36256617:
                                var25 = 0.2023452
                            else:
                                var25 = 0.07109509
                    else:
                        if input[1] < 1.2021335:
                            if input[4] < 0.24633874:
                                var25 = -0.09955361
                            else:
                                var25 = 0.007534893
                        else:
                            if input[4] < -0.35913086:
                                var25 = -0.059937686
                            else:
                                var25 = 0.09721152
        else:
            if input[10] < 2.0151885:
                if input[0] < -1.5570326:
                    if input[3] < -0.5225813:
                        if input[1] < -0.36256617:
                            if input[2] < -0.67637277:
                                var25 = 0.18058442
                            else:
                                var25 = -0.07596193
                        else:
                            if input[6] < 0.17672138:
                                var25 = -0.14716694
                            else:
                                var25 = -0.0586093
                    else:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var25 = 0.9691092
                            else:
                                var25 = 3.716824
                        else:
                            var25 = 0.24282831
                else:
                    if input[0] < 0.93445706:
                        if input[6] < 0.17672138:
                            if input[1] < -0.36256617:
                                var25 = -0.053402197
                            else:
                                var25 = -0.13087906
                        else:
                            if input[7] < 0.8726697:
                                var25 = 0.18291606
                            else:
                                var25 = -0.1007571
                    else:
                        var25 = 0.15077384
            else:
                var25 = 0.15084639
    else:
        if input[0] < 0.05038005:
            if input[3] < 0.45454916:
                if input[0] < -0.7533263:
                    var25 = 0.15491273
                else:
                    if input[5] < -0.55487835:
                        var25 = 0.1447073
                    else:
                        if input[10] < 2.0151885:
                            if input[4] < 0.97290224:
                                var25 = 0.33906358
                            else:
                                var25 = 0.13082394
                        else:
                            var25 = 0.13869292
            else:
                var25 = 0.15123858
        else:
            if input[3] < 0.45454916:
                if input[0] < 0.93445706:
                    if input[5] < -0.53826725:
                        if input[5] < -0.55487835:
                            var25 = 0.14511731
                        else:
                            if input[4] < -0.48022476:
                                var25 = 0.12332879
                            else:
                                var25 = -0.08699145
                    else:
                        if input[6] < 0.17672138:
                            if input[4] < 0.97290224:
                                var25 = -0.13147719
                            else:
                                var25 = 0.12996812
                        else:
                            if input[7] < 0.8726697:
                                var25 = 0.19048321
                            else:
                                var25 = -0.11768458
                else:
                    var25 = 0.14981611
            else:
                if input[3] < 0.7802593:
                    if input[0] < 0.93445706:
                        if input[0] < 0.8540864:
                            var25 = 0.14843385
                        else:
                            if input[7] < 0.8726697:
                                var25 = 0.03390229
                            else:
                                var25 = -0.06649806
                    else:
                        var25 = 0.14941733
                else:
                    var25 = 0.1512337
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var26 = 0.15092723
        else:
            if input[4] < 0.97290224:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var26 = 0.052334204
                            else:
                                var26 = -0.079031065
                        else:
                            if input[3] < -0.19687115:
                                var26 = 0.7681984
                            else:
                                var26 = 0.4651259
                    else:
                        if input[3] < -0.19687115:
                            if input[10] < 2.0151885:
                                var26 = -0.100898765
                            else:
                                var26 = 0.14303313
                        else:
                            if input[0] < -0.7533263:
                                var26 = 0.23070255
                            else:
                                var26 = -0.060048264
                else:
                    if input[3] < -0.19687115:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var26 = -0.124583855
                            else:
                                var26 = 0.17631339
                        else:
                            if input[0] < 0.93445706:
                                var26 = -0.12980253
                            else:
                                var26 = 0.14730445
                    else:
                        if input[0] < -0.7533263:
                            if input[3] < 0.12883902:
                                var26 = 0.25610745
                            else:
                                var26 = 0.15432373
                        else:
                            if input[3] < 0.12883902:
                                var26 = -0.10781677
                            else:
                                var26 = 0.0034924725
            else:
                var26 = 0.15100451
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var26 = 0.15014675
            else:
                if input[0] < 0.93445706:
                    if input[10] < 2.0151885:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var26 = -0.08794995
                            else:
                                var26 = 0.26476073
                        else:
                            if input[4] < 0.97290224:
                                var26 = -0.10287207
                            else:
                                var26 = 0.11527295
                    else:
                        var26 = 0.13557658
                else:
                    var26 = 0.14888985
        else:
            var26 = 0.15111703
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var27 = 0.15069436
            else:
                if input[0] < -1.476662:
                    if input[11] < 1.2236042:
                        var27 = 0.00617011
                    else:
                        if input[6] < -0.28860062:
                            var27 = 0.24618864
                        else:
                            if input[4] < 0.0041509015:
                                var27 = 0.1000436
                            else:
                                var27 = -0.0011640098
                else:
                    if input[6] < -1.4519056:
                        var27 = -0.052993227
                    else:
                        if input[6] < -1.2192446:
                            if input[0] < -0.35147312:
                                var27 = -0.010284709
                            else:
                                var27 = 0.20676231
                        else:
                            if input[0] < 0.8540864:
                                var27 = 0.031709075
                            else:
                                var27 = 0.121621706
        else:
            if input[10] < 2.0151885:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var27 = 0.04167899
                            else:
                                var27 = -0.07182944
                        else:
                            if input[0] < 0.93445706:
                                var27 = 0.45283937
                            else:
                                var27 = 0.12937471
                    else:
                        if input[3] < 0.12883902:
                            if input[6] < 0.17672138:
                                var27 = -0.110219605
                            else:
                                var27 = -0.033951312
                        else:
                            if input[0] < 0.05038005:
                                var27 = 0.2730344
                            else:
                                var27 = -0.10439525
                else:
                    if input[3] < -0.19687115:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var27 = -0.121158876
                            else:
                                var27 = 0.1721134
                        else:
                            if input[4] < 0.97290224:
                                var27 = -0.12845394
                            else:
                                var27 = 0.14734986
                    else:
                        if input[0] < -0.7533263:
                            if input[3] < 0.12883902:
                                var27 = 0.23368974
                            else:
                                var27 = 0.15261929
                        else:
                            if input[0] < 0.05038005:
                                var27 = 0.013698982
                            else:
                                var27 = -0.09968609
            else:
                var27 = 0.15064776
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var27 = 0.14979145
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.5175034:
                        if input[5] < -0.55487835:
                            var27 = 0.12988396
                        else:
                            var27 = 0.03220145
                    else:
                        if input[2] < -0.67637277:
                            if input[2] < -1.3751659:
                                var27 = 0.18590507
                            else:
                                var27 = 0.024457838
                        else:
                            if input[4] < 0.97290224:
                                var27 = -0.08404316
                            else:
                                var27 = 0.118759245
                else:
                    var27 = 0.14834331
        else:
            var27 = 0.15091455
    if input[3] < 0.12883902:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var28 = 0.15036164
            else:
                if input[1] < -1.6375066:
                    var28 = 0.1941385
                else:
                    if input[1] < -1.1159401:
                        if input[3] < -0.19687115:
                            if input[9] < 1.3985938:
                                var28 = -0.101120226
                            else:
                                var28 = -0.020391658
                        else:
                            var28 = 0.08897686
                    else:
                        if input[4] < -0.60131866:
                            if input[7] < 0.8726697:
                                var28 = 0.06352125
                            else:
                                var28 = -0.031572845
                        else:
                            if input[1] < -0.36256617:
                                var28 = 0.157618
                            else:
                                var28 = 0.043302536
        else:
            if input[0] < 0.93445706:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var28 = -0.05953156
                            else:
                                var28 = 0.5162598
                        else:
                            if input[4] < 0.97290224:
                                var28 = -0.08018012
                            else:
                                var28 = 0.1456429
                    else:
                        if input[4] < 0.97290224:
                            if input[6] < 0.17672138:
                                var28 = 0.21109115
                            else:
                                var28 = 0.24669178
                        else:
                            var28 = 0.133338
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[1] < -0.36256617:
                                var28 = -0.058987465
                            else:
                                var28 = -0.14218444
                        else:
                            var28 = 0.17535643
                    else:
                        if input[1] < -0.36256617:
                            if input[2] < -0.67637277:
                                var28 = 0.10917643
                            else:
                                var28 = -0.11542461
                        else:
                            if input[4] < 0.97290224:
                                var28 = -0.14790803
                            else:
                                var28 = 0.14521423
            else:
                var28 = 0.15058248
    else:
        if input[0] < 0.05038005:
            if input[3] < 0.45454916:
                if input[0] < -0.7533263:
                    var28 = 0.15186992
                else:
                    if input[5] < -0.55487835:
                        var28 = 0.14072375
                    else:
                        if input[10] < 2.0151885:
                            if input[4] < 0.97290224:
                                var28 = 0.2817007
                            else:
                                var28 = 0.12349435
                        else:
                            var28 = 0.13388929
            else:
                var28 = 0.15056674
        else:
            if input[3] < 0.45454916:
                if input[0] < 0.93445706:
                    if input[6] < 0.17672138:
                        if input[5] < -0.53826725:
                            if input[5] < -0.55487835:
                                var28 = 0.13298768
                            else:
                                var28 = -0.007018995
                        else:
                            if input[10] < 2.0151885:
                                var28 = -0.12732677
                            else:
                                var28 = 0.1261249
                    else:
                        if input[7] < 0.8726697:
                            var28 = 0.18536794
                        else:
                            if input[10] < 2.0151885:
                                var28 = -0.11158094
                            else:
                                var28 = 0.12580577
                else:
                    var28 = 0.14893301
            else:
                if input[3] < 0.7802593:
                    if input[0] < 0.93445706:
                        if input[0] < 0.8540864:
                            var28 = 0.14627178
                        else:
                            if input[10] < 2.0151885:
                                var28 = -0.029331584
                            else:
                                var28 = 0.13221471
                    else:
                        var28 = 0.14776678
                else:
                    var28 = 0.15055978
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var29 = 0.15027745
        else:
            if input[0] < 0.93445706:
                if input[4] < 0.97290224:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var29 = -0.03284388
                            else:
                                var29 = 0.35149893
                        else:
                            if input[7] < 0.8726697:
                                var29 = -0.016142873
                            else:
                                var29 = -0.09120999
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var29 = 0.1836028
                            else:
                                var29 = -0.09151156
                        else:
                            if input[3] < 0.12883902:
                                var29 = -0.085641846
                            else:
                                var29 = 0.0074279574
                else:
                    var29 = 0.15033133
            else:
                var29 = 0.15048206
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var29 = 0.14906631
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.5175034:
                        if input[5] < -0.55487835:
                            var29 = 0.12685221
                        else:
                            var29 = 0.03143747
                    else:
                        if input[2] < -0.67637277:
                            if input[2] < -1.3751659:
                                var29 = 0.17388956
                            else:
                                var29 = 0.023184733
                        else:
                            if input[6] < 0.17672138:
                                var29 = -0.10713538
                            else:
                                var29 = 0.0062275184
                else:
                    var29 = 0.14714919
        else:
            var29 = 0.15056932
    if input[3] < 0.45454916:
        if input[5] < -0.55487835:
            var30 = 0.15007904
        else:
            if input[10] < 2.0151885:
                if input[6] < 0.17672138:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[1] < -0.420518:
                                var30 = -0.026319778
                            else:
                                var30 = -0.13887247
                        else:
                            if input[3] < -0.19687115:
                                var30 = 0.63862836
                            else:
                                var30 = 0.17506483
                    else:
                        if input[3] < 0.12883902:
                            if input[1] < -0.36256617:
                                var30 = -0.038882855
                            else:
                                var30 = -0.11213132
                        else:
                            if input[0] < 0.05038005:
                                var30 = 0.23998919
                            else:
                                var30 = -0.11098411
                else:
                    if input[7] < 0.8726697:
                        var30 = 0.17436549
                    else:
                        if input[3] < -0.19687115:
                            if input[1] < -0.36256617:
                                var30 = -0.03533485
                            else:
                                var30 = -0.13126005
                        else:
                            if input[0] < -0.7533263:
                                var30 = 0.22205253
                            else:
                                var30 = -0.057052832
            else:
                var30 = 0.1503315
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var30 = 0.14868046
            else:
                if input[0] < 0.93445706:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[4] < 0.97290224:
                                var30 = -0.085263595
                            else:
                                var30 = 0.10252174
                        else:
                            var30 = 0.2390917
                    else:
                        if input[10] < 2.0151885:
                            if input[5] < -0.5270547:
                                var30 = 0.09783914
                            else:
                                var30 = -0.096981116
                        else:
                            var30 = 0.117308125
                else:
                    var30 = 0.14647917
        else:
            var30 = 0.15041836
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var31 = 0.14988302
            else:
                if input[0] < -1.476662:
                    if input[11] < 1.2236042:
                        var31 = 0.008781456
                    else:
                        if input[7] < 0.8726697:
                            var31 = 0.036393687
                        else:
                            if input[4] < -0.11694302:
                                var31 = 0.07441764
                            else:
                                var31 = 0.2732109
                else:
                    if input[4] < -1.2067883:
                        if input[1] < 1.1441816:
                            if input[3] < 0.12883902:
                                var31 = -0.07969031
                            else:
                                var31 = 0.010114381
                        else:
                            var31 = 0.15948832
                    else:
                        if input[3] < -0.5225813:
                            if input[8] < 1.4017887:
                                var31 = 0.06591749
                            else:
                                var31 = -0.045954436
                        else:
                            if input[4] < -0.23803693:
                                var31 = 0.1424261
                            else:
                                var31 = 0.034211274
        else:
            if input[0] < 0.93445706:
                if input[0] < 0.05038005:
                    if input[3] < 0.12883902:
                        if input[0] < -0.7533263:
                            if input[3] < -0.19687115:
                                var31 = -0.040748075
                            else:
                                var31 = 0.2097908
                        else:
                            if input[7] < 0.8726697:
                                var31 = -0.027781246
                            else:
                                var31 = -0.09768178
                    else:
                        if input[0] < -0.7533263:
                            var31 = 0.1492496
                        else:
                            if input[10] < 2.0151885:
                                var31 = 0.23838176
                            else:
                                var31 = 0.12790063
                else:
                    if input[4] < 0.97290224:
                        if input[6] < 0.17672138:
                            if input[1] < -0.36256617:
                                var31 = -0.05796548
                            else:
                                var31 = -0.14614864
                        else:
                            if input[7] < 0.8726697:
                                var31 = 0.17169772
                            else:
                                var31 = -0.10610611
                    else:
                        var31 = 0.1479793
            else:
                var31 = 0.1502033
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var31 = 0.14826871
            else:
                if input[0] < 0.93445706:
                    if input[4] < 0.97290224:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var31 = -0.077305235
                            else:
                                var31 = 0.2179964
                        else:
                            if input[10] < 2.0151885:
                                var31 = -0.0915682
                            else:
                                var31 = 0.108766995
                    else:
                        var31 = 0.13057742
                else:
                    var31 = 0.14574511
        else:
            var31 = 0.15027717
    if input[3] < 0.45454916:
        if input[10] < 2.0151885:
            if input[4] < 0.97290224:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var32 = 0.043177627
                            else:
                                var32 = -0.07279193
                        else:
                            if input[5] < -0.55487835:
                                var32 = 0.12643485
                            else:
                                var32 = 0.31022805
                    else:
                        if input[6] < 0.17672138:
                            if input[3] < -0.19687115:
                                var32 = -0.11963034
                            else:
                                var32 = -0.024820799
                        else:
                            if input[7] < 0.8726697:
                                var32 = 0.1720543
                            else:
                                var32 = -0.08344045
                else:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var32 = 1.6182349
                            else:
                                var32 = -0.08386092
                        else:
                            if input[0] < 0.93445706:
                                var32 = -0.10707978
                            else:
                                var32 = 0.09964163
                    else:
                        if input[0] < 0.93445706:
                            if input[0] < 0.05038005:
                                var32 = -0.03784399
                            else:
                                var32 = -0.11047113
                        else:
                            var32 = 0.14894882
            else:
                var32 = 0.15008523
        else:
            var32 = 0.15019508
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var32 = 0.14782293
            else:
                if input[0] < 0.93445706:
                    if input[2] < -1.3751659:
                        var32 = 0.17224035
                    else:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var32 = -0.049542855
                            else:
                                var32 = 0.12116009
                        else:
                            var32 = 0.12585512
                else:
                    var32 = 0.14493503
        else:
            var32 = 0.15014246
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var33 = 0.14957711
            else:
                if input[1] < -0.94208455:
                    if input[0] < -0.029990584:
                        if input[0] < -1.476662:
                            var33 = 0.04892308
                        else:
                            if input[1] < -1.1738919:
                                var33 = -0.097380765
                            else:
                                var33 = -0.013227333
                    else:
                        if input[6] < -0.055939615:
                            if input[6] < -0.9865836:
                                var33 = -0.0028328884
                            else:
                                var33 = 0.23347214
                        else:
                            if input[0] < 0.6129745:
                                var33 = -0.08622953
                            else:
                                var33 = -0.0101418905
                else:
                    if input[1] < 1.5498445:
                        if input[6] < -1.4519056:
                            var33 = -0.03509068
                        else:
                            if input[6] < -1.1029141:
                                var33 = 0.1798361
                            else:
                                var33 = 0.06874598
                    else:
                        if input[2] < 0.48828247:
                            var33 = -0.06648842
                        else:
                            var33 = 0.035213243
        else:
            if input[10] < 2.0151885:
                if input[6] < 0.17672138:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var33 = -0.045746267
                            else:
                                var33 = 0.27036175
                        else:
                            if input[3] < -0.19687115:
                                var33 = -0.115807064
                            else:
                                var33 = -0.021374997
                    else:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var33 = -0.12432935
                            else:
                                var33 = 0.3938065
                        else:
                            if input[3] < -0.19687115:
                                var33 = -0.11940576
                            else:
                                var33 = -0.035424564
                else:
                    if input[7] < 0.8726697:
                        var33 = 0.17000154
                    else:
                        if input[3] < -0.19687115:
                            if input[1] < -0.36256617:
                                var33 = -0.02774014
                            else:
                                var33 = -0.12679495
                        else:
                            if input[0] < -0.7533263:
                                var33 = 0.20119712
                            else:
                                var33 = -0.045679636
            else:
                var33 = 0.14966854
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var33 = 0.14733437
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.5175034:
                        if input[5] < -0.55487835:
                            var33 = 0.12341579
                        else:
                            var33 = 0.030518109
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var33 = 0.13428308
                            else:
                                var33 = 0.009762477
                        else:
                            if input[4] < 0.97290224:
                                var33 = -0.06942571
                            else:
                                var33 = 0.108725734
                else:
                    var33 = 0.1440366
        else:
            var33 = 0.15001129
    if input[3] < 0.12883902:
        if input[4] < 0.97290224:
            if input[0] < 0.93445706:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var34 = -0.03827384
                            else:
                                var34 = 0.3785857
                        else:
                            if input[6] < 0.17672138:
                                var34 = -0.09373022
                            else:
                                var34 = -0.015825784
                    else:
                        var34 = 0.19830893
                else:
                    if input[6] < 0.17672138:
                        if input[1] < -0.36256617:
                            if input[2] < -0.67637277:
                                var34 = 0.070577756
                            else:
                                var34 = -0.10133589
                        else:
                            if input[10] < 2.0151885:
                                var34 = -0.14320022
                            else:
                                var34 = 0.14261833
                    else:
                        if input[7] < 0.8726697:
                            var34 = 0.16502537
                        else:
                            if input[1] < -0.36256617:
                                var34 = -0.038599443
                            else:
                                var34 = -0.1374241
            else:
                var34 = 0.14940195
        else:
            var34 = 0.14984143
    else:
        if input[0] < 0.05038005:
            if input[3] < 0.45454916:
                if input[0] < -0.7533263:
                    var34 = 0.14789784
                else:
                    if input[5] < -0.55487835:
                        var34 = 0.12931666
                    else:
                        if input[10] < 2.0151885:
                            var34 = 0.22626072
                        else:
                            var34 = 0.118357286
            else:
                var34 = 0.14947687
        else:
            if input[3] < 0.45454916:
                if input[0] < 0.93445706:
                    if input[6] < 0.17672138:
                        if input[4] < 0.97290224:
                            if input[10] < 2.0151885:
                                var34 = -0.11602546
                            else:
                                var34 = 0.114767484
                        else:
                            var34 = 0.12379251
                    else:
                        if input[7] < 0.8726697:
                            var34 = 0.16640744
                        else:
                            if input[2] < -0.67637277:
                                var34 = -0.012494897
                            else:
                                var34 = -0.12136921
                else:
                    var34 = 0.14605732
            else:
                if input[3] < 0.7802593:
                    if input[0] < 0.93445706:
                        if input[0] < 0.8540864:
                            var34 = 0.139625
                        else:
                            if input[7] < 0.8726697:
                                var34 = 0.042038642
                            else:
                                var34 = -0.044535007
                    else:
                        var34 = 0.14303702
                else:
                    var34 = 0.14946005
    if input[3] < 0.45454916:
        if input[5] < -0.53826725:
            if input[5] < -0.55487835:
                var35 = 0.14926626
            else:
                if input[1] < -0.94208455:
                    if input[0] < -0.029990584:
                        if input[0] < -1.476662:
                            var35 = 0.048543576
                        else:
                            if input[1] < -1.1738919:
                                var35 = -0.09159426
                            else:
                                var35 = -0.015083841
                    else:
                        if input[6] < -0.055939615:
                            if input[0] < 0.6129745:
                                var35 = 0.19395562
                            else:
                                var35 = -0.01891987
                        else:
                            var35 = -0.0639165
                else:
                    if input[1] < 1.5498445:
                        if input[6] < -0.28860062:
                            if input[1] < -0.1307588:
                                var35 = 0.026286075
                            else:
                                var35 = 0.14848876
                        else:
                            if input[6] < -0.055939615:
                                var35 = -0.06356964
                            else:
                                var35 = 0.07418172
                    else:
                        if input[0] < 0.05038005:
                            var35 = 0.030125136
                        else:
                            var35 = -0.06528474
        else:
            if input[4] < 0.97290224:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var35 = 0.033946406
                            else:
                                var35 = -0.073764324
                        else:
                            if input[0] < 0.93445706:
                                var35 = 0.25375476
                            else:
                                var35 = 0.09264526
                    else:
                        if input[0] < 0.05038005:
                            if input[3] < 0.12883902:
                                var35 = -0.04350209
                            else:
                                var35 = 0.19781022
                        else:
                            if input[0] < 0.93445706:
                                var35 = -0.10805443
                            else:
                                var35 = 0.14257552
                else:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var35 = 1.1999214
                            else:
                                var35 = -0.07640571
                        else:
                            if input[3] < -0.19687115:
                                var35 = -0.118830636
                            else:
                                var35 = -0.05685683
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var35 = -0.08390711
                            else:
                                var35 = 0.16493446
                        else:
                            if input[3] < -0.19687115:
                                var35 = -0.12546054
                            else:
                                var35 = -0.03257972
            else:
                var35 = 0.14944638
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var35 = 0.14619473
            else:
                if input[0] < 0.93445706:
                    if input[2] < -1.3751659:
                        var35 = 0.15641502
                    else:
                        if input[5] < -0.5175034:
                            if input[2] < -0.44344172:
                                var35 = 0.02312201
                            else:
                                var35 = 0.12157891
                        else:
                            if input[6] < 0.17672138:
                                var35 = -0.07865679
                            else:
                                var35 = 0.024544366
                else:
                    var35 = 0.14192393
        else:
            var35 = 0.149748
    if input[3] < 0.12883902:
        if input[10] < 2.0151885:
            if input[0] < 0.93445706:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var36 = -0.034794968
                            else:
                                var36 = 0.34504554
                        else:
                            if input[6] < 0.17672138:
                                var36 = -0.08829982
                            else:
                                var36 = -0.01489285
                    else:
                        var36 = 0.19209607
                else:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var36 = -0.055340197
                            else:
                                var36 = 0.22314687
                        else:
                            if input[7] < 0.8726697:
                                var36 = -0.038407966
                            else:
                                var36 = -0.13001274
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var36 = 0.14944445
                            else:
                                var36 = -0.122990556
                        else:
                            if input[4] < 0.97290224:
                                var36 = -0.10575072
                            else:
                                var36 = 0.14549902
            else:
                var36 = 0.14902526
        else:
            var36 = 0.14942949
    else:
        if input[0] < 0.05038005:
            if input[3] < 0.45454916:
                if input[0] < -0.7533263:
                    var36 = 0.14678597
                else:
                    var36 = 0.20938364
            else:
                var36 = 0.14906809
        else:
            if input[3] < 0.45454916:
                if input[0] < 0.93445706:
                    if input[6] < 0.17672138:
                        if input[2] < -0.79283834:
                            if input[1] < -0.36256617:
                                var36 = 0.070258416
                            else:
                                var36 = -0.12723155
                        else:
                            if input[10] < 2.0151885:
                                var36 = -0.12781622
                            else:
                                var36 = 0.10851434
                    else:
                        if input[7] < 0.8726697:
                            var36 = 0.16092509
                        else:
                            if input[1] < -0.30461434:
                                var36 = -0.03108505
                            else:
                                var36 = -0.12877816
                else:
                    var36 = 0.14482535
            else:
                if input[3] < 0.7802593:
                    if input[0] < 0.93445706:
                        if input[0] < 0.8540864:
                            var36 = 0.13632245
                        else:
                            if input[10] < 2.0151885:
                                var36 = -0.0147102885
                            else:
                                var36 = 0.12263277
                    else:
                        var36 = 0.14068446
                else:
                    var36 = 0.1490454
    if input[5] < -0.55487835:
        var37 = 0.14964789
    else:
        if input[10] < 2.0151885:
            if input[4] < 0.97290224:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var37 = 0.07379351
                            else:
                                var37 = -0.055858057
                        else:
                            var37 = 0.18576628
                    else:
                        if input[6] < 0.17672138:
                            if input[1] < -1.4636511:
                                var37 = 0.020444466
                            else:
                                var37 = -0.106374815
                        else:
                            if input[7] < 0.8726697:
                                var37 = 0.16306868
                            else:
                                var37 = -0.087212205
                else:
                    if input[0] < 0.05038005:
                        if input[0] < -0.7533263:
                            var37 = 0.14668342
                        else:
                            if input[3] < 0.45454916:
                                var37 = 0.20070025
                            else:
                                var37 = 0.13863197
                    else:
                        if input[0] < 0.93445706:
                            if input[3] < 0.7802593:
                                var37 = -0.07612069
                            else:
                                var37 = 0.13786423
                        else:
                            var37 = 0.14543426
            else:
                var37 = 0.14944103
        else:
            var37 = 0.14965318
    if input[5] < -0.53826725:
        if input[5] < -0.55487835:
            var38 = 0.14948627
        else:
            if input[6] < -1.4519056:
                var38 = -0.05285721
            else:
                if input[6] < -0.28860062:
                    if input[1] < -0.1307588:
                        if input[1] < -0.420518:
                            if input[9] < 1.3985938:
                                var38 = 0.02384529
                            else:
                                var38 = 0.19591084
                        else:
                            var38 = -0.078511156
                    else:
                        if input[3] < -0.19687115:
                            if input[7] < 0.8726697:
                                var38 = 0.08260226
                            else:
                                var38 = 0.28960064
                        else:
                            if input[0] < 0.13075069:
                                var38 = -0.049061414
                            else:
                                var38 = 0.11652498
                else:
                    if input[2] < 0.48828247:
                        if input[2] < -0.09404516:
                            if input[1] < -0.47846985:
                                var38 = 0.092578635
                            else:
                                var38 = 0.0157249
                        else:
                            if input[7] < 0.8726697:
                                var38 = 0.007802759
                            else:
                                var38 = -0.102995254
                    else:
                        if input[3] < -0.84829146:
                            var38 = -0.084158815
                        else:
                            if input[6] < 1.5726874:
                                var38 = 0.1874893
                            else:
                                var38 = -0.018339856
    else:
        if input[0] < 0.93445706:
            if input[10] < 2.0151885:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[8] < 1.4017887:
                                var38 = 0.024708463
                            else:
                                var38 = -0.09380277
                        else:
                            if input[3] < 0.7802593:
                                var38 = 0.23026653
                            else:
                                var38 = 0.11069147
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var38 = -0.079258
                            else:
                                var38 = 0.16588269
                        else:
                            if input[3] < -0.19687115:
                                var38 = -0.12194689
                            else:
                                var38 = -0.01866272
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[0] < -1.5570326:
                                var38 = 0.10821288
                            else:
                                var38 = -0.077712245
                        else:
                            var38 = 0.16411605
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var38 = 0.14072467
                            else:
                                var38 = -0.11268536
                        else:
                            if input[3] < 0.12883902:
                                var38 = -0.11253859
                            else:
                                var38 = 0.003852398
            else:
                var38 = 0.14907825
        else:
            var38 = 0.14934634
    if input[5] < -0.55487835:
        var39 = 0.14931352
    else:
        if input[4] < 0.97290224:
            if input[0] < 0.93445706:
                if input[0] < 0.05038005:
                    if input[3] < 0.12883902:
                        if input[0] < -0.7533263:
                            if input[3] < -0.19687115:
                                var39 = -0.02471844
                            else:
                                var39 = 0.18154567
                        else:
                            if input[6] < 0.17672138:
                                var39 = -0.09061253
                            else:
                                var39 = -0.018838655
                    else:
                        if input[3] < 0.45454916:
                            var39 = 0.18828656
                        else:
                            var39 = 0.14570472
                else:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var39 = -0.042030636
                            else:
                                var39 = 0.2135079
                        else:
                            if input[1] < -1.4636511:
                                var39 = 0.027121065
                            else:
                                var39 = -0.10218307
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var39 = -0.13111724
                            else:
                                var39 = 0.16163698
                        else:
                            if input[10] < 2.0151885:
                                var39 = -0.14105473
                            else:
                                var39 = 0.13673247
            else:
                var39 = 0.14873773
        else:
            var39 = 0.14934044
    if input[5] < -0.53826725:
        if input[5] < -0.55487835:
            var40 = 0.14912602
        else:
            if input[1] < -0.94208455:
                if input[0] < -0.029990584:
                    if input[0] < -1.476662:
                        var40 = 0.04431178
                    else:
                        if input[7] < 0.8726697:
                            var40 = -0.020060632
                        else:
                            var40 = -0.08948908
                else:
                    if input[6] < -0.055939615:
                        if input[6] < -0.9865836:
                            var40 = -0.0066967304
                        else:
                            if input[0] < 0.53260386:
                                var40 = 0.23718503
                            else:
                                var40 = 0.061936397
                    else:
                        var40 = -0.057091214
            else:
                if input[2] < -1.4916315:
                    var40 = -0.014316021
                else:
                    if input[1] < 0.6226151:
                        if input[0] < -0.19073185:
                            if input[4] < -1.0856943:
                                var40 = -0.04090916
                            else:
                                var40 = 0.2069201
                        else:
                            if input[6] < -0.8702531:
                                var40 = 0.1421851
                            else:
                                var40 = 0.006255602
                    else:
                        if input[0] < -0.11036122:
                            if input[1] < 1.375989:
                                var40 = -0.09286094
                            else:
                                var40 = 0.09913152
                        else:
                            if input[2] < 0.022420364:
                                var40 = 0.18624763
                            else:
                                var40 = 0.03604159
    else:
        if input[4] < 0.97290224:
            if input[10] < 2.0151885:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[9] < 1.3985938:
                                var40 = 0.036656488
                            else:
                                var40 = -0.09398078
                        else:
                            var40 = 0.21058555
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var40 = -0.073257156
                            else:
                                var40 = 0.16259518
                        else:
                            if input[3] < -0.5225813:
                                var40 = -0.13975197
                            else:
                                var40 = -0.034468483
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[1] < -1.4636511:
                                var40 = 0.05176857
                            else:
                                var40 = -0.07666882
                        else:
                            var40 = 0.16203518
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var40 = 0.14669853
                            else:
                                var40 = -0.12367471
                        else:
                            if input[3] < -0.19687115:
                                var40 = -0.12846671
                            else:
                                var40 = -0.03053575
            else:
                var40 = 0.14861563
        else:
            var40 = 0.1489761
    if input[5] < -0.55487835:
        var41 = 0.14891982
    else:
        if input[0] < 0.93445706:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var41 = 0.07809866
                            else:
                                var41 = -0.041024566
                        else:
                            var41 = 0.17721266
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var41 = 0.137002
                            else:
                                var41 = -0.1260514
                        else:
                            if input[2] < -0.67637277:
                                var41 = -0.01435607
                            else:
                                var41 = -0.09355827
                else:
                    if input[3] < 0.45454916:
                        var41 = 0.18266785
                    else:
                        var41 = 0.14631927
            else:
                if input[1] < -1.4636511:
                    if input[9] < 1.3985938:
                        if input[8] < 1.4017887:
                            if input[2] < -0.90930384:
                                var41 = 1.9832317
                            else:
                                var41 = 0.43800807
                        else:
                            if input[5] < -0.53826725:
                                var41 = 0.059389744
                            else:
                                var41 = -0.12569797
                    else:
                        if input[3] < 0.45454916:
                            if input[6] < 0.17672138:
                                var41 = -0.14505973
                            else:
                                var41 = -0.09867107
                        else:
                            var41 = 0.034692332
                else:
                    if input[10] < 2.0151885:
                        if input[4] < 0.97290224:
                            if input[6] < 0.17672138:
                                var41 = -0.107823424
                            else:
                                var41 = -0.034415368
                        else:
                            var41 = 0.14289929
                    else:
                        var41 = 0.14434771
        else:
            var41 = 0.14876015
    if input[5] < -0.53826725:
        if input[5] < -0.55487835:
            var42 = 0.14869061
        else:
            if input[6] < -1.4519056:
                var42 = -0.057039183
            else:
                if input[6] < -0.28860062:
                    if input[1] < -0.1307588:
                        if input[1] < -0.420518:
                            if input[9] < 1.3985938:
                                var42 = 0.017026234
                            else:
                                var42 = 0.16481858
                        else:
                            var42 = -0.079188645
                    else:
                        if input[1] < 0.15900038:
                            var42 = 0.24560484
                        else:
                            if input[1] < 0.39080775:
                                var42 = -0.03166054
                            else:
                                var42 = 0.1244729
                else:
                    if input[2] < 0.48828247:
                        if input[2] < -0.09404516:
                            if input[3] < 0.12883902:
                                var42 = 0.022568932
                            else:
                                var42 = 0.10740494
                        else:
                            if input[7] < 0.8726697:
                                var42 = 0.008678531
                            else:
                                var42 = -0.09916329
                    else:
                        if input[3] < -0.84829146:
                            var42 = -0.078568555
                        else:
                            if input[1] < 0.7385188:
                                var42 = 0.17705813
                            else:
                                var42 = -0.016894618
    else:
        if input[0] < 0.93445706:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var42 = 0.06358951
                            else:
                                var42 = -0.037662916
                        else:
                            var42 = 0.17263077
                    else:
                        if input[6] < 0.17672138:
                            if input[1] < -0.36256617:
                                var42 = -0.035140887
                            else:
                                var42 = -0.13090043
                        else:
                            if input[7] < 0.8726697:
                                var42 = 0.15777393
                            else:
                                var42 = -0.07850285
                else:
                    var42 = 0.17175788
            else:
                if input[1] < -0.36256617:
                    if input[2] < -0.67637277:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var42 = 0.0401565
                            else:
                                var42 = -0.10325614
                        else:
                            var42 = 0.19511726
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var42 = 0.088751905
                            else:
                                var42 = -0.1185255
                        else:
                            if input[7] < 0.8726697:
                                var42 = -0.037275564
                            else:
                                var42 = -0.12953767
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[4] < 0.97290224:
                                var42 = -0.13063103
                            else:
                                var42 = 0.120919846
                        else:
                            var42 = 0.15774576
                    else:
                        if input[10] < 2.0151885:
                            if input[4] < 0.97290224:
                                var42 = -0.14237419
                            else:
                                var42 = 0.1283809
                        else:
                            var42 = 0.1318805
        else:
            var42 = 0.14836188
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[0] < 0.93445706:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[8] < 1.4017887:
                                var43 = 0.03247576
                            else:
                                var43 = -0.089265995
                        else:
                            var43 = 0.20126633
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var43 = -0.06952679
                            else:
                                var43 = 0.1598174
                        else:
                            if input[3] < -0.5225813:
                                var43 = -0.13656747
                            else:
                                var43 = -0.032344617
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[3] < -0.5225813:
                                var43 = -0.1088999
                            else:
                                var43 = -0.021755513
                        else:
                            var43 = 0.16027348
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var43 = 0.11730594
                            else:
                                var43 = -0.12674934
                        else:
                            if input[3] < -0.19687115:
                                var43 = -0.120259374
                            else:
                                var43 = -0.030728424
            else:
                var43 = 0.14764415
        else:
            var43 = 0.14846042
    else:
        var43 = 0.14886466
    if input[5] < -0.53826725:
        if input[5] < -0.55487835:
            var44 = 0.14827646
        else:
            if input[1] < -1.1159401:
                if input[2] < -0.79283834:
                    if input[0] < -0.11036122:
                        var44 = -0.024505788
                    else:
                        var44 = 0.14752789
                else:
                    if input[4] < 0.48852658:
                        if input[1] < -1.2897956:
                            var44 = -0.09074149
                        else:
                            var44 = 0.029392531
                    else:
                        var44 = 0.044160753
            else:
                if input[6] < -1.4519056:
                    var44 = -0.04002345
                else:
                    if input[1] < 1.5498445:
                        if input[6] < -0.28860062:
                            if input[7] < 0.8726697:
                                var44 = 0.061075855
                            else:
                                var44 = 0.16814835
                        else:
                            if input[6] < -0.055939615:
                                var44 = -0.050732512
                            else:
                                var44 = 0.07581002
                    else:
                        var44 = -0.0130647365
    else:
        if input[10] < 2.0151885:
            if input[4] < 0.97290224:
                if input[0] < 0.05038005:
                    if input[3] < 0.12883902:
                        if input[0] < -0.7533263:
                            if input[3] < -0.19687115:
                                var44 = -0.01784305
                            else:
                                var44 = 0.1696417
                        else:
                            if input[1] < -1.4636511:
                                var44 = 0.031154972
                            else:
                                var44 = -0.07597354
                    else:
                        var44 = 0.17149311
                else:
                    if input[0] < 0.93445706:
                        if input[1] < -0.36256617:
                            if input[2] < -0.67637277:
                                var44 = 0.044034034
                            else:
                                var44 = -0.064103365
                        else:
                            if input[7] < 0.8726697:
                                var44 = -0.043507643
                            else:
                                var44 = -0.13875721
                    else:
                        var44 = 0.14630489
            else:
                var44 = 0.14736582
        else:
            var44 = 0.14790325
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[3] < 0.45454916:
        if input[10] < 2.0151885:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[4] < 0.8518083:
                                var46 = -0.12627861
                            else:
                                var46 = 0.036651146
                        else:
                            if input[3] < -0.19687115:
                                var46 = 0.43003565
                            else:
                                var46 = 0.11356819
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var46 = 0.14272901
                            else:
                                var46 = -0.12021854
                        else:
                            if input[3] < -0.19687115:
                                var46 = -0.09278354
                            else:
                                var46 = -0.012663986
                else:
                    var46 = 0.16001093
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var46 = 0.03731183
                            else:
                                var46 = -0.10059126
                        else:
                            var46 = 0.19416936
                    else:
                        if input[3] < -0.5225813:
                            if input[4] < 0.97290224:
                                var46 = -0.124974646
                            else:
                                var46 = 0.100872084
                        else:
                            if input[0] < -1.5570326:
                                var46 = 0.18525171
                            else:
                                var46 = -0.04743943
                else:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var46 = 0.36240092
                            else:
                                var46 = -0.12045284
                        else:
                            if input[0] < -1.5570326:
                                var46 = -0.03588518
                            else:
                                var46 = -0.12942953
                    else:
                        if input[3] < -0.5225813:
                            if input[5] < -0.53826725:
                                var46 = 0.09576002
                            else:
                                var46 = -0.13403536
                        else:
                            if input[0] < 0.05038005:
                                var46 = 0.0101004895
                            else:
                                var46 = -0.11724686
        else:
            var46 = 0.14703833
    else:
        if input[3] < 0.7802593:
            if input[0] < 0.8540864:
                var46 = 0.13816206
            else:
                if input[2] < -1.0257694:
                    if input[1] < -1.0579883:
                        var46 = 0.003079469
                    else:
                        if input[1] < -0.18871064:
                            var46 = 0.21035047
                        else:
                            if input[8] < 1.4017887:
                                var46 = 0.0009777594
                            else:
                                var46 = 0.09497086
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[5] < -0.46061033:
                                var46 = 0.03811775
                            else:
                                var46 = -0.073777035
                        else:
                            var46 = 0.16962063
                    else:
                        if input[5] < -0.5270547:
                            var46 = 0.096873306
                        else:
                            if input[4] < 0.8518083:
                                var46 = -0.100049764
                            else:
                                var46 = 0.045414925
        else:
            var46 = 0.14811558
    if input[4] < 0.97290224:
        if input[0] < 0.93445706:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var47 = 0.06504323
                            else:
                                var47 = -0.033298384
                        else:
                            var47 = 0.16623813
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var47 = 0.05611645
                            else:
                                var47 = -0.08274616
                        else:
                            if input[1] < -1.4636511:
                                var47 = 0.017616507
                            else:
                                var47 = -0.09072615
                else:
                    var47 = 0.16618052
            else:
                if input[5] < -0.5270547:
                    if input[5] < -0.55487835:
                        var47 = 0.13957621
                    else:
                        if input[6] < -0.8702531:
                            if input[2] < -0.44344172:
                                var47 = 0.008572559
                            else:
                                var47 = 0.17272815
                        else:
                            if input[0] < 0.8540864:
                                var47 = -0.0017270998
                            else:
                                var47 = 0.10644441
                else:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var47 = -0.040859893
                            else:
                                var47 = 0.17771867
                        else:
                            if input[1] < -1.4636511:
                                var47 = 0.008360293
                            else:
                                var47 = -0.090949975
                    else:
                        if input[3] < 0.45454916:
                            if input[6] < 0.17672138:
                                var47 = -0.14284773
                            else:
                                var47 = -0.052365597
                        else:
                            if input[0] < 0.8540864:
                                var47 = 0.13611984
                            else:
                                var47 = -0.011713949
        else:
            var47 = 0.147301
    else:
        var47 = 0.1481012
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[1] < -1.4636511:
                                var48 = -0.006171884
                            else:
                                var48 = -0.12935993
                        else:
                            if input[3] < -0.19687115:
                                var48 = 0.32318008
                            else:
                                var48 = 0.10775606
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var48 = 0.1409875
                            else:
                                var48 = -0.12992638
                        else:
                            if input[3] < -0.19687115:
                                var48 = -0.09141093
                            else:
                                var48 = -0.009055984
                else:
                    var48 = 0.15966961
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[9] < 1.3985938:
                                var48 = 0.02179414
                            else:
                                var48 = -0.1174526
                        else:
                            var48 = 0.18855166
                    else:
                        if input[3] < -0.5225813:
                            if input[5] < -0.53826725:
                                var48 = 0.054429702
                            else:
                                var48 = -0.13674468
                        else:
                            if input[0] < -1.5570326:
                                var48 = 0.17166798
                            else:
                                var48 = -0.041184604
                else:
                    if input[3] < 0.12883902:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var48 = 0.094689295
                            else:
                                var48 = -0.12882884
                        else:
                            if input[5] < -0.53826725:
                                var48 = 0.0831582
                            else:
                                var48 = -0.099301666
                    else:
                        if input[0] < 0.05038005:
                            var48 = 0.16381846
                        else:
                            if input[3] < 0.7802593:
                                var48 = -0.1077987
                            else:
                                var48 = 0.13270903
        else:
            var48 = 0.14708148
    else:
        var48 = 0.147789
    if input[0] < 0.93445706:
        if input[10] < 2.0151885:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var49 = 0.05540945
                            else:
                                var49 = -0.029366938
                        else:
                            var49 = 0.16402394
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var49 = 0.045765433
                            else:
                                var49 = -0.07525255
                        else:
                            if input[1] < -1.4636511:
                                var49 = 0.009498001
                            else:
                                var49 = -0.08606675
                else:
                    var49 = 0.16257244
            else:
                if input[5] < -0.5270547:
                    if input[5] < -0.55487835:
                        var49 = 0.1376916
                    else:
                        if input[6] < 0.40938237:
                            if input[1] < 1.2600853:
                                var49 = 0.09455671
                            else:
                                var49 = -0.0598413
                        else:
                            if input[4] < -1.0856943:
                                var49 = 0.0602135
                            else:
                                var49 = -0.055051018
                else:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var49 = 0.3834097
                            else:
                                var49 = -0.1252406
                        else:
                            if input[3] < 0.45454916:
                                var49 = -0.13321976
                            else:
                                var49 = -0.002615385
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var49 = -0.10002233
                            else:
                                var49 = 0.15616271
                        else:
                            if input[3] < 0.7802593:
                                var49 = -0.108170606
                            else:
                                var49 = 0.12819536
        else:
            var49 = 0.14671096
    else:
        var49 = 0.14744464
    if input[4] < 0.97290224:
        if input[0] < 0.93445706:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[3] < 0.12883902:
                        if input[0] < -0.8336969:
                            if input[3] < -0.5225813:
                                var50 = -0.06988415
                            else:
                                var50 = 0.08462403
                        else:
                            if input[1] < -0.36256617:
                                var50 = -0.029499976
                            else:
                                var50 = -0.124140695
                    else:
                        if input[0] < 0.05038005:
                            var50 = 0.15790142
                        else:
                            if input[3] < 0.7802593:
                                var50 = -0.071954526
                            else:
                                var50 = 0.12358419
                else:
                    var50 = 0.15796682
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[8] < 1.4017887:
                                var50 = 0.028561937
                            else:
                                var50 = -0.12004805
                        else:
                            var50 = 0.18302687
                    else:
                        if input[5] < -0.53826725:
                            if input[8] < 1.4017887:
                                var50 = 0.1437802
                            else:
                                var50 = 0.006199603
                        else:
                            if input[3] < -0.5225813:
                                var50 = -0.13922556
                            else:
                                var50 = -0.034543183
                else:
                    if input[5] < -0.53826725:
                        if input[5] < -0.55487835:
                            var50 = 0.13658854
                        else:
                            if input[2] < 0.48828247:
                                var50 = -0.039423037
                            else:
                                var50 = 0.09116419
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var50 = 0.09051898
                            else:
                                var50 = -0.12672445
                        else:
                            if input[3] < -0.5225813:
                                var50 = -0.13971974
                            else:
                                var50 = -0.04065124
        else:
            var50 = 0.1462356
    else:
        var50 = 0.14713387
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[2] < -0.67637277:
                if input[1] < -0.36256617:
                    if input[1] < -1.1159401:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var51 = 0.20400652
                            else:
                                var51 = -0.09050362
                        else:
                            if input[5] < -0.53826725:
                                var51 = 0.08532603
                            else:
                                var51 = -0.10035546
                    else:
                        var51 = 0.18368995
                else:
                    if input[3] < -0.5225813:
                        if input[6] < 0.17672138:
                            if input[0] < 0.93445706:
                                var51 = -0.13478667
                            else:
                                var51 = 0.08285381
                        else:
                            if input[7] < 0.8726697:
                                var51 = 0.14837496
                            else:
                                var51 = -0.115382046
                    else:
                        if input[0] < -1.5570326:
                            var51 = 0.21494663
                        else:
                            if input[5] < -0.53826725:
                                var51 = 0.11170566
                            else:
                                var51 = -0.026196035
            else:
                if input[0] < 0.93445706:
                    if input[0] < 0.05038005:
                        if input[3] < 0.12883902:
                            if input[0] < -1.5570326:
                                var51 = 0.057207216
                            else:
                                var51 = -0.04074746
                        else:
                            var51 = 0.16005468
                    else:
                        if input[5] < -0.5270547:
                            if input[5] < -0.55487835:
                                var51 = 0.12585923
                            else:
                                var51 = 0.034552477
                        else:
                            if input[1] < -1.4636511:
                                var51 = -0.004862613
                            else:
                                var51 = -0.09570289
                else:
                    var51 = 0.14279158
        else:
            var51 = 0.14582217
    else:
        var51 = 0.14672902
    if input[5] < -0.55487835:
        var52 = 0.14613871
    else:
        if input[10] < 2.0151885:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var52 = 0.4584145
                            else:
                                var52 = -0.12282601
                        else:
                            if input[5] < -0.5270547:
                                var52 = 0.0507498
                            else:
                                var52 = -0.12589237
                    else:
                        if input[3] < -0.5225813:
                            if input[2] < -0.67637277:
                                var52 = -0.013188903
                            else:
                                var52 = -0.1272226
                        else:
                            if input[0] < -1.5570326:
                                var52 = 0.24319658
                            else:
                                var52 = -0.033617906
                else:
                    var52 = 0.15698956
            else:
                if input[1] < -1.4636511:
                    if input[9] < 1.3985938:
                        if input[8] < 1.4017887:
                            if input[2] < -0.67637277:
                                var52 = 0.9494424
                            else:
                                var52 = 0.2747988
                        else:
                            if input[3] < 0.12883902:
                                var52 = -0.13683815
                            else:
                                var52 = -0.04711594
                    else:
                        if input[0] < -0.9944382:
                            if input[3] < -0.19687115:
                                var52 = -0.108784385
                            else:
                                var52 = 0.08884406
                        else:
                            if input[3] < 0.12883902:
                                var52 = -0.14337425
                            else:
                                var52 = -0.08118678
                else:
                    if input[3] < 0.12883902:
                        if input[0] < -0.7533263:
                            if input[3] < -0.19687115:
                                var52 = -0.053189795
                            else:
                                var52 = 0.1603452
                        else:
                            if input[0] < 0.93445706:
                                var52 = -0.095860936
                            else:
                                var52 = 0.13566227
                    else:
                        if input[0] < 0.05038005:
                            var52 = 0.15933031
                        else:
                            if input[3] < 0.7802593:
                                var52 = -0.09034857
                            else:
                                var52 = 0.13169476
        else:
            var52 = 0.14495462
    if input[5] < -0.53826725:
        if input[5] < -0.55487835:
            var53 = 0.14552072
        else:
            if input[6] < 0.40938237:
                if input[1] < 1.5498445:
                    if input[2] < 0.022420364:
                        if input[0] < 0.3718626:
                            if input[8] < 1.4017887:
                                var53 = 0.2433983
                            else:
                                var53 = -0.027133899
                        else:
                            if input[3] < -0.19687115:
                                var53 = 0.08940556
                            else:
                                var53 = -0.073219895
                    else:
                        if input[0] < 0.45223323:
                            if input[0] < -0.35147312:
                                var53 = 0.0662653
                            else:
                                var53 = -0.055697124
                        else:
                            if input[7] < 0.8726697:
                                var53 = 0.016527263
                            else:
                                var53 = 0.17476839
                else:
                    var53 = -0.068541594
            else:
                if input[9] < 1.3985938:
                    if input[0] < -1.23555:
                        var53 = 0.10080315
                    else:
                        if input[0] < 0.7737158:
                            var53 = -0.10192236
                        else:
                            var53 = 0.03153054
                else:
                    if input[2] < 0.7212135:
                        if input[1] < 0.21695223:
                            if input[1] < -0.8261809:
                                var53 = -0.06135633
                            else:
                                var53 = 0.080224425
                        else:
                            var53 = -0.077415526
                    else:
                        var53 = 0.26476684
    else:
        if input[4] < 0.97290224:
            if input[2] < -0.67637277:
                if input[1] < -0.36256617:
                    if input[1] < -1.1159401:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var53 = 0.14747459
                            else:
                                var53 = -0.10903799
                        else:
                            if input[6] < 0.17672138:
                                var53 = -0.1117783
                            else:
                                var53 = -0.03257644
                    else:
                        var53 = 0.17942302
                else:
                    if input[3] < 0.12883902:
                        if input[0] < -0.7533263:
                            if input[3] < -0.19687115:
                                var53 = -0.04280667
                            else:
                                var53 = 0.15493006
                        else:
                            if input[0] < 0.93445706:
                                var53 = -0.09524842
                            else:
                                var53 = 0.11331713
                    else:
                        if input[0] < 0.05038005:
                            var53 = 0.15036222
                        else:
                            if input[3] < 0.45454916:
                                var53 = -0.099048145
                            else:
                                var53 = 0.089219116
            else:
                if input[7] < 0.8726697:
                    if input[6] < 0.17672138:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var53 = 0.112095274
                            else:
                                var53 = -0.11256737
                        else:
                            if input[3] < -0.5225813:
                                var53 = -0.13366586
                            else:
                                var53 = -0.030298209
                    else:
                        var53 = 0.15426885
                else:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[1] < -1.4636511:
                                var53 = 0.01709711
                            else:
                                var53 = -0.1397805
                        else:
                            var53 = 0.2023485
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var53 = 0.076017454
                            else:
                                var53 = -0.12420207
                        else:
                            if input[3] < -0.19687115:
                                var53 = -0.12981379
                            else:
                                var53 = -0.02691971
        else:
            var53 = 0.14473213
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var54 = -0.068674445
                            else:
                                var54 = 0.21446794
                        else:
                            if input[1] < -0.36256617:
                                var54 = 0.018165067
                            else:
                                var54 = -0.06944773
                    else:
                        var54 = 0.16076596
                else:
                    if input[3] < -0.19687115:
                        if input[8] < 1.4017887:
                            if input[1] < -1.4636511:
                                var54 = 0.15388319
                            else:
                                var54 = -0.019471481
                        else:
                            if input[1] < -1.1159401:
                                var54 = -0.12511493
                            else:
                                var54 = -0.01597057
                    else:
                        if input[6] < 0.17672138:
                            if input[5] < -0.5270547:
                                var54 = 0.04597784
                            else:
                                var54 = -0.10595056
                        else:
                            if input[7] < 0.8726697:
                                var54 = 0.14309528
                            else:
                                var54 = -0.100642465
            else:
                var54 = 0.15762518
        else:
            if input[3] < 0.45454916:
                if input[5] < -0.53826725:
                    if input[4] < 0.7307144:
                        if input[4] < -0.48022476:
                            if input[8] < 1.4017887:
                                var54 = 0.02549504
                            else:
                                var54 = 0.15015858
                        else:
                            if input[3] < 0.12883902:
                                var54 = 0.035066333
                            else:
                                var54 = -0.083480194
                    else:
                        if input[1] < -0.014855128:
                            var54 = 0.049952958
                        else:
                            var54 = 0.18588036
                else:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var54 = -0.04462227
                            else:
                                var54 = 0.15944186
                        else:
                            if input[1] < -1.4636511:
                                var54 = -0.015200433
                            else:
                                var54 = -0.09323964
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var54 = -0.13011394
                            else:
                                var54 = 0.1445702
                        else:
                            if input[10] < 2.0151885:
                                var54 = -0.14118056
                            else:
                                var54 = 0.09996095
            else:
                if input[0] < 0.8540864:
                    var54 = 0.1413396
                else:
                    if input[2] < -1.3751659:
                        var54 = 0.1663337
                    else:
                        if input[1] < -0.30461434:
                            if input[5] < 0.8885023:
                                var54 = 0.064300574
                            else:
                                var54 = -0.03634182
                        else:
                            if input[7] < 0.8726697:
                                var54 = 0.0119321225
                            else:
                                var54 = -0.069189265
    else:
        var54 = 0.14549716
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var55 = 0.3576339
                            else:
                                var55 = -0.11344811
                        else:
                            if input[3] < 0.12883902:
                                var55 = -0.1287056
                            else:
                                var55 = -0.037701074
                    else:
                        if input[3] < -0.5225813:
                            if input[2] < -0.67637277:
                                var55 = -0.01466643
                            else:
                                var55 = -0.12155948
                        else:
                            if input[0] < -1.5570326:
                                var55 = 0.20863137
                            else:
                                var55 = -0.031675134
                else:
                    var55 = 0.15533938
            else:
                if input[5] < -0.53826725:
                    if input[4] < -0.60131866:
                        if input[5] < -0.55487835:
                            var55 = 0.11406832
                        else:
                            if input[0] < 0.8540864:
                                var55 = -0.055386405
                            else:
                                var55 = 0.11703765
                    else:
                        if input[6] < 1.4563569:
                            if input[2] < 0.48828247:
                                var55 = 0.07046741
                            else:
                                var55 = 0.1712304
                        else:
                            if input[2] < -0.79283834:
                                var55 = 0.027649505
                            else:
                                var55 = -0.05835616
                else:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var55 = 0.34365296
                            else:
                                var55 = -0.12579043
                        else:
                            if input[3] < 0.12883902:
                                var55 = -0.13850996
                            else:
                                var55 = -0.060600195
                    else:
                        if input[3] < 0.12883902:
                            if input[0] < -0.7533263:
                                var55 = -0.016361484
                            else:
                                var55 = -0.09859079
                        else:
                            if input[0] < 0.05038005:
                                var55 = 0.15505126
                            else:
                                var55 = -0.07283713
        else:
            var55 = 0.1442532
    else:
        var55 = 0.1452727
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var56 = 0.060506828
                            else:
                                var56 = -0.07182113
                        else:
                            var56 = 0.17660797
                    else:
                        if input[0] < -1.476662:
                            if input[3] < -0.5225813:
                                var56 = -0.06020633
                            else:
                                var56 = 0.14323962
                        else:
                            if input[6] < 0.17672138:
                                var56 = -0.06835551
                            else:
                                var56 = 0.0033353574
                else:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var56 = 0.04268844
                            else:
                                var56 = -0.05283778
                        else:
                            var56 = 0.15719557
                    else:
                        if input[5] < -0.5175034:
                            if input[2] < 0.7212135:
                                var56 = 0.006028566
                            else:
                                var56 = 0.11747862
                        else:
                            if input[1] < -1.4636511:
                                var56 = -0.0066737095
                            else:
                                var56 = -0.08588008
            else:
                var56 = 0.15536022
        else:
            if input[3] < 0.45454916:
                if input[5] < -0.53826725:
                    if input[8] < 1.4017887:
                        if input[0] < 0.6129745:
                            if input[0] < 0.13075069:
                                var56 = -0.061055563
                            else:
                                var56 = 0.08884279
                        else:
                            if input[4] < -0.7224126:
                                var56 = 0.025061995
                            else:
                                var56 = -0.080360666
                    else:
                        if input[3] < 0.12883902:
                            if input[6] < 0.40938237:
                                var56 = 0.175941
                            else:
                                var56 = -0.02554058
                        else:
                            if input[4] < -0.7224126:
                                var56 = 0.07708703
                            else:
                                var56 = -0.06757544
                else:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var56 = -0.044041306
                            else:
                                var56 = 0.15744898
                        else:
                            if input[1] < -1.4636511:
                                var56 = -0.023397833
                            else:
                                var56 = -0.08791904
                    else:
                        if input[10] < 2.0151885:
                            if input[4] < 0.97290224:
                                var56 = -0.10931375
                            else:
                                var56 = 0.1096889
                        else:
                            var56 = 0.11222091
            else:
                if input[0] < 0.8540864:
                    var56 = 0.1400785
                else:
                    if input[2] < -1.0257694:
                        if input[6] < -0.28860062:
                            var56 = 0.16381375
                        else:
                            var56 = 0.018287776
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var56 = -0.06451502
                            else:
                                var56 = 0.12742025
                        else:
                            if input[5] < -0.5175034:
                                var56 = 0.03788507
                            else:
                                var56 = -0.07185877
    else:
        var56 = 0.14479503
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[5] < -0.53826725:
                        if input[4] < -0.7224126:
                            if input[9] < 1.3985938:
                                var57 = 0.22564663
                            else:
                                var57 = -0.045770325
                        else:
                            if input[5] < -0.55487835:
                                var57 = 0.11765226
                            else:
                                var57 = -0.014595837
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var57 = 0.04246321
                            else:
                                var57 = -0.05854216
                        else:
                            if input[1] < -1.4636511:
                                var57 = 0.018226597
                            else:
                                var57 = -0.06645972
                else:
                    var57 = 0.15440579
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var57 = 0.038204618
                            else:
                                var57 = -0.09637076
                        else:
                            var57 = 0.16906828
                    else:
                        if input[5] < -0.53826725:
                            if input[3] < -0.19687115:
                                var57 = 0.13616873
                            else:
                                var57 = -0.023185018
                        else:
                            if input[3] < -0.19687115:
                                var57 = -0.102388665
                            else:
                                var57 = -0.012434851
                else:
                    if input[0] < 0.93445706:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var57 = -0.09625035
                            else:
                                var57 = 0.18201555
                        else:
                            if input[1] < -1.4636511:
                                var57 = -0.0015745829
                            else:
                                var57 = -0.074252106
                    else:
                        var57 = 0.13303342
        else:
            var57 = 0.14318645
    else:
        var57 = 0.14433406
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var58 = 0.15137303
                            else:
                                var58 = -0.10531357
                        else:
                            if input[0] < -1.5570326:
                                var58 = 0.04100007
                            else:
                                var58 = -0.041505665
                    else:
                        var58 = 0.15871681
                else:
                    if input[8] < 1.4017887:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var58 = 0.34770545
                            else:
                                var58 = -0.1354089
                        else:
                            if input[5] < -0.53826725:
                                var58 = 0.11021211
                            else:
                                var58 = -0.05025252
                    else:
                        if input[1] < -1.1159401:
                            if input[5] < -0.5175034:
                                var58 = -0.03678167
                            else:
                                var58 = -0.12896849
                        else:
                            if input[2] < -0.67637277:
                                var58 = 0.014835668
                            else:
                                var58 = -0.065996334
            else:
                var58 = 0.15452024
        else:
            if input[3] < 0.45454916:
                if input[5] < -0.50504506:
                    if input[5] < -0.55487835:
                        var58 = 0.11580817
                    else:
                        if input[4] < 0.7307144:
                            if input[4] < -0.48022476:
                                var58 = 0.034455467
                            else:
                                var58 = -0.021118235
                        else:
                            if input[1] < -0.014855128:
                                var58 = 0.0043781404
                            else:
                                var58 = 0.14932936
                else:
                    if input[1] < -0.36256617:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var58 = 0.061676227
                            else:
                                var58 = -0.07278695
                        else:
                            if input[1] < -1.1738919:
                                var58 = -0.12107628
                            else:
                                var58 = -0.011379033
                    else:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var58 = -0.12735525
                            else:
                                var58 = 0.14060515
                        else:
                            if input[4] < 0.97290224:
                                var58 = -0.1394736
                            else:
                                var58 = 0.08421581
            else:
                if input[0] < 0.8540864:
                    var58 = 0.13877438
                else:
                    if input[2] < -1.3751659:
                        var58 = 0.1524149
                    else:
                        if input[3] < 0.7802593:
                            if input[1] < -0.36256617:
                                var58 = 0.022852195
                            else:
                                var58 = -0.048583556
                        else:
                            var58 = 0.07977599
    else:
        var58 = 0.14355426
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[2] < -0.67637277:
                if input[1] < -0.36256617:
                    if input[1] < -1.1159401:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var59 = 0.12729615
                            else:
                                var59 = -0.11307502
                        else:
                            if input[6] < 0.17672138:
                                var59 = -0.10196421
                            else:
                                var59 = -0.021709664
                    else:
                        var59 = 0.17065032
                else:
                    if input[3] < -0.5225813:
                        if input[6] < 0.17672138:
                            if input[5] < -0.53826725:
                                var59 = -0.007361223
                            else:
                                var59 = -0.13411094
                        else:
                            if input[7] < 0.8726697:
                                var59 = 0.1404983
                            else:
                                var59 = -0.102838255
                    else:
                        if input[0] < -1.5570326:
                            var59 = 0.1727009
                        else:
                            if input[5] < -0.53826725:
                                var59 = 0.06775478
                            else:
                                var59 = -0.02347943
            else:
                if input[7] < 0.8726697:
                    if input[6] < 0.17672138:
                        if input[5] < -0.53826725:
                            if input[2] < 0.25535142:
                                var59 = 0.13673413
                            else:
                                var59 = 0.017484436
                        else:
                            if input[1] < -1.4636511:
                                var59 = 0.011959906
                            else:
                                var59 = -0.06271478
                    else:
                        var59 = 0.15166074
                else:
                    if input[5] < -0.53826725:
                        if input[1] < -1.3477474:
                            var59 = -0.066038415
                        else:
                            if input[2] < 0.48828247:
                                var59 = 0.018446254
                            else:
                                var59 = 0.089179195
                    else:
                        if input[3] < -0.5225813:
                            if input[1] < -1.4636511:
                                var59 = 0.0095304735
                            else:
                                var59 = -0.1396444
                        else:
                            if input[0] < -1.5570326:
                                var59 = 0.17290321
                            else:
                                var59 = -0.045932822
        else:
            var59 = 0.14201955
    else:
        var59 = 0.14337093
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var60 = -0.06960826
                            else:
                                var60 = 0.18795198
                        else:
                            if input[1] < -0.36256617:
                                var60 = 0.01203726
                            else:
                                var60 = -0.062091064
                    else:
                        var60 = 0.15728669
                else:
                    if input[3] < -0.19687115:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var60 = 0.07813287
                            else:
                                var60 = -0.04369208
                        else:
                            if input[1] < -1.1159401:
                                var60 = -0.11469679
                            else:
                                var60 = -0.011802325
                    else:
                        if input[6] < 0.17672138:
                            if input[5] < -0.5270547:
                                var60 = 0.017807039
                            else:
                                var60 = -0.09862863
                        else:
                            if input[7] < 0.8726697:
                                var60 = 0.13542436
                            else:
                                var60 = -0.09000005
            else:
                var60 = 0.15359747
        else:
            if input[3] < 0.45454916:
                if input[10] < 2.0151885:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var60 = -0.03635665
                            else:
                                var60 = 0.15095553
                        else:
                            if input[9] < 1.3985938:
                                var60 = -0.03087535
                            else:
                                var60 = -0.09620161
                    else:
                        if input[5] < -0.53826725:
                            if input[4] < -0.7224126:
                                var60 = 0.076551154
                            else:
                                var60 = -0.012377507
                        else:
                            if input[7] < 0.8726697:
                                var60 = -0.053245757
                            else:
                                var60 = -0.13862357
                else:
                    var60 = 0.12222586
            else:
                if input[0] < 0.8540864:
                    var60 = 0.13728793
                else:
                    if input[2] < -1.0257694:
                        if input[6] < -0.28860062:
                            var60 = 0.13994527
                        else:
                            var60 = 0.015487414
                    else:
                        if input[5] < -0.50504506:
                            var60 = 0.04719084
                        else:
                            if input[6] < 0.17672138:
                                var60 = -0.0641935
                            else:
                                var60 = 0.012631124
    else:
        var60 = 0.14264023
    if input[4] < 0.97290224:
        if input[10] < 2.0151885:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var61 = 0.28953847
                            else:
                                var61 = -0.10744825
                        else:
                            if input[3] < -0.5225813:
                                var61 = -0.07283816
                            else:
                                var61 = -0.00963296
                    else:
                        if input[1] < -1.2318437:
                            if input[3] < -0.19687115:
                                var61 = -0.13943236
                            else:
                                var61 = -0.06730297
                        else:
                            if input[2] < -0.44344172:
                                var61 = 0.016987033
                            else:
                                var61 = -0.051917803
                else:
                    var61 = 0.15326446
            else:
                if input[2] < -0.55990726:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[9] < 1.3985938:
                                var61 = 0.025906151
                            else:
                                var61 = -0.10664994
                        else:
                            if input[2] < -0.67637277:
                                var61 = 0.16397628
                            else:
                                var61 = -0.019156542
                    else:
                        if input[5] < -0.53826725:
                            if input[3] < -0.19687115:
                                var61 = 0.11249206
                            else:
                                var61 = -0.03649847
                        else:
                            if input[3] < -0.19687115:
                                var61 = -0.0990849
                            else:
                                var61 = -0.011560882
                else:
                    if input[5] < -0.53826725:
                        if input[5] < -0.55487835:
                            var61 = 0.12055916
                        else:
                            if input[2] < 0.37181693:
                                var61 = -0.043561317
                            else:
                                var61 = 0.05119353
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var61 = 0.06231398
                            else:
                                var61 = -0.12089618
                        else:
                            if input[3] < -0.5225813:
                                var61 = -0.13756578
                            else:
                                var61 = -0.036856033
        else:
            var61 = 0.14084195
    else:
        var61 = 0.14196067
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var62 = -0.061060656
                            else:
                                var62 = 0.1814235
                        else:
                            if input[1] < -1.4636511:
                                var62 = 0.04816984
                            else:
                                var62 = -0.037198763
                    else:
                        var62 = 0.15572557
                else:
                    if input[2] < -0.55990726:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var62 = -0.020054607
                            else:
                                var62 = 0.14732273
                        else:
                            if input[5] < -0.53826725:
                                var62 = 0.089921005
                            else:
                                var62 = -0.07808635
                    else:
                        if input[10] < 2.0151885:
                            if input[6] < 0.17672138:
                                var62 = -0.08767026
                            else:
                                var62 = -0.024437962
                        else:
                            var62 = 0.11481318
            else:
                var62 = 0.1524496
        else:
            if input[3] < 0.7802593:
                if input[4] < 0.97290224:
                    if input[5] < -0.50504506:
                        if input[5] < -0.55487835:
                            var62 = 0.110726826
                        else:
                            if input[6] < -0.8702531:
                                var62 = 0.05061643
                            else:
                                var62 = -0.012498718
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var62 = 0.05375697
                            else:
                                var62 = -0.1272066
                        else:
                            if input[6] < 0.17672138:
                                var62 = -0.09740455
                            else:
                                var62 = -0.024147091
                else:
                    var62 = 0.12190197
            else:
                var62 = 0.13310179
    else:
        var62 = 0.14162928
    if input[0] < 0.93445706:
        if input[10] < 2.0151885:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var63 = 0.26591927
                            else:
                                var63 = -0.10063504
                        else:
                            if input[1] < -1.1159401:
                                var63 = -0.096801646
                            else:
                                var63 = -0.015297145
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < -0.19687115:
                                var63 = -0.13275197
                            else:
                                var63 = -0.060343675
                        else:
                            if input[1] < -0.36256617:
                                var63 = 0.0373259
                            else:
                                var63 = -0.05017088
                else:
                    var63 = 0.15248623
            else:
                if input[8] < 1.4017887:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[2] < -0.67637277:
                                var63 = 0.4022408
                            else:
                                var63 = 0.20061669
                        else:
                            if input[5] < -0.53826725:
                                var63 = -0.031686917
                            else:
                                var63 = -0.12857169
                    else:
                        if input[5] < -0.53826725:
                            if input[9] < 1.3985938:
                                var63 = -0.013931546
                            else:
                                var63 = 0.1054163
                        else:
                            if input[3] < -0.5225813:
                                var63 = -0.089781195
                            else:
                                var63 = -0.028673334
                else:
                    if input[1] < -1.3477474:
                        if input[3] < 0.12883902:
                            if input[0] < -1.5570326:
                                var63 = -0.04962219
                            else:
                                var63 = -0.13406159
                        else:
                            if input[0] < 0.05038005:
                                var63 = 0.08117655
                            else:
                                var63 = -0.10694395
                    else:
                        if input[5] < -0.53826725:
                            if input[11] < 1.2236042:
                                var63 = -0.010638366
                            else:
                                var63 = 0.11476753
                        else:
                            if input[2] < -0.67637277:
                                var63 = 0.010931482
                            else:
                                var63 = -0.06436358
        else:
            var63 = 0.13956669
    else:
        var63 = 0.14039133
    if input[4] < 0.97290224:
        if input[2] < -0.67637277:
            if input[1] < -0.36256617:
                if input[1] < -1.1159401:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var64 = 0.35068446
                            else:
                                var64 = -0.10080401
                        else:
                            if input[8] < 1.4017887:
                                var64 = -0.10486371
                            else:
                                var64 = -0.024290837
                    else:
                        if input[1] < -1.4636511:
                            if input[6] < 0.17672138:
                                var64 = -0.12719373
                            else:
                                var64 = -0.072484694
                        else:
                            if input[3] < -0.19687115:
                                var64 = -0.057457622
                            else:
                                var64 = 0.00948756
                else:
                    var64 = 0.1665751
            else:
                if input[0] < -1.476662:
                    if input[3] < -0.5225813:
                        if input[5] < -0.46061033:
                            var64 = 0.076435044
                        else:
                            if input[6] < 0.17672138:
                                var64 = -0.10879006
                            else:
                                var64 = -0.021218698
                    else:
                        if input[0] < -1.5570326:
                            var64 = 0.15208355
                        else:
                            if input[7] < 0.8726697:
                                var64 = 0.0598901
                            else:
                                var64 = -0.019945772
                else:
                    if input[3] < 0.12883902:
                        if input[7] < 0.8726697:
                            if input[6] < 0.17672138:
                                var64 = -0.081634685
                            else:
                                var64 = 0.14168942
                        else:
                            if input[5] < -0.53826725:
                                var64 = 0.045553025
                            else:
                                var64 = -0.09143379
                    else:
                        if input[0] < 0.05038005:
                            var64 = 0.13284227
                        else:
                            if input[3] < 0.45454916:
                                var64 = -0.08419939
                            else:
                                var64 = 0.063363016
        else:
            if input[10] < 2.0151885:
                if input[0] < 0.93445706:
                    if input[0] < 0.05038005:
                        if input[3] < 0.12883902:
                            if input[0] < -0.7533263:
                                var64 = 0.0030623071
                            else:
                                var64 = -0.063470654
                        else:
                            var64 = 0.14997067
                    else:
                        if input[3] < 0.7802593:
                            if input[5] < -0.5270547:
                                var64 = 0.021547474
                            else:
                                var64 = -0.075377166
                        else:
                            var64 = 0.12359185
                else:
                    var64 = 0.13258243
            else:
                var64 = 0.13449103
    else:
        var64 = 0.14038542
    if input[5] < -0.55487835:
        var65 = 0.13913073
    else:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[0] < -0.8336969:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var65 = 0.040010676
                            else:
                                var65 = -0.0491733
                        else:
                            var65 = 0.14985168
                    else:
                        if input[3] < 0.12883902:
                            if input[1] < -0.36256617:
                                var65 = -0.02959268
                            else:
                                var65 = -0.1023018
                        else:
                            if input[0] < 0.05038005:
                                var65 = 0.14285216
                            else:
                                var65 = -0.029993974
                else:
                    var65 = 0.1516636
            else:
                if input[8] < 1.4017887:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[2] < -0.67637277:
                                var65 = 0.2959781
                            else:
                                var65 = 0.1917661
                        else:
                            if input[3] < -0.19687115:
                                var65 = -0.13175765
                            else:
                                var65 = -0.077749684
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < -0.19687115:
                                var65 = -0.11901761
                            else:
                                var65 = -0.03817482
                        else:
                            if input[2] < -0.55990726:
                                var65 = 0.025895238
                            else:
                                var65 = -0.046993203
                else:
                    if input[1] < -1.4636511:
                        if input[3] < 0.12883902:
                            var65 = -0.13251172
                        else:
                            if input[0] < 0.21112132:
                                var65 = 0.02648218
                            else:
                                var65 = -0.096852526
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var65 = 0.033677943
                            else:
                                var65 = -0.06914564
                        else:
                            if input[0] < -0.7533263:
                                var65 = 0.14065456
                            else:
                                var65 = -0.031910215
        else:
            var65 = 0.137404
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var66 = -0.061665285
                            else:
                                var66 = 0.17453952
                        else:
                            if input[1] < -0.36256617:
                                var66 = 0.011389352
                            else:
                                var66 = -0.06295695
                    else:
                        var66 = 0.15397787
                else:
                    if input[3] < -0.19687115:
                        if input[8] < 1.4017887:
                            if input[1] < -1.4636511:
                                var66 = 0.08439238
                            else:
                                var66 = -0.013799959
                        else:
                            if input[1] < -1.1159401:
                                var66 = -0.105361916
                            else:
                                var66 = -0.011030634
                    else:
                        if input[5] < -0.5270547:
                            if input[2] < 0.95414454:
                                var66 = -0.03398734
                            else:
                                var66 = 0.09848534
                        else:
                            if input[1] < -0.36256617:
                                var66 = -0.05089148
                            else:
                                var66 = -0.10341501
            else:
                var66 = 0.1500234
        else:
            if input[3] < 0.45454916:
                if input[5] < -0.53826725:
                    if input[8] < 1.4017887:
                        if input[0] < 0.6129745:
                            if input[4] < -0.60131866:
                                var66 = -0.04068028
                            else:
                                var66 = 0.0740293
                        else:
                            if input[4] < -0.7224126:
                                var66 = 0.005506249
                            else:
                                var66 = -0.09156829
                    else:
                        if input[0] < 0.6933451:
                            if input[1] < -0.30461434:
                                var66 = 0.10576197
                            else:
                                var66 = -0.039169434
                        else:
                            var66 = 0.14770085
                else:
                    if input[1] < -0.36256617:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var66 = 0.040362
                            else:
                                var66 = -0.067522906
                        else:
                            if input[1] < -1.1159401:
                                var66 = -0.10620489
                            else:
                                var66 = -0.00949419
                    else:
                        if input[10] < 2.0151885:
                            if input[6] < 0.17672138:
                                var66 = -0.1354613
                            else:
                                var66 = -0.051465414
                        else:
                            var66 = 0.0912502
            else:
                if input[0] < 0.8540864:
                    var66 = 0.13400893
                else:
                    if input[2] < -1.3751659:
                        var66 = 0.14461103
                    else:
                        if input[1] < -0.36256617:
                            if input[2] < -0.79283834:
                                var66 = 0.09475197
                            else:
                                var66 = -0.006940159
                        else:
                            if input[7] < 0.8726697:
                                var66 = -0.0063186097
                            else:
                                var66 = -0.063265346
    else:
        var66 = 0.13824165
    if input[10] < 2.0151885:
        if input[2] < -0.67637277:
            if input[1] < -0.36256617:
                if input[1] < -1.1159401:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var67 = 0.28292766
                            else:
                                var67 = -0.08831213
                        else:
                            if input[8] < 1.4017887:
                                var67 = -0.099579886
                            else:
                                var67 = -0.022185434
                    else:
                        if input[1] < -1.4636511:
                            if input[6] < 0.17672138:
                                var67 = -0.122839615
                            else:
                                var67 = -0.06223176
                        else:
                            if input[6] < 0.40938237:
                                var67 = -0.0548228
                            else:
                                var67 = 0.012670897
                else:
                    var67 = 0.16432014
            else:
                if input[7] < 0.8726697:
                    if input[6] < 0.17672138:
                        if input[3] < -0.5225813:
                            if input[5] < -0.5175034:
                                var67 = -0.007993415
                            else:
                                var67 = -0.11834488
                        else:
                            if input[0] < -1.3159207:
                                var67 = 0.09462415
                            else:
                                var67 = -0.034790013
                    else:
                        var67 = 0.14095213
                else:
                    if input[5] < -0.53826725:
                        if input[3] < -0.19687115:
                            if input[3] < -0.5225813:
                                var67 = 0.0138269365
                            else:
                                var67 = 0.13675086
                        else:
                            if input[4] < 0.0041509015:
                                var67 = -0.07765408
                            else:
                                var67 = 0.016313106
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var67 = 0.027879748
                            else:
                                var67 = -0.11756731
                        else:
                            if input[0] < -0.7533263:
                                var67 = 0.12702951
                            else:
                                var67 = -0.059033584
        else:
            if input[5] < -0.53826725:
                if input[5] < -0.55487835:
                    var67 = 0.13047089
                else:
                    if input[1] < -1.3477474:
                        var67 = -0.09311594
                    else:
                        if input[6] < 1.5726874:
                            if input[0] < 0.6129745:
                                var67 = 0.070732884
                            else:
                                var67 = -0.008860976
                        else:
                            var67 = -0.066514716
            else:
                if input[4] < 0.97290224:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var67 = 0.19065826
                            else:
                                var67 = -0.1012869
                        else:
                            if input[3] < -0.19687115:
                                var67 = -0.12109523
                            else:
                                var67 = -0.06029909
                    else:
                        if input[3] < -0.5225813:
                            if input[6] < 0.17672138:
                                var67 = -0.13661756
                            else:
                                var67 = -0.02243399
                        else:
                            if input[0] < -1.5570326:
                                var67 = 0.1653687
                            else:
                                var67 = -0.03418196
                else:
                    var67 = 0.13022943
    else:
        var67 = 0.13780569
    if input[7] < 0.8726697:
        if input[6] < 0.17672138:
            if input[5] < -0.53826725:
                if input[4] < -0.7224126:
                    if input[9] < 1.3985938:
                        if input[4] < -1.2067883:
                            var68 = 0.03677153
                        else:
                            if input[11] < 1.2236042:
                                var68 = 0.071355015
                            else:
                                var68 = 0.2812357
                    else:
                        var68 = -0.050350346
                else:
                    if input[2] < 0.25535142:
                        if input[4] < 0.24633874:
                            if input[6] < -0.9865836:
                                var68 = -0.06391882
                            else:
                                var68 = 0.035835464
                        else:
                            if input[2] < -0.3269762:
                                var68 = 0.06518458
                            else:
                                var68 = 0.2309625
                    else:
                        if input[5] < -0.55487835:
                            var68 = 0.08167073
                        else:
                            var68 = -0.11181498
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var68 = 0.015847584
                            else:
                                var68 = -0.092308804
                        else:
                            var68 = 0.15850572
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var68 = 0.022049364
                            else:
                                var68 = -0.1101389
                        else:
                            if input[0] < -0.7533263:
                                var68 = 0.12209522
                            else:
                                var68 = -0.040485315
                else:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var68 = 0.1794174
                            else:
                                var68 = -0.08325017
                        else:
                            if input[0] < -1.3962914:
                                var68 = -0.029158153
                            else:
                                var68 = -0.11573114
                    else:
                        if input[3] < -0.5225813:
                            if input[0] < 0.93445706:
                                var68 = -0.1262839
                            else:
                                var68 = 0.08165021
                        else:
                            if input[0] < -1.5570326:
                                var68 = 0.15417354
                            else:
                                var68 = -0.04944523
        else:
            var68 = 0.1509847
    else:
        if input[0] < 0.93445706:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.3962914:
                                var68 = 0.011414675
                            else:
                                var68 = -0.05517319
                        else:
                            var68 = 0.14937316
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var68 = 0.06871512
                            else:
                                var68 = -0.12834856
                        else:
                            if input[5] < -0.53826725:
                                var68 = 0.053760167
                            else:
                                var68 = -0.09042728
                else:
                    var68 = 0.14646935
            else:
                if input[3] < 0.45454916:
                    if input[5] < -0.53826725:
                        if input[0] < 0.21112132:
                            var68 = -0.09931354
                        else:
                            if input[6] < 0.40938237:
                                var68 = 0.08199942
                            else:
                                var68 = -0.0351102
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var68 = 0.032122158
                            else:
                                var68 = -0.12896252
                        else:
                            if input[4] < 0.97290224:
                                var68 = -0.10805929
                            else:
                                var68 = 0.084690824
                else:
                    if input[0] < 0.8540864:
                        var68 = 0.122627564
                    else:
                        if input[2] < -1.0257694:
                            var68 = 0.09794898
                        else:
                            if input[6] < -0.63759214:
                                var68 = 0.020610403
                            else:
                                var68 = -0.062755495
        else:
            var68 = 0.12899253
    if input[4] < 0.97290224:
        if input[10] < 2.0151885:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[5] < -0.53826725:
                        if input[0] < 0.3718626:
                            if input[2] < -0.90930384:
                                var69 = -0.03397354
                            else:
                                var69 = 0.13114648
                        else:
                            if input[4] < -0.7224126:
                                var69 = 0.07788299
                            else:
                                var69 = -0.07602564
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var69 = 0.03966311
                            else:
                                var69 = -0.04908636
                        else:
                            if input[1] < -1.4636511:
                                var69 = 0.01129413
                            else:
                                var69 = -0.058163762
                else:
                    var69 = 0.1501298
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var69 = 0.019776717
                            else:
                                var69 = -0.080943376
                        else:
                            var69 = 0.15808408
                    else:
                        if input[5] < -0.53826725:
                            if input[3] < -0.19687115:
                                var69 = 0.062954105
                            else:
                                var69 = -0.05070937
                        else:
                            if input[3] < 0.12883902:
                                var69 = -0.07627185
                            else:
                                var69 = 0.014431383
                else:
                    if input[5] < -0.53826725:
                        if input[5] < -0.55487835:
                            var69 = 0.107225984
                        else:
                            if input[1] < 1.4339409:
                                var69 = 0.0014191308
                            else:
                                var69 = 0.11259835
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var69 = 0.06735337
                            else:
                                var69 = -0.1146611
                        else:
                            if input[3] < -0.5225813:
                                var69 = -0.13541421
                            else:
                                var69 = -0.034495454
        else:
            var69 = 0.13539195
    else:
        var69 = 0.13678516
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var70 = -0.055957865
                            else:
                                var70 = 0.16528085
                        else:
                            if input[2] < -0.67637277:
                                var70 = 0.020223023
                            else:
                                var70 = -0.045654405
                    else:
                        var70 = 0.15226015
                else:
                    if input[3] < -0.19687115:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var70 = 0.048400983
                            else:
                                var70 = -0.03268182
                        else:
                            if input[1] < -1.3477474:
                                var70 = -0.11019237
                            else:
                                var70 = -0.017817825
                    else:
                        if input[5] < -0.5270547:
                            if input[2] < 0.95414454:
                                var70 = -0.039115723
                            else:
                                var70 = 0.069065556
                        else:
                            if input[2] < -0.67637277:
                                var70 = -0.04084025
                            else:
                                var70 = -0.09096675
            else:
                var70 = 0.14874868
        else:
            if input[3] < 0.45454916:
                if input[5] < -0.53826725:
                    if input[4] < 0.7307144:
                        if input[6] < 0.40938237:
                            if input[0] < 0.21112132:
                                var70 = -0.041583445
                            else:
                                var70 = 0.036063526
                        else:
                            if input[3] < 0.12883902:
                                var70 = -0.09403255
                            else:
                                var70 = 0.053463716
                    else:
                        if input[6] < -0.8702531:
                            var70 = 0.117270656
                        else:
                            var70 = 0.030337613
                else:
                    if input[7] < 0.8726697:
                        if input[6] < 0.17672138:
                            if input[2] < -0.67637277:
                                var70 = -0.026940135
                            else:
                                var70 = -0.097441606
                        else:
                            var70 = 0.14125577
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var70 = 0.02900094
                            else:
                                var70 = -0.12693045
                        else:
                            if input[10] < 2.0151885:
                                var70 = -0.10433369
                            else:
                                var70 = 0.08121255
            else:
                if input[0] < 0.8540864:
                    var70 = 0.13162668
                else:
                    if input[2] < -1.3751659:
                        var70 = 0.13900517
                    else:
                        if input[1] < -0.30461434:
                            if input[1] < -0.94208455:
                                var70 = -0.017030148
                            else:
                                var70 = 0.06338451
                        else:
                            if input[7] < 0.8726697:
                                var70 = -0.012241436
                            else:
                                var70 = -0.05546425
    else:
        var70 = 0.13650075
    if input[4] < 0.97290224:
        if input[0] < 0.93445706:
            if input[10] < 2.0151885:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var71 = 0.114104964
                            else:
                                var71 = -0.10169043
                        else:
                            if input[0] < -1.5570326:
                                var71 = 0.029532222
                            else:
                                var71 = -0.0418051
                    else:
                        var71 = 0.15065642
                else:
                    if input[3] < 0.12883902:
                        if input[5] < -0.53826725:
                            if input[5] < -0.55487835:
                                var71 = 0.11312281
                            else:
                                var71 = 0.016621703
                        else:
                            if input[1] < -0.36256617:
                                var71 = -0.020304041
                            else:
                                var71 = -0.09397596
                    else:
                        if input[0] < 0.05038005:
                            var71 = 0.14705867
                        else:
                            if input[3] < 0.45454916:
                                var71 = -0.05804141
                            else:
                                var71 = 0.057125896
            else:
                var71 = 0.13271052
        else:
            var71 = 0.13387129
    else:
        var71 = 0.13523586
    if input[4] < 0.97290224:
        if input[7] < 0.8726697:
            if input[6] < 0.17672138:
                if input[9] < 1.3985938:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            var72 = 0.20976168
                        else:
                            if input[5] < -0.50504506:
                                var72 = 0.058485214
                            else:
                                var72 = -0.10472923
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < -0.19687115:
                                var72 = -0.113037385
                            else:
                                var72 = -0.03886476
                        else:
                            if input[2] < -0.67637277:
                                var72 = 0.04619801
                            else:
                                var72 = -0.039108325
                else:
                    if input[1] < -1.1159401:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var72 = -0.028706754
                            else:
                                var72 = -0.13343504
                        else:
                            if input[0] < -0.7533263:
                                var72 = 0.08550352
                            else:
                                var72 = -0.086092934
                    else:
                        if input[1] < -0.420518:
                            if input[2] < -0.55990726:
                                var72 = 0.13642697
                            else:
                                var72 = -0.050665885
                        else:
                            if input[3] < -0.19687115:
                                var72 = -0.080305666
                            else:
                                var72 = 0.015187543
            else:
                var72 = 0.14936474
        else:
            if input[8] < 1.4017887:
                if input[1] < -1.4636511:
                    if input[9] < 1.3985938:
                        var72 = 0.20267873
                    else:
                        if input[0] < -1.476662:
                            if input[1] < -1.6375066:
                                var72 = 0.013683946
                            else:
                                var72 = -0.06589576
                        else:
                            if input[3] < 0.12883902:
                                var72 = -0.12811571
                            else:
                                var72 = -0.054400194
                else:
                    if input[5] < -0.53826725:
                        if input[9] < 1.3985938:
                            if input[0] < -0.91406757:
                                var72 = 0.120650135
                            else:
                                var72 = -0.064817086
                        else:
                            if input[6] < -0.63759214:
                                var72 = 0.16635521
                            else:
                                var72 = 0.024767455
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < -0.19687115:
                                var72 = -0.11811013
                            else:
                                var72 = -0.043075394
                        else:
                            if input[2] < -0.67637277:
                                var72 = 0.028809758
                            else:
                                var72 = -0.056455147
            else:
                if input[1] < -1.4636511:
                    if input[3] < 0.12883902:
                        var72 = -0.12699035
                    else:
                        if input[0] < 0.3718626:
                            var72 = -0.0014489731
                        else:
                            var72 = -0.07352085
                else:
                    if input[2] < -0.79283834:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var72 = -0.035787873
                            else:
                                var72 = 0.14578764
                        else:
                            if input[0] < -1.5570326:
                                var72 = 0.046229705
                            else:
                                var72 = -0.060891207
                    else:
                        if input[5] < -0.53826725:
                            if input[0] < 0.45223323:
                                var72 = -0.009474352
                            else:
                                var72 = 0.122821905
                        else:
                            if input[3] < -0.19687115:
                                var72 = -0.08593199
                            else:
                                var72 = -0.019929824
    else:
        var72 = 0.13329716
    if input[0] < 0.93445706:
        if input[10] < 2.0151885:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[0] < -0.7533263:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var73 = 0.034479365
                            else:
                                var73 = -0.0200648
                        else:
                            var73 = 0.14941853
                    else:
                        if input[2] < -0.55990726:
                            if input[1] < 0.21695223:
                                var73 = 0.025506537
                            else:
                                var73 = -0.06932734
                        else:
                            if input[6] < -0.055939615:
                                var73 = -0.08468719
                            else:
                                var73 = -0.021467445
                else:
                    var73 = 0.14624883
            else:
                if input[3] < 0.7802593:
                    if input[5] < -0.50504506:
                        if input[5] < -0.55487835:
                            var73 = 0.09286913
                        else:
                            if input[1] < -1.2318437:
                                var73 = 0.05049933
                            else:
                                var73 = -0.015225812
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var73 = -0.05728419
                            else:
                                var73 = 0.0288936
                        else:
                            if input[1] < -1.4636511:
                                var73 = -0.011514621
                            else:
                                var73 = -0.08545783
                else:
                    var73 = 0.12332516
        else:
            var73 = 0.13218173
    else:
        var73 = 0.13314776
    if input[5] < -0.55487835:
        var74 = 0.1320228
    else:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var74 = 0.1998416
                            else:
                                var74 = -0.083523
                        else:
                            if input[1] < -1.1159401:
                                var74 = -0.08803135
                            else:
                                var74 = -0.011822249
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < 0.12883902:
                                var74 = -0.11451509
                            else:
                                var74 = -0.009752061
                        else:
                            if input[1] < -0.36256617:
                                var74 = 0.03215445
                            else:
                                var74 = -0.04393881
                else:
                    var74 = 0.14865112
            else:
                if input[8] < 1.4017887:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            var74 = 0.1938628
                        else:
                            if input[0] < -1.476662:
                                var74 = -0.033539265
                            else:
                                var74 = -0.12052974
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < -0.5225813:
                                var74 = -0.12684108
                            else:
                                var74 = -0.04841341
                        else:
                            if input[2] < -0.55990726:
                                var74 = 0.021964928
                            else:
                                var74 = -0.04213369
                else:
                    if input[1] < -1.3477474:
                        if input[0] < -1.5570326:
                            var74 = -0.031794153
                        else:
                            if input[3] < -0.19687115:
                                var74 = -0.13571164
                            else:
                                var74 = -0.07713182
                    else:
                        if input[2] < -0.79283834:
                            if input[1] < -0.36256617:
                                var74 = 0.086217396
                            else:
                                var74 = -0.04801138
                        else:
                            if input[5] < -0.53826725:
                                var74 = 0.036129795
                            else:
                                var74 = -0.05317565
        else:
            var74 = 0.12977031
    if input[0] < 0.93445706:
        if input[10] < 2.0151885:
            if input[4] < 0.97290224:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[1] < -0.014855128:
                            if input[2] < -0.67637277:
                                var75 = 0.05188838
                            else:
                                var75 = -0.016286714
                        else:
                            if input[0] < -1.5570326:
                                var75 = 0.023770504
                            else:
                                var75 = -0.069976375
                    else:
                        var75 = 0.1484288
                else:
                    if input[3] < 0.12883902:
                        if input[5] < -0.53826725:
                            if input[3] < -0.5225813:
                                var75 = -0.009031605
                            else:
                                var75 = 0.056314502
                        else:
                            if input[1] < -0.36256617:
                                var75 = -0.019312112
                            else:
                                var75 = -0.09249419
                    else:
                        if input[0] < 0.05038005:
                            var75 = 0.1446277
                        else:
                            if input[3] < 0.45454916:
                                var75 = -0.053218815
                            else:
                                var75 = 0.05244658
            else:
                var75 = 0.12708935
        else:
            var75 = 0.13021402
    else:
        var75 = 0.13130587
    if input[5] < -0.55487835:
        var76 = 0.12926629
    else:
        if input[0] < 0.93445706:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[2] < -0.79283834:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var76 = -0.022448217
                            else:
                                var76 = 0.1523555
                        else:
                            if input[3] < -0.5225813:
                                var76 = -0.11430136
                            else:
                                var76 = -0.016391838
                    else:
                        if input[5] < -0.53826725:
                            if input[0] < 0.3718626:
                                var76 = 0.09912229
                            else:
                                var76 = -0.06046091
                        else:
                            if input[0] < -1.5570326:
                                var76 = 0.027174456
                            else:
                                var76 = -0.048401706
                else:
                    var76 = 0.14793971
            else:
                if input[10] < 2.0151885:
                    if input[1] < -0.36256617:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var76 = -0.023717005
                            else:
                                var76 = 0.15406632
                        else:
                            if input[8] < 1.4017887:
                                var76 = -0.010454543
                            else:
                                var76 = -0.07780167
                    else:
                        if input[3] < -0.5225813:
                            if input[5] < -0.53826725:
                                var76 = 0.011986231
                            else:
                                var76 = -0.13116741
                        else:
                            if input[0] < -1.5570326:
                                var76 = 0.14301522
                            else:
                                var76 = -0.04060361
                else:
                    var76 = 0.115645975
        else:
            var76 = 0.12768248
    if input[3] < 0.7802593:
        if input[4] < 0.97290224:
            if input[10] < 2.0151885:
                if input[5] < -0.53826725:
                    if input[5] < -0.55487835:
                        var77 = 0.12197872
                    else:
                        if input[0] < -0.8336969:
                            if input[4] < 0.24633874:
                                var77 = 0.012780369
                            else:
                                var77 = 0.14534417
                        else:
                            if input[4] < -0.11694302:
                                var77 = 0.041206706
                            else:
                                var77 = -0.026566887
                else:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var77 = 0.19331247
                            else:
                                var77 = -0.10078103
                        else:
                            if input[1] < -1.1159401:
                                var77 = -0.07021469
                            else:
                                var77 = -0.010518101
                    else:
                        if input[1] < -1.4636511:
                            if input[3] < -0.19687115:
                                var77 = -0.11958561
                            else:
                                var77 = -0.06960711
                        else:
                            if input[7] < 0.8726697:
                                var77 = 0.011634953
                            else:
                                var77 = -0.034838986
            else:
                var77 = 0.12518129
        else:
            var77 = 0.12619704
    else:
        var77 = 0.12848508
    if input[0] < 0.93445706:
        if input[0] < 0.05038005:
            if input[3] < 0.12883902:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var78 = -0.067203365
                            else:
                                var78 = 0.16122548
                        else:
                            if input[1] < -0.36256617:
                                var78 = 0.0070711263
                            else:
                                var78 = -0.05594789
                    else:
                        var78 = 0.14744586
                else:
                    if input[3] < -0.19687115:
                        if input[2] < -0.67637277:
                            if input[1] < 0.21695223:
                                var78 = 0.046015643
                            else:
                                var78 = -0.04874111
                        else:
                            if input[5] < -0.5175034:
                                var78 = 0.027387736
                            else:
                                var78 = -0.040915567
                    else:
                        if input[5] < -0.5270547:
                            if input[2] < 0.95414454:
                                var78 = -0.044536486
                            else:
                                var78 = 0.05533
                        else:
                            if input[6] < 0.17672138:
                                var78 = -0.08345044
                            else:
                                var78 = -0.032573152
            else:
                var78 = 0.14427167
        else:
            if input[3] < 0.7802593:
                if input[5] < -0.5270547:
                    if input[6] < 0.40938237:
                        if input[3] < -0.84829146:
                            if input[6] < -0.75392264:
                                var78 = 0.009059123
                            else:
                                var78 = -0.083180234
                        else:
                            if input[1] < 1.2600853:
                                var78 = 0.05323073
                            else:
                                var78 = -0.050303593
                    else:
                        if input[4] < -1.0856943:
                            var78 = 0.03422595
                        else:
                            if input[4] < 0.36743265:
                                var78 = -0.08981927
                            else:
                                var78 = -0.0050710975
                else:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var78 = -0.048860017
                            else:
                                var78 = 0.14834926
                        else:
                            if input[3] < 0.45454916:
                                var78 = -0.09404308
                            else:
                                var78 = 0.012959806
                    else:
                        if input[6] < 0.17672138:
                            if input[1] < -1.4636511:
                                var78 = -0.017723994
                            else:
                                var78 = -0.10876728
                        else:
                            if input[7] < 0.8726697:
                                var78 = 0.13181034
                            else:
                                var78 = -0.08785408
            else:
                var78 = 0.11801086
    else:
        var78 = 0.12647268
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var79 = 0.18323223
                            else:
                                var79 = -0.07133051
                        else:
                            if input[5] < -0.53826725:
                                var79 = 0.055229645
                            else:
                                var79 = -0.033318643
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < 0.12883902:
                                var79 = -0.10855795
                            else:
                                var79 = -0.0069231126
                        else:
                            if input[2] < 0.25535142:
                                var79 = 0.013677614
                            else:
                                var79 = -0.061102033
                else:
                    var79 = 0.14719804
            else:
                if input[5] < -0.53826725:
                    if input[4] < -0.60131866:
                        if input[0] < 0.8540864:
                            if input[1] < 1.0862298:
                                var79 = -0.068033375
                            else:
                                var79 = 0.028288014
                        else:
                            var79 = 0.06836421
                    else:
                        if input[3] < 0.12883902:
                            if input[4] < -0.11694302:
                                var79 = 0.13969503
                            else:
                                var79 = 0.02989711
                        else:
                            var79 = -0.07830928
                else:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var79 = 0.17966038
                            else:
                                var79 = -0.11217093
                        else:
                            if input[3] < -0.19687115:
                                var79 = -0.12504862
                            else:
                                var79 = -0.06202723
                    else:
                        if input[3] < 0.12883902:
                            if input[0] < -0.7533263:
                                var79 = -0.02158755
                            else:
                                var79 = -0.086413436
                        else:
                            if input[0] < 0.05038005:
                                var79 = 0.13556872
                            else:
                                var79 = -0.04184539
        else:
            var79 = 0.12433485
    else:
        var79 = 0.12578501
    if input[0] < 0.93445706:
        if input[2] < -0.67637277:
            if input[1] < -0.36256617:
                if input[1] < -1.1159401:
                    if input[1] < -1.4636511:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var80 = 0.19430114
                            else:
                                var80 = -0.078538
                        else:
                            if input[0] < -1.3962914:
                                var80 = -0.012438326
                            else:
                                var80 = -0.10231901
                    else:
                        if input[3] < -0.19687115:
                            if input[6] < 0.17672138:
                                var80 = -0.1107922
                            else:
                                var80 = -0.039273746
                        else:
                            if input[0] < -0.7533263:
                                var80 = 0.10040549
                            else:
                                var80 = -0.043958165
                else:
                    var80 = 0.15620604
            else:
                if input[0] < -1.476662:
                    if input[3] < -0.5225813:
                        if input[5] < -0.4386006:
                            var80 = 0.05537138
                        else:
                            var80 = -0.08558024
                    else:
                        if input[0] < -1.5570326:
                            var80 = 0.121084735
                        else:
                            var80 = 0.008368602
                else:
                    if input[3] < 0.45454916:
                        if input[0] < 0.3718626:
                            if input[5] < -0.53826725:
                                var80 = 0.025824916
                            else:
                                var80 = -0.04548219
                        else:
                            if input[0] < 0.8540864:
                                var80 = -0.09994575
                            else:
                                var80 = -0.016729113
                    else:
                        if input[2] < -1.2587004:
                            var80 = 0.08407011
                        else:
                            var80 = -0.026018495
        else:
            if input[10] < 2.0151885:
                if input[5] < -0.53826725:
                    if input[1] < -0.768229:
                        if input[9] < 1.3985938:
                            if input[4] < 0.0041509015:
                                var80 = 0.009290226
                            else:
                                var80 = -0.103917636
                        else:
                            if input[11] < 1.2236042:
                                var80 = -0.06891989
                            else:
                                var80 = 0.09284233
                    else:
                        if input[0] < -0.592585:
                            if input[0] < -1.1551795:
                                var80 = 0.02971475
                            else:
                                var80 = 0.1518951
                        else:
                            if input[6] < -1.1029141:
                                var80 = 0.08920926
                            else:
                                var80 = -0.003076203
                else:
                    if input[3] < -0.5225813:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var80 = 0.06532076
                            else:
                                var80 = -0.1118771
                        else:
                            if input[6] < 0.17672138:
                                var80 = -0.13206592
                            else:
                                var80 = -0.025856255
                    else:
                        if input[0] < -1.5570326:
                            var80 = 0.15509886
                        else:
                            if input[3] < -0.19687115:
                                var80 = -0.07729572
                            else:
                                var80 = 0.0025478636
            else:
                var80 = 0.11598026
    else:
        var80 = 0.12475968
    if input[4] < 0.97290224:
        if input[7] < 0.8726697:
            if input[6] < 0.17672138:
                if input[3] < 0.12883902:
                    if input[0] < -0.8336969:
                        if input[3] < -0.19687115:
                            if input[1] < -1.4636511:
                                var81 = 0.04160087
                            else:
                                var81 = -0.030017722
                        else:
                            var81 = 0.13527873
                    else:
                        if input[2] < -0.55990726:
                            if input[1] < -0.36256617:
                                var81 = 0.019629506
                            else:
                                var81 = -0.08703381
                        else:
                            if input[1] < -1.4636511:
                                var81 = -0.008462611
                            else:
                                var81 = -0.08887801
                else:
                    if input[0] < 0.05038005:
                        var81 = 0.12986293
                    else:
                        if input[3] < 0.7802593:
                            if input[5] < -0.53826725:
                                var81 = 0.05533566
                            else:
                                var81 = -0.050124045
                        else:
                            var81 = 0.09118889
            else:
                var81 = 0.146522
        else:
            if input[5] < -0.53826725:
                if input[4] < -0.60131866:
                    if input[0] < 0.8540864:
                        if input[1] < 1.0862298:
                            if input[9] < 1.3985938:
                                var81 = -0.10791637
                            else:
                                var81 = 0.015075031
                        else:
                            var81 = 0.02356855
                    else:
                        var81 = 0.061651994
                else:
                    if input[3] < 0.12883902:
                        if input[0] < 0.6129745:
                            if input[4] < -0.23803693:
                                var81 = 0.14941236
                            else:
                                var81 = 0.037097383
                        else:
                            if input[8] < 1.4017887:
                                var81 = -0.09062739
                            else:
                                var81 = 0.030145619
                    else:
                        var81 = -0.07049481
            else:
                if input[1] < -0.36256617:
                    if input[2] < -0.67637277:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var81 = 0.012765641
                            else:
                                var81 = -0.08721082
                        else:
                            var81 = 0.14976977
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var81 = 0.057523698
                            else:
                                var81 = -0.089452684
                        else:
                            if input[3] < -0.5225813:
                                var81 = -0.11901531
                            else:
                                var81 = -0.04251696
                else:
                    if input[3] < -0.5225813:
                        if input[0] < 0.6933451:
                            var81 = -0.12744144
                        else:
                            var81 = 0.035126433
                    else:
                        if input[0] < -1.5570326:
                            var81 = 0.13073285
                        else:
                            if input[3] < -0.19687115:
                                var81 = -0.12383323
                            else:
                                var81 = -0.007793947
    else:
        var81 = 0.12385931
    if input[5] < -0.55487835:
        var82 = 0.122855216
    else:
        if input[0] < 0.93445706:
            if input[10] < 2.0151885:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var82 = -0.06294768
                            else:
                                var82 = 0.15526092
                        else:
                            if input[1] < -0.36256617:
                                var82 = 0.00096016756
                            else:
                                var82 = -0.059361104
                    else:
                        var82 = 0.14611284
                else:
                    if input[3] < 0.12883902:
                        if input[3] < -0.19687115:
                            if input[2] < -0.67637277:
                                var82 = 0.013286655
                            else:
                                var82 = -0.030495316
                        else:
                            if input[1] < -0.36256617:
                                var82 = -0.04131869
                            else:
                                var82 = -0.089661084
                    else:
                        if input[0] < 0.05038005:
                            var82 = 0.14101636
                        else:
                            if input[3] < 0.45454916:
                                var82 = -0.050386272
                            else:
                                var82 = 0.048934944
            else:
                var82 = 0.120472506
        else:
            var82 = 0.121555686
    if input[4] < 0.97290224:
        if input[7] < 0.8726697:
            if input[6] < 0.17672138:
                if input[5] < -0.53826725:
                    if input[4] < -0.7224126:
                        if input[9] < 1.3985938:
                            if input[1] < -0.1307588:
                                var83 = 0.049382024
                            else:
                                var83 = 0.20413545
                        else:
                            var83 = -0.06098204
                    else:
                        if input[2] < 0.25535142:
                            if input[0] < 0.3718626:
                                var83 = 0.11670463
                            else:
                                var83 = -0.07174552
                        else:
                            var83 = -0.080748886
                else:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var83 = -0.038437836
                            else:
                                var83 = 0.14815943
                        else:
                            if input[3] < -0.19687115:
                                var83 = -0.08637973
                            else:
                                var83 = -0.006977232
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var83 = 0.058427047
                            else:
                                var83 = -0.089893945
                        else:
                            if input[3] < -0.5225813:
                                var83 = -0.119559124
                            else:
                                var83 = -0.026063185
            else:
                var83 = 0.14575185
        else:
            if input[5] < -0.53826725:
                if input[4] < -0.60131866:
                    if input[0] < 0.8540864:
                        if input[1] < 1.0862298:
                            if input[9] < 1.3985938:
                                var83 = -0.10173765
                            else:
                                var83 = 0.017078944
                        else:
                            var83 = 0.023992993
                    else:
                        var83 = 0.056986954
                else:
                    if input[6] < 1.4563569:
                        if input[3] < 0.12883902:
                            if input[0] < 0.6129745:
                                var83 = 0.08042896
                            else:
                                var83 = -0.032365862
                        else:
                            var83 = -0.06536082
                    else:
                        if input[6] < 1.6890179:
                            var83 = -0.08341874
                        else:
                            var83 = 0.007002355
            else:
                if input[1] < -1.4636511:
                    if input[8] < 1.4017887:
                        if input[9] < 1.3985938:
                            var83 = 0.16873217
                        else:
                            if input[3] < -0.19687115:
                                var83 = -0.11803281
                            else:
                                var83 = -0.050614208
                    else:
                        if input[3] < 0.12883902:
                            var83 = -0.11617847
                        else:
                            var83 = -0.02904818
                else:
                    if input[3] < -0.19687115:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var83 = -0.11537565
                            else:
                                var83 = 0.026908217
                        else:
                            if input[0] < -1.5570326:
                                var83 = 0.01801894
                            else:
                                var83 = -0.12045842
                    else:
                        if input[0] < -0.7533263:
                            var83 = 0.13769601
                        else:
                            if input[3] < 0.12883902:
                                var83 = -0.103982165
                            else:
                                var83 = 0.01300162
    else:
        var83 = 0.12138599
    if input[0] < 0.93445706:
        if input[10] < 2.0151885:
            if input[0] < 0.05038005:
                if input[3] < 0.12883902:
                    if input[8] < 1.4017887:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var84 = 0.17575762
                            else:
                                var84 = -0.083725676
                        else:
                            if input[5] < -0.53826725:
                                var84 = 0.054602686
                            else:
                                var84 = -0.018655123
                    else:
                        if input[1] < -1.1738919:
                            if input[0] < -1.5570326:
                                var84 = 0.004448602
                            else:
                                var84 = -0.09259517
                        else:
                            if input[2] < -0.67637277:
                                var84 = 0.03418563
                            else:
                                var84 = -0.025370134
                else:
                    var84 = 0.14005004
            else:
                if input[3] < 0.7802593:
                    if input[5] < -0.53826725:
                        if input[4] < 0.7307144:
                            if input[6] < 0.87470436:
                                var84 = 0.00906315
                            else:
                                var84 = -0.06767152
                        else:
                            var84 = 0.08809771
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var84 = 0.015288199
                            else:
                                var84 = -0.06970594
                        else:
                            if input[1] < -1.4636511:
                                var84 = -0.009523142
                            else:
                                var84 = -0.079404406
                else:
                    var84 = 0.11286965
        else:
            var84 = 0.12031356
    else:
        var84 = 0.12133957
    if input[4] < 0.97290224:
        if input[7] < 0.8726697:
            if input[6] < 0.17672138:
                if input[5] < -0.53826725:
                    if input[4] < -0.7224126:
                        if input[9] < 1.3985938:
                            if input[4] < -1.0856943:
                                var85 = 0.04676601
                            else:
                                var85 = 0.18957911
                        else:
                            var85 = -0.05921336
                    else:
                        if input[2] < 0.25535142:
                            if input[4] < 0.24633874:
                                var85 = -0.038522616
                            else:
                                var85 = 0.12722726
                        else:
                            var85 = -0.07660054
                else:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var85 = -0.03628241
                            else:
                                var85 = 0.14529657
                        else:
                            if input[3] < -0.5225813:
                                var85 = -0.10427
                            else:
                                var85 = -0.019697879
                    else:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var85 = -0.108412825
                            else:
                                var85 = 0.13825785
                        else:
                            if input[3] < -0.19687115:
                                var85 = -0.08113973
                            else:
                                var85 = -0.0038353805
            else:
                var85 = 0.14495139
        else:
            if input[10] < 2.0151885:
                if input[0] < -1.3962914:
                    if input[3] < -0.5225813:
                        if input[5] < -0.53826725:
                            if input[4] < -0.11694302:
                                var85 = -0.05808818
                            else:
                                var85 = 0.12261432
                        else:
                            if input[1] < -1.4636511:
                                var85 = 0.0037633819
                            else:
                                var85 = -0.09855823
                    else:
                        if input[0] < -1.5570326:
                            var85 = 0.1390199
                        else:
                            if input[3] < -0.19687115:
                                var85 = -0.023107175
                            else:
                                var85 = 0.09639066
                else:
                    if input[0] < 0.93445706:
                        if input[3] < 0.45454916:
                            if input[5] < -0.53826725:
                                var85 = 0.005220781
                            else:
                                var85 = -0.03916112
                        else:
                            if input[0] < 0.8540864:
                                var85 = 0.11445202
                            else:
                                var85 = -0.020828744
                    else:
                        var85 = 0.101386584
            else:
                var85 = 0.102456465
    else:
        var85 = 0.11899679
    if input[5] < -0.55487835:
        var86 = 0.11845256
    else:
        if input[0] < 0.93445706:
            if input[0] < -0.7533263:
                if input[3] < -0.19687115:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[1] < -1.4636511:
                                var86 = 0.008836546
                            else:
                                var86 = -0.075656295
                        else:
                            var86 = 0.1501945
                    else:
                        if input[3] < -0.5225813:
                            if input[5] < -0.53826725:
                                var86 = 0.08368789
                            else:
                                var86 = -0.009058055
                        else:
                            if input[1] < -0.420518:
                                var86 = -0.02478224
                            else:
                                var86 = -0.09124175
                else:
                    var86 = 0.14449883
            else:
                if input[3] < 0.12883902:
                    if input[3] < -0.19687115:
                        if input[8] < 1.4017887:
                            if input[1] < -1.4636511:
                                var86 = 0.05482032
                            else:
                                var86 = -0.01456569
                        else:
                            if input[1] < -1.1159401:
                                var86 = -0.09195271
                            else:
                                var86 = -0.001622405
                    else:
                        if input[1] < -0.36256617:
                            if input[2] < -0.3269762:
                                var86 = 0.004146186
                            else:
                                var86 = -0.068821415
                        else:
                            if input[4] < 0.8518083:
                                var86 = -0.0883271
                            else:
                                var86 = 0.008315973
                else:
                    if input[0] < 0.05038005:
                        var86 = 0.13765697
                    else:
                        if input[3] < 0.45454916:
                            if input[5] < -0.53826725:
                                var86 = 0.018700363
                            else:
                                var86 = -0.06381965
                        else:
                            if input[0] < 0.8540864:
                                var86 = 0.12308404
                            else:
                                var86 = -0.011856405
        else:
            var86 = 0.1161801
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var87 = 0.16549264
                            else:
                                var87 = -0.06783808
                        else:
                            if input[1] < -1.1159401:
                                var87 = -0.07710624
                            else:
                                var87 = -0.0075645074
                    else:
                        if input[1] < -1.3477474:
                            if input[0] < -1.3962914:
                                var87 = -0.021736294
                            else:
                                var87 = -0.109092966
                        else:
                            if input[2] < 0.25535142:
                                var87 = 0.006558441
                            else:
                                var87 = -0.05729234
                else:
                    var87 = 0.14410408
            else:
                if input[1] < -0.36256617:
                    if input[2] < -0.67637277:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var87 = 0.01125955
                            else:
                                var87 = -0.065798715
                        else:
                            var87 = 0.14816003
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var87 = 0.051499557
                            else:
                                var87 = -0.090238184
                        else:
                            if input[5] < -0.53826725:
                                var87 = 0.013710599
                            else:
                                var87 = -0.07216953
                else:
                    if input[5] < -0.53826725:
                        if input[2] < 0.604748:
                            if input[1] < 1.0862298:
                                var87 = -0.048584513
                            else:
                                var87 = 0.0668651
                        else:
                            if input[1] < 0.5067114:
                                var87 = 0.110954665
                            else:
                                var87 = -0.011810013
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var87 = 0.0029065022
                            else:
                                var87 = -0.12890972
                        else:
                            if input[0] < -0.7533263:
                                var87 = 0.12288786
                            else:
                                var87 = -0.053592633
        else:
            var87 = 0.115298964
    else:
        var87 = 0.11743519
    if input[0] < 0.93445706:
        if input[5] < -0.55487835:
            var88 = 0.11415865
        else:
            if input[10] < 2.0151885:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var88 = -0.053658914
                            else:
                                var88 = 0.14751029
                        else:
                            if input[2] < -0.67637277:
                                var88 = 0.012574809
                            else:
                                var88 = -0.04495875
                    else:
                        var88 = 0.14287354
                else:
                    if input[3] < 0.12883902:
                        if input[3] < -0.19687115:
                            if input[2] < -0.67637277:
                                var88 = 0.009299928
                            else:
                                var88 = -0.02926777
                        else:
                            if input[5] < -0.53826725:
                                var88 = -0.0007556333
                            else:
                                var88 = -0.064882234
                    else:
                        if input[0] < 0.05038005:
                            var88 = 0.13622738
                        else:
                            if input[3] < 0.45454916:
                                var88 = -0.04229267
                            else:
                                var88 = 0.043467954
            else:
                var88 = 0.112448685
    else:
        var88 = 0.11568376
    if input[4] < 0.97290224:
        if input[0] < 0.93445706:
            if input[5] < -0.55487835:
                var89 = 0.10984685
            else:
                if input[10] < 2.0151885:
                    if input[2] < -0.67637277:
                        if input[1] < -0.36256617:
                            if input[1] < -1.1159401:
                                var89 = -0.014465602
                            else:
                                var89 = 0.1509621
                        else:
                            if input[3] < -0.5225813:
                                var89 = -0.07823395
                            else:
                                var89 = -0.018339721
                    else:
                        if input[3] < 0.7802593:
                            if input[1] < -1.4636511:
                                var89 = 0.015181642
                            else:
                                var89 = -0.025510842
                        else:
                            var89 = 0.09931789
                else:
                    var89 = 0.10848318
        else:
            var89 = 0.11202305
    else:
        var89 = 0.113595076
    if input[3] < 0.7802593:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[5] < -0.53826725:
                        if input[2] < -0.90930384:
                            if input[1] < 0.04309671:
                                var90 = 0.008715422
                            else:
                                var90 = -0.06545855
                        else:
                            if input[0] < 0.3718626:
                                var90 = 0.103917666
                            else:
                                var90 = -0.027100489
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var90 = 0.031076794
                            else:
                                var90 = -0.05507519
                        else:
                            if input[1] < -1.4636511:
                                var90 = 0.016144494
                            else:
                                var90 = -0.05655691
                else:
                    var90 = 0.14337431
            else:
                if input[5] < -0.53826725:
                    if input[4] < -0.60131866:
                        if input[1] < 0.4487596:
                            if input[3] < 0.12883902:
                                var90 = -0.08424024
                            else:
                                var90 = 0.037509687
                        else:
                            if input[3] < -0.5225813:
                                var90 = -0.04533191
                            else:
                                var90 = 0.09511092
                    else:
                        if input[3] < 0.12883902:
                            if input[6] < 1.2236959:
                                var90 = 0.0598577
                            else:
                                var90 = -0.04071352
                        else:
                            var90 = -0.07656835
                else:
                    if input[1] < -0.36256617:
                        if input[9] < 1.3985938:
                            if input[8] < 1.4017887:
                                var90 = 0.062905304
                            else:
                                var90 = -0.046970725
                        else:
                            if input[1] < -1.1159401:
                                var90 = -0.09224222
                            else:
                                var90 = 0.026296984
                    else:
                        if input[3] < -0.5225813:
                            if input[0] < 0.29149196:
                                var90 = -0.122247584
                            else:
                                var90 = -0.000055871442
                        else:
                            if input[0] < -1.5570326:
                                var90 = 0.10843281
                            else:
                                var90 = -0.05097598
        else:
            var90 = 0.10963497
    else:
        var90 = 0.11041761
    if input[0] < 0.93445706:
        if input[0] < -0.7533263:
            if input[3] < -0.19687115:
                if input[0] < -1.5570326:
                    if input[3] < -0.5225813:
                        if input[5] < -0.53826725:
                            if input[4] < -0.11694302:
                                var91 = -0.029384032
                            else:
                                var91 = 0.07159393
                        else:
                            if input[1] < -1.4636511:
                                var91 = 0.010365015
                            else:
                                var91 = -0.09179402
                    else:
                        var91 = 0.14494872
                else:
                    if input[3] < -0.5225813:
                        if input[5] < -0.53826725:
                            if input[6] < 0.40938237:
                                var91 = 0.120986424
                            else:
                                var91 = -0.039297156
                        else:
                            if input[2] < -0.67637277:
                                var91 = 0.02315747
                            else:
                                var91 = -0.04039193
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var91 = 0.057570565
                            else:
                                var91 = -0.07788965
                        else:
                            if input[2] < -0.67637277:
                                var91 = -0.022372115
                            else:
                                var91 = -0.09181351
            else:
                var91 = 0.14190625
        else:
            if input[3] < 0.12883902:
                if input[5] < -0.53826725:
                    if input[3] < -0.5225813:
                        if input[6] < -0.8702531:
                            if input[9] < 1.3985938:
                                var91 = -0.007357104
                            else:
                                var91 = 0.116154544
                        else:
                            if input[1] < 0.9703261:
                                var91 = -0.08655955
                            else:
                                var91 = 0.010769153
                    else:
                        if input[1] < 0.79647064:
                            if input[4] < -1.2067883:
                                var91 = -0.070113786
                            else:
                                var91 = 0.07606711
                        else:
                            if input[2] < -1.0257694:
                                var91 = 0.055417065
                            else:
                                var91 = -0.10077
                else:
                    if input[8] < 1.4017887:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var91 = 0.15210864
                            else:
                                var91 = -0.121798865
                        else:
                            if input[1] < -1.1159401:
                                var91 = -0.107287675
                            else:
                                var91 = -0.026325503
                    else:
                        if input[1] < -1.1159401:
                            if input[6] < 0.17672138:
                                var91 = -0.124198504
                            else:
                                var91 = -0.05650657
                        else:
                            if input[2] < -0.67637277:
                                var91 = 0.017100675
                            else:
                                var91 = -0.06493986
            else:
                if input[0] < 0.05038005:
                    var91 = 0.13510592
                else:
                    if input[3] < 0.45454916:
                        if input[5] < -0.53826725:
                            if input[4] < -1.0856943:
                                var91 = 0.089623846
                            else:
                                var91 = -0.027935235
                        else:
                            if input[1] < -0.420518:
                                var91 = -0.025426192
                            else:
                                var91 = -0.09902118
                    else:
                        if input[0] < 0.8540864:
                            var91 = 0.11974437
                        else:
                            if input[2] < -1.0257694:
                                var91 = 0.061730396
                            else:
                                var91 = -0.0594433
    else:
        var91 = 0.10990971
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[7] < 0.8726697:
                if input[6] < 0.17672138:
                    if input[9] < 1.3985938:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var92 = 0.15812322
                            else:
                                var92 = -0.064142376
                        else:
                            if input[1] < -1.1159401:
                                var92 = -0.07362807
                            else:
                                var92 = -0.0063829194
                    else:
                        if input[1] < -1.1159401:
                            if input[3] < 0.12883902:
                                var92 = -0.10198627
                            else:
                                var92 = -0.0018964682
                        else:
                            if input[2] < 0.25535142:
                                var92 = 0.013486066
                            else:
                                var92 = -0.05327693
                else:
                    var92 = 0.14251058
            else:
                if input[2] < -1.0257694:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.2897956:
                                var92 = 0.01099043
                            else:
                                var92 = -0.081118
                        else:
                            var92 = 0.13854995
                    else:
                        if input[5] < -0.53826725:
                            if input[1] < 0.39080775:
                                var92 = -0.058589417
                            else:
                                var92 = 0.05634326
                        else:
                            if input[3] < 0.12883902:
                                var92 = -0.08547819
                            else:
                                var92 = 0.010125662
                else:
                    if input[5] < -0.53826725:
                        if input[2] < 0.37181693:
                            if input[2] < -0.09404516:
                                var92 = 0.001408371
                            else:
                                var92 = -0.10588408
                        else:
                            if input[6] < -0.9865836:
                                var92 = -0.04376821
                            else:
                                var92 = 0.052550804
                    else:
                        if input[1] < -1.4636511:
                            if input[8] < 1.4017887:
                                var92 = 0.052539747
                            else:
                                var92 = -0.09271979
                        else:
                            if input[3] < -0.19687115:
                                var92 = -0.077793285
                            else:
                                var92 = -0.014490206
        else:
            var92 = 0.1073884
    else:
        var92 = 0.11026912
    if input[5] < -0.55487835:
        var93 = 0.10771429
    else:
        if input[0] < 0.93445706:
            if input[0] < -0.7533263:
                if input[3] < -0.19687115:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[1] < 1.4339409:
                                var93 = -0.05329226
                            else:
                                var93 = 0.050922345
                        else:
                            var93 = 0.14268444
                    else:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var93 = 0.045114234
                            else:
                                var93 = -0.051951665
                        else:
                            if input[1] < -1.1159401:
                                var93 = -0.10249814
                            else:
                                var93 = -0.029519143
                else:
                    var93 = 0.140411
            else:
                if input[3] < 0.12883902:
                    if input[3] < -0.19687115:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var93 = -0.030330064
                            else:
                                var93 = 0.042527217
                        else:
                            if input[6] < -0.055939615:
                                var93 = -0.043285042
                            else:
                                var93 = -0.001040445
                    else:
                        if input[1] < -0.36256617:
                            if input[2] < -0.3269762:
                                var93 = 0.010586555
                            else:
                                var93 = -0.061740726
                        else:
                            if input[2] < 0.95414454:
                                var93 = -0.09251162
                            else:
                                var93 = -0.018884392
                else:
                    if input[0] < 0.05038005:
                        var93 = 0.13304414
                    else:
                        if input[3] < 0.45454916:
                            if input[5] < -0.53826725:
                                var93 = 0.019681372
                            else:
                                var93 = -0.056084022
                        else:
                            if input[0] < 0.8540864:
                                var93 = 0.11660097
                            else:
                                var93 = -0.015793817
        else:
            var93 = 0.10642757
    if input[10] < 2.0151885:
        if input[4] < 0.97290224:
            if input[0] < 0.93445706:
                if input[0] < -0.7533263:
                    if input[3] < -0.19687115:
                        if input[0] < -1.5570326:
                            if input[3] < -0.5225813:
                                var94 = -0.03614644
                            else:
                                var94 = 0.1394698
                        else:
                            if input[3] < -0.5225813:
                                var94 = 0.0046277805
                            else:
                                var94 = -0.0497852
                    else:
                        var94 = 0.13855585
                else:
                    if input[3] < 0.12883902:
                        if input[5] < -0.53826725:
                            if input[4] < -0.11694302:
                                var94 = 0.0372116
                            else:
                                var94 = -0.019188046
                        else:
                            if input[1] < -0.36256617:
                                var94 = -0.017730206
                            else:
                                var94 = -0.084156044
                    else:
                        if input[0] < 0.05038005:
                            var94 = 0.13068911
                        else:
                            if input[3] < 0.7802593:
                                var94 = -0.020037403
                            else:
                                var94 = 0.09395296
            else:
                var94 = 0.10330341
        else:
            var94 = 0.104712754
    else:
        var94 = 0.107470736
    if input[7] < 0.8726697:
        if input[6] < 0.17672138:
            if input[5] < -0.53826725:
                if input[4] < -0.7224126:
                    if input[9] < 1.3985938:
                        if input[4] < -1.0856943:
                            if input[6] < -0.9865836:
                                var95 = -0.038457643
                            else:
                                var95 = 0.096578635
                        else:
                            var95 = 0.17070329
                    else:
                        var95 = -0.060952198
                else:
                    if input[2] < 0.25535142:
                        if input[4] < 0.24633874:
                            if input[6] < -0.52126163:
                                var95 = -0.07204107
                            else:
                                var95 = 0.020174678
                        else:
                            if input[2] < -0.3269762:
                                var95 = 0.024713887
                            else:
                                var95 = 0.16576119
                    else:
                        var95 = -0.079336196
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var95 = 0.005832048
                            else:
                                var95 = -0.08161345
                        else:
                            var95 = 0.13985366
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var95 = 0.013741847
                            else:
                                var95 = -0.10496261
                        else:
                            if input[0] < -0.51221436:
                                var95 = 0.04258652
                            else:
                                var95 = -0.031223945
                else:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var95 = 0.13059942
                            else:
                                var95 = -0.075988404
                        else:
                            var95 = -0.069893405
                    else:
                        if input[3] < -0.19687115:
                            if input[0] < -1.5570326:
                                var95 = 0.019134933
                            else:
                                var95 = -0.112015285
                        else:
                            if input[0] < -0.7533263:
                                var95 = 0.109032266
                            else:
                                var95 = -0.049666014
        else:
            var95 = 0.1418234
    else:
        if input[6] < 0.40938237:
            if input[1] < -0.014855128:
                if input[2] < -0.67637277:
                    if input[1] < -1.1159401:
                        if input[5] < -0.53826725:
                            var95 = 0.10896879
                        else:
                            if input[1] < -1.4636511:
                                var95 = 0.024711642
                            else:
                                var95 = -0.0738445
                    else:
                        if input[1] < -0.36256617:
                            var95 = 0.13382125
                        else:
                            var95 = -0.022666663
                else:
                    if input[5] < -0.5270547:
                        if input[6] < -0.17227012:
                            if input[3] < -0.5225813:
                                var95 = 0.049887843
                            else:
                                var95 = -0.06834367
                        else:
                            if input[0] < 0.29149196:
                                var95 = 0.012895141
                            else:
                                var95 = 0.1935391
                    else:
                        if input[1] < -1.4636511:
                            if input[9] < 1.3985938:
                                var95 = 0.06827055
                            else:
                                var95 = -0.07523982
                        else:
                            if input[3] < 0.12883902:
                                var95 = -0.068924636
                            else:
                                var95 = -0.00818809
            else:
                if input[6] < 0.060390886:
                    if input[2] < 1.4200066:
                        if input[1] < 1.3180372:
                            if input[1] < 1.0862298:
                                var95 = -0.025757607
                            else:
                                var95 = 0.08441287
                        else:
                            if input[5] < -0.50504506:
                                var95 = -0.087190524
                            else:
                                var95 = -0.021344827
                    else:
                        if input[1] < 0.9703261:
                            var95 = 0.0075922734
                        else:
                            var95 = 0.079548255
                else:
                    if input[0] < -0.9944382:
                        var95 = 0.0018175271
                    else:
                        var95 = -0.08251922
        else:
            if input[3] < 0.12883902:
                if input[4] < 0.48852658:
                    if input[1] < 0.5067114:
                        if input[1] < 0.39080775:
                            if input[2] < -0.67637277:
                                var95 = 0.0011088314
                            else:
                                var95 = -0.058845416
                        else:
                            var95 = 0.06628885
                    else:
                        if input[0] < -1.5570326:
                            var95 = -0.029136857
                        else:
                            var95 = -0.099399254
                else:
                    if input[6] < 1.1073654:
                        if input[5] < -0.53826725:
                            var95 = 0.1471693
                        else:
                            if input[1] < -1.521603:
                                var95 = 0.023452247
                            else:
                                var95 = -0.019066917
                    else:
                        if input[1] < -0.36256617:
                            if input[2] < -0.21051069:
                                var95 = 0.01232297
                            else:
                                var95 = -0.046102256
                        else:
                            var95 = -0.068182684
            else:
                if input[0] < 0.05038005:
                    var95 = 0.097693436
                else:
                    if input[4] < -1.0856943:
                        var95 = 0.034534153
                    else:
                        if input[2] < -1.2587004:
                            var95 = 0.032150667
                        else:
                            if input[3] < 0.45454916:
                                var95 = -0.060118426
                            else:
                                var95 = -0.01802333
    if input[10] < 2.0151885:
        if input[5] < -0.55487835:
            var96 = 0.10343911
        else:
            if input[4] < 0.97290224:
                if input[0] < 0.93445706:
                    if input[0] < -0.8336969:
                        if input[3] < -0.19687115:
                            if input[1] < -0.014855128:
                                var96 = 0.01235452
                            else:
                                var96 = -0.03214739
                        else:
                            var96 = 0.13416126
                    else:
                        if input[3] < 0.12883902:
                            if input[2] < -0.67637277:
                                var96 = -0.0037340787
                            else:
                                var96 = -0.037452508
                        else:
                            if input[0] < 0.05038005:
                                var96 = 0.12809822
                            else:
                                var96 = -0.010358381
                else:
                    var96 = 0.10094478
            else:
                var96 = 0.102160685
    else:
        var96 = 0.10587409
    if input[10] < 2.0151885:
        if input[5] < -0.55487835:
            var97 = 0.10005627
        else:
            if input[4] < 0.97290224:
                if input[7] < 0.8726697:
                    if input[6] < 0.17672138:
                        if input[9] < 1.3985938:
                            if input[1] < -1.4636511:
                                var97 = 0.065297864
                            else:
                                var97 = -0.021594884
                        else:
                            if input[1] < -1.3477474:
                                var97 = -0.099810176
                            else:
                                var97 = -0.019062912
                    else:
                        var97 = 0.14057063
                else:
                    if input[1] < -0.30461434:
                        if input[2] < -0.67637277:
                            if input[1] < -1.1159401:
                                var97 = -0.020056548
                            else:
                                var97 = 0.1272608
                        else:
                            if input[8] < 1.4017887:
                                var97 = -0.0045551346
                            else:
                                var97 = -0.061243333
                    else:
                        if input[5] < -0.53826725:
                            if input[1] < 1.4339409:
                                var97 = -0.007986646
                            else:
                                var97 = 0.06977921
                        else:
                            if input[3] < -0.19687115:
                                var97 = -0.09502605
                            else:
                                var97 = -0.01864862
            else:
                var97 = 0.09876682
    else:
        var97 = 0.10249805
    if input[0] < 0.93445706:
        if input[10] < 2.0151885:
            if input[5] < -0.53826725:
                if input[6] < -1.4519056:
                    var98 = -0.06973138
                else:
                    if input[6] < 0.060390886:
                        if input[1] < -0.1307588:
                            if input[1] < -0.65232533:
                                var98 = 0.050310057
                            else:
                                var98 = -0.09442303
                        else:
                            if input[2] < -0.90930384:
                                var98 = 0.0036411928
                            else:
                                var98 = 0.08471373
                    else:
                        if input[11] < 1.2236042:
                            if input[2] < 0.48828247:
                                var98 = -0.03946177
                            else:
                                var98 = 0.093803674
                        else:
                            if input[0] < 0.53260386:
                                var98 = -0.05791158
                            else:
                                var98 = 0.04979091
            else:
                if input[9] < 1.3985938:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            var98 = 0.16196482
                        else:
                            if input[0] < -1.5570326:
                                var98 = -0.023862878
                            else:
                                var98 = -0.10222965
                    else:
                        if input[1] < -1.1159401:
                            if input[0] < -1.5570326:
                                var98 = 0.01877091
                            else:
                                var98 = -0.07674764
                        else:
                            if input[2] < -0.67637277:
                                var98 = 0.039915085
                            else:
                                var98 = -0.037156843
                else:
                    if input[1] < -1.4636511:
                        if input[0] < -1.5570326:
                            var98 = -0.023095258
                        else:
                            if input[3] < -0.19687115:
                                var98 = -0.11901246
                            else:
                                var98 = -0.057865735
                    else:
                        if input[2] < -0.67637277:
                            if input[1] < -0.36256617:
                                var98 = 0.06355952
                            else:
                                var98 = -0.04871575
                        else:
                            if input[6] < 0.17672138:
                                var98 = -0.047616526
                            else:
                                var98 = 0.0023127657
        else:
            var98 = 0.09847897
    else:
        var98 = 0.10062891
    if input[3] < 0.7802593:
        if input[4] < 0.97290224:
            if input[0] < -0.7533263:
                if input[3] < -0.19687115:
                    if input[0] < -1.5570326:
                        if input[3] < -0.5225813:
                            if input[5] < -0.53826725:
                                var99 = 0.027327748
                            else:
                                var99 = -0.055069625
                        else:
                            var99 = 0.13793541
                    else:
                        if input[5] < -0.53826725:
                            if input[6] < -0.8702531:
                                var99 = -0.041145723
                            else:
                                var99 = 0.06732061
                        else:
                            if input[1] < -0.36256617:
                                var99 = -0.004161134
                            else:
                                var99 = -0.075722486
                else:
                    var99 = 0.13551815
            else:
                if input[0] < 0.93445706:
                    if input[5] < -0.53826725:
                        if input[3] < -0.5225813:
                            if input[6] < -0.8702531:
                                var99 = 0.05107406
                            else:
                                var99 = -0.06320042
                        else:
                            if input[4] < -1.2067883:
                                var99 = -0.06661107
                            else:
                                var99 = 0.040674753
                    else:
                        if input[3] < 0.12883902:
                            if input[1] < -0.36256617:
                                var99 = -0.016455688
                            else:
                                var99 = -0.072070576
                        else:
                            if input[0] < 0.05038005:
                                var99 = 0.12612456
                            else:
                                var99 = -0.02432687
                else:
                    var99 = 0.094792865
        else:
            var99 = 0.09753172
    else:
        var99 = 0.09973767
    if input[7] < 0.8726697:
        if input[6] < 0.17672138:
            if input[5] < -0.53826725:
                if input[2] < -0.90930384:
                    if input[1] < 0.04309671:
                        var100 = 0.004231407
                    else:
                        var100 = -0.066068344
                else:
                    if input[0] < 0.3718626:
                        if input[2] < 0.604748:
                            if input[8] < 1.4017887:
                                var100 = 0.16563255
                            else:
                                var100 = -0.020336568
                        else:
                            if input[0] < -0.35147312:
                                var100 = 0.017549763
                            else:
                                var100 = -0.07019222
                    else:
                        if input[8] < 1.4017887:
                            var100 = -0.0834321
                        else:
                            var100 = 0.026990205
            else:
                if input[2] < -0.67637277:
                    if input[1] < -0.36256617:
                        if input[1] < -1.1159401:
                            if input[1] < -1.4636511:
                                var100 = 0.002599489
                            else:
                                var100 = -0.07565029
                        else:
                            var100 = 0.13674815
                    else:
                        if input[3] < 0.45454916:
                            if input[0] < -1.5570326:
                                var100 = 0.011599693
                            else:
                                var100 = -0.081317976
                        else:
                            var100 = 0.030696994
                else:
                    if input[1] < -1.4636511:
                        if input[8] < 1.4017887:
                            if input[9] < 1.3985938:
                                var100 = 0.12022433
                            else:
                                var100 = -0.062107347
                        else:
                            var100 = -0.06679173
                    else:
                        if input[3] < -0.5225813:
                            if input[0] < 0.05038005:
                                var100 = -0.111073054
                            else:
                                var100 = -0.012988471
                        else:
                            if input[0] < -1.5570326:
                                var100 = 0.10420211
                            else:
                                var100 = -0.046931166
        else:
            var100 = 0.1399416
    else:
        if input[0] < -1.3962914:
            if input[3] < -0.5225813:
                if input[2] < -0.09404516:
                    if input[5] < -0.53826725:
                        var100 = 0.12134835
                    else:
                        if input[4] < -0.96460044:
                            var100 = 0.02889173
                        else:
                            if input[6] < -0.17227012:
                                var100 = -0.0017760555
                            else:
                                var100 = -0.0600938
                else:
                    if input[6] < -0.28860062:
                        var100 = -0.00470308
                    else:
                        if input[1] < -1.0000364:
                            var100 = -0.017521454
                        else:
                            var100 = -0.10598496
            else:
                if input[0] < -1.5570326:
                    var100 = 0.1166839
                else:
                    if input[1] < -0.47846985:
                        if input[5] < 0.31799382:
                            var100 = 0.07177929
                        else:
                            var100 = 0.018974502
                    else:
                        var100 = -0.029515317
        else:
            if input[2] < -1.1422349:
                if input[1] < -0.36256617:
                    if input[1] < -1.1159401:
                        if input[5] < -0.47182283:
                            var100 = 0.08677846
                        else:
                            if input[1] < -1.4636511:
                                var100 = 0.021424545
                            else:
                                var100 = -0.083719656
                    else:
                        var100 = 0.12176458
                else:
                    if input[6] < 1.5726874:
                        if input[11] < 1.2236042:
                            if input[5] < -0.53826725:
                                var100 = 0.078516774
                            else:
                                var100 = -0.055837072
                        else:
                            var100 = -0.09837492
                    else:
                        var100 = 0.058191862
            else:
                if input[6] < 0.17672138:
                    if input[3] < 0.45454916:
                        if input[6] < -0.17227012:
                            if input[1] < 1.1441816:
                                var100 = -0.030255087
                            else:
                                var100 = 0.02845158
                        else:
                            if input[5] < -0.53826725:
                                var100 = 0.091294475
                            else:
                                var100 = -0.023057338
                    else:
                        var100 = 0.05213416
                else:
                    if input[3] < 0.12883902:
                        if input[0] < 0.45223323:
                            if input[1] < -1.4636511:
                                var100 = -0.0068039256
                            else:
                                var100 = -0.06410173
                        else:
                            if input[0] < 0.6129745:
                                var100 = 0.06298565
                            else:
                                var100 = -0.044281896
                    else:
                        if input[0] < 0.13075069:
                            var100 = 0.07205054
                        else:
                            if input[5] < -0.53826725:
                                var100 = 0.042865314
                            else:
                                var100 = -0.048480067
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
