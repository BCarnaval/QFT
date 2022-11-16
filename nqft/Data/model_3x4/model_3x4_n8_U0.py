from pyqcm import *
new_cluster_model('clus', 12, 0, generators=None, bath_irrep=False)
add_cluster('clus', [0, 0, 0], [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0]], ref = 0)
lattice_model('model_3x4_n8_U0', [[4, 0, 0], [1, 3, 0]], None)
interaction_operator('U', band1=1, band2=1)
hopping_operator('t', [1, 0, 0], -1, band1=1, band2=1)
hopping_operator('t', [0, 1, 0], -1, band1=1, band2=1)
hopping_operator('tp', [1, 1, 0], -1, band1=1, band2=1)
hopping_operator('tp', [-1, 1, 0], -1, band1=1, band2=1)
hopping_operator('tpp', [2, 0, 0], -1, band1=1, band2=1)
hopping_operator('tpp', [0, 2, 0], -1, band1=1, band2=1)

try:
    import model_extra
except:
    pass
set_target_sectors(['R0:N8:S0'])
set_parameters("""

                U = 0.0
                t = 1.0
                tp = -0.3
                tpp = 0.2
                mu = 0.000000001
                """)
set_parameter("U", 0.0)
set_parameter("mu", 1e-09)
set_parameter("t", 1.0)
set_parameter("tp", -0.3)
set_parameter("tpp", 0.2)

new_model_instance(0)

solution=[None]*1

#--------------------- cluster no 1 -----------------
solution[0] = """
mu	1e-09
t	1
tp	-0.3
tpp	0.2

GS_energy: -18.1628 GS_sector: uncorrelated
GF_format: bl
mixing	0
state
R0	-18.1628	1
w	12	12
-2.6363301834896	-0.21472401243673	-0.30962975265518	-0.30962975265518	-0.21472401243673	-0.26594515691225	-0.38120755897862	-0.38120755897862	-0.26594515691225	-0.21472401243673	-0.30962975265518	-0.30962975265518	-0.21472401243673
-1.7039919419221	0.33013646811128	0.16361478648922	-0.16361478648922	-0.33013646811128	0.42892088050987	0.21096707419127	-0.21096707419127	-0.42892088050987	0.33013646811128	0.16361478648922	-0.16361478648922	-0.33013646811128
-1.600000001	-0.27735009811261	-0.41602514716892	-0.41602514716892	-0.27735009811261	0	0	0	0	0.27735009811261	0.41602514716892	0.41602514716892	0.27735009811261
-1.1646603273208	0.17455907264001	0.27869993440907	0.27869993440907	0.17455907264001	-0.29841116736448	-0.44120486016255	-0.44120486016255	-0.29841116736448	0.17455907264001	0.27869993440907	0.27869993440907	0.17455907264001
-0.97759030613878	-0.30168601000139	0.20325070201565	0.20325070201565	-0.30168601000139	-0.39327341914507	0.28405179948931	0.28405179948931	-0.39327341914507	-0.30168601000139	0.20325070201565	0.20325070201565	-0.30168601000139
-0.75541300863338	-0.15932295848261	0.32498761668473	-0.32498761668473	0.15932295848261	-0.21747080830212	0.43669776200511	-0.43669776200512	0.21747080830212	-0.15932295848261	0.32498761668473	-0.32498761668473	0.15932295848261
-0.24339811420566	-0.43732124062341	-0.24238426619647	0.24238426619647	0.43732124062341	0	0	0	0	0.43732124062341	0.24238426619647	-0.24238426619647	-0.43732124062341
0.61436181022307	-0.2932604848525	-0.16788391952686	0.16788391952686	0.2932604848525	0.45132088771475	0.26064537496207	-0.26064537496207	-0.45132088771475	-0.2932604848525	-0.16788391952686	0.16788391952686	0.2932604848525
0.999999999	-0.41602514716892	0.27735009811261	0.27735009811261	-0.41602514716892	0	0	0	0	0.41602514716892	-0.27735009811261	-0.27735009811261	0.41602514716892
1.6433981122057	-0.24238426619647	0.43732124062341	-0.43732124062341	0.24238426619647	0	0	0	0	0.24238426619647	-0.43732124062341	0.43732124062341	-0.24238426619647
2.3785808129492	0.28706842391941	-0.1874697707931	-0.1874697707931	0.28706842391941	-0.43076671935171	0.28166228635262	0.28166228635262	-0.43076671935171	0.28706842391941	-0.1874697707931	-0.1874697707931	0.28706842391941
3.4450431363325	-0.17211738827739	0.29904554871786	-0.29904554871786	0.17211738827739	0.25503486450176	-0.44368000493349	0.44368000493349	-0.25503486450176	-0.17211738827739	0.29904554871785	-0.29904554871786	0.17211738827739

"""
read_cluster_model_instance(solution[0], 0)
