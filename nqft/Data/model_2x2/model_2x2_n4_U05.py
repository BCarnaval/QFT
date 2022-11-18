from pyqcm import *
new_cluster_model('clus', 4, 0, generators=None, bath_irrep=False)
add_cluster('clus', [0, 0, 0], [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]], ref = 0)
lattice_model('model_2x2_n4_U05', [[2, 0, 0], [0, 2, 0]], None)
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
set_target_sectors(['R0:N4:S0'])
set_parameters("""

                U = 0.5
                t = 1.0
                tp = -0.3
                tpp = 0.2
                mu = 4.0
                """)
set_parameter("U", 0.5)
set_parameter("mu", 4.0)
set_parameter("t", 1.0)
set_parameter("tp", -0.3)
set_parameter("tpp", 0.2)

new_model_instance(0)

solution=[None]*1

#--------------------- cluster no 1 -----------------
solution[0] = """
U	0.5
mu	4
t	1
tp	-0.3

GS_energy: -19.649 GS_sector: R0:N4:S0:1
GF_format: bl
mixing	0
state
R0:N4:S0	-19.649	1
w	4	28
-4.1836464558599	-0.49901596671032	0.0081840411677315	-0.008184041167732	0.49901596671032
-4.1836464558599	0.0081840411677351	0.49901596671045	-0.49901596671045	-0.0081840411677326
-5.4629857854386	-0.49929167249971	-0.49929167249971	-0.49929167249972	-0.49929167249971
-5.7115281129503	-0.025474206075334	0.025474206075412	0.025474206075413	-0.025474206075334
-6.9784757948047	-0.023703254111442	0.0034382315775515	-0.0034382315775511	0.023703254111443
-6.9784757948047	0.0034382315775521	0.023703254111448	-0.023703254111449	-0.0034382315775523
-8.3228356211019	0.00030874743955066	-0.017920279573915	0.017920279573914	-0.00030874743955183
-8.3228356211019	-0.017920279573916	-0.00030874743955102	0.00030874743955152	0.017920279573917
-8.3482237097212	-0.0045685062459015	0.00056277603946187	-0.00056277603946197	0.0045685062459015
-8.3482237097212	0.00056277603946192	0.0045685062459038	-0.0045685062459043	-0.00056277603946255
-9.4864453305857	-0.007666233824016	0.0076662338240144	0.0076662338240151	-0.007666233824016
-9.7349876580974	-0.00034562439955797	-0.00034562439955666	-0.00034562439955739	-0.00034562439955847
-12.211752027352	-3.1960924419984e-05	-3.7062188012319e-06	3.7062188010966e-06	3.1960924419864e-05
-12.211752027352	3.7062188011873e-06	-3.1960924420357e-05	3.1960924420301e-05	-3.7062188012351e-06
-3.913722836212	0.0081283558661179	0.49938766894589	-0.49938766894589	-0.0081283558661163
-3.913722836212	-0.49938766894602	0.0081283558661201	-0.0081283558661185	0.49938766894602
-1.4370142145614	0.49929167249971	-0.49929167249971	-0.49929167249971	0.49929167249971
-1.1884718870497	0.025474206075405	0.025474206075339	0.02547420607534	0.025474206075408
0.19317272458839	-0.014994640200645	0.0073009590744318	-0.0073009590744315	0.014994640200645
0.19317272458839	0.0073009590744315	0.014994640200648	-0.014994640200646	-0.0073009590744341
0.22609875954933	0.0053942440030806	0.011664084856494	-0.011664084856494	-0.0053942440030814
0.22609875954933	-0.011664084856497	0.0053942440030821	-0.0053942440030828	0.011664084856497
1.3251609851569	0.0004099667104239	0.010119902131822	-0.010119902131822	-0.00040996671042393
1.3251609851569	-0.010119902131826	0.00040996671042448	-0.00040996671042362	0.010119902131825
2.5864453305857	0.0076662338240149	0.0076662338240158	0.0076662338240157	0.0076662338240151
2.8349876580974	0.00034562439955672	-0.00034562439955759	-0.00034562439955809	0.00034562439955633
4.1142239757572	-0.00011234879167824	2.8973550993131e-05	-2.8973550993008e-05	0.00011234879167801
4.1142239757572	2.8973550993239e-05	0.00011234879167835	-0.0001123487916786	-2.8973550993083e-05

"""
read_cluster_model_instance(solution[0], 0)
