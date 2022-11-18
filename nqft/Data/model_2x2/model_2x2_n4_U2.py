from pyqcm import *
new_cluster_model('clus', 4, 0, generators=None, bath_irrep=False)
add_cluster('clus', [0, 0, 0], [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]], ref = 0)
lattice_model('model_2x2_n4_U2', [[2, 0, 0], [1, 2, 0]], None)
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

                U = 2.0
                t = 1.0
                tp = -0.3
                tpp = 0.2
                mu = 0.0
                """)
set_parameter("U", 2.0)
set_parameter("mu", 0.0)
set_parameter("t", 1.0)
set_parameter("tp", -0.3)
set_parameter("tpp", 0.2)

new_model_instance(0)

solution=[None]*1

#--------------------- cluster no 1 -----------------
solution[0] = """
U	2
t	1
tp	-0.3

GS_energy: -2.82843 GS_sector: R0:N4:S0:1
GF_format: bl
mixing	0
state
R0:N4:S0	-2.82843	1
w	4	28
0.10655103060966	-0.15843959394976	-0.46148282016245	0.46148282016245	0.15843959394976
0.10655103060966	-0.46148282016245	0.15843959394976	-0.15843959394976	0.46148282016245
-0.8826758136816	-0.49162825282993	-0.49162825282993	-0.49162825282993	-0.49162825282993
-1.7963763171773	0.08796841614253	-0.087968416142531	-0.08796841614253	0.08796841614253
-2.6980034913655	0.035780382851293	-0.094763452441163	0.094763452441163	-0.035780382851294
-2.6980034913655	-0.094763452441163	-0.035780382851293	0.035780382851293	0.094763452441163
-4.6348026490034	-0.038597840043757	0.011210452333527	-0.011210452333527	0.038597840043757
-4.6348026490034	0.011210452333527	0.038597840043757	-0.038597840043757	-0.011210452333527
-4.8894436268962	-0.0073391967944024	-0.00089587045375107	0.00089587045375117	0.0073391967944022
-4.8894436268962	0.00089587045375118	-0.0073391967944027	0.0073391967944025	-0.00089587045375113
-5.2604779323151	0.023571066064836	-0.023571066064836	-0.023571066064836	0.023571066064836
-6.1741784358108	0.0027610913295534	0.0027610913295533	0.0027610913295537	0.0027610913295536
-8.3264368870756	1.041659510578e-05	-0.00014159402363701	0.00014159402363692	-1.0416595105786e-05
-8.3264368870756	-0.00014159402363732	-1.0416595105827e-05	1.0416595105786e-05	0.00014159402363726
1.3334939683068	-0.44963421592638	0.20404048470388	-0.20404048470388	0.44963421592638
1.3334939683068	0.20404048470388	0.44963421592638	-0.44963421592638	-0.20404048470388
3.4826758136816	-0.49162825282993	0.49162825282993	0.49162825282993	-0.49162825282993
4.3963763171773	0.08796841614253	0.087968416142531	0.087968416142531	0.08796841614253
5.5158375022646	-0.051489525376182	0.051489525376182	-0.051489525376182	0.051489525376182
5.5158375022646	0.051489525376182	0.051489525376182	-0.051489525376182	-0.051489525376182
6.0784351825985	-0.0022728503150348	-0.025254911655876	0.025254911655876	0.0022728503150355
6.0784351825985	-0.025254911655876	0.0022728503150352	-0.0022728503150351	0.025254911655876
7.1562945789201	-0.015618814437205	0.0021208436205398	-0.0021208436205398	0.015618814437205
7.1562945789201	0.0021208436205398	0.015618814437205	-0.015618814437205	-0.0021208436205399
7.8604779323151	-0.023571066064836	-0.023571066064836	-0.023571066064836	-0.023571066064836
8.7741784358108	-0.0027610913295536	0.0027610913295537	0.0027610913295536	-0.0027610913295535
9.7580743916409	-0.0016021406549299	-0.00047054764203021	0.00047054764203016	0.00160214065493
9.7580743916409	0.0004705476420302	-0.0016021406549301	0.0016021406549303	-0.00047054764203029

"""
read_cluster_model_instance(solution[0], 0)
