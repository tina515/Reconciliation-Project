import math
import seaborn as sns
import pandas as pd
import matplotlib.colors as mcolors
def average_and_stddev_of_odd_index_items(input_list):
    # Initialize variables to store the sum and count of odd-indexed items
    odd_sum = 0
    odd_count = 0

    # Iterate through the list using a for loop
    for i in range(1, len(input_list), 2):
        odd_sum += input_list[i]  # Add the item at the odd index to the sum
        odd_count += 1  # Increment the count

    # Calculate the average of odd-indexed items
    if odd_count > 0:
        average = odd_sum / odd_count

        # Calculate the standard deviation of odd-indexed items
        stddev_sum = 0
        for i in range(1, len(input_list), 2):
            stddev_sum += (input_list[i] - average) ** 2
        stddev = math.sqrt(stddev_sum / odd_count)

        return average, stddev
    else:
        return None, None


def average_and_stddev_of_even_index_items(input_list):
    # Initialize variables to store the sum and count of odd-indexed items
    odd_sum = 0
    odd_count = 0

    # Iterate through the list using a for loop
    for i in range(0, len(input_list), 2):
        odd_sum += input_list[i][0]
        odd_sum += input_list[i][1]# Add the item at the odd index to the sum
        odd_count += 2  # Increment the count

    # Calculate the average of odd-indexed items
    if odd_count > 0:
        average = odd_sum / odd_count

        # Calculate the standard deviation of odd-indexed items
        stddev_sum = 0
        for i in range(0, len(input_list), 2):
            stddev_sum += (input_list[i][0] - average) ** 2
            stddev_sum += (input_list[i][1] - average) ** 2
        stddev = math.sqrt(stddev_sum / odd_count)

        return average, stddev
    else:
        return None, None
#logistic regression
my_list = [[0.1138980301352039, 0.1143942164223994], 0.031693384927215774, [0.11490150406627266, 0.1145683223720718], 0.02671826054910632, [0.11637476449870804, 0.11651546901246793], 0.024599226091763404, [0.11768834674576863, 0.11726375415680518], 0.026810392482034272, [0.11364958707513748, 0.1138209525344662], 0.026165468951538602, [0.11681017276035123, 0.11822069757271066], 0.0244149622259075, [0.11742411918169449, 0.11534859767680196], 0.025336281555187027, [0.11828087087842185, 0.11983719499952467], 0.028100239543025613, [0.11750895752049509, 0.11896425146186154], 0.02892942693937719, [0.116626710235954, 0.11638936973577114], 0.035747189976045694, [0.11721546994978417, 0.11658354953095947], 0.024322830292979547, [0.11435170764929854, 0.11487571958594575], 0.022572323567348444, [0.11279266117731826, 0.11265761490663043], 0.019992629445365763, [0.11270496934149085, 0.11345467733612945], 0.02211166390270868, [0.11630811535516375, 0.11609793410521677], 0.024599226091763404, [0.11656551973046979, 0.11729657205942393], 0.03021927400036853, [0.11409362693131325, 0.11321478364668956], 0.02957435046987286, [0.1146726688916487, 0.11662802294577652], 0.024507094158835452, [0.11308788576249008, 0.11389848118686627], 0.025612677353970888, [0.11311303085512305, 0.11316344885112031], 0.027639579878385848, [0.11481471082488633, 0.11707470321350734], 0.02155887230514096, [0.11371877692101834, 0.11533241050730483], 0.027639579878385848, [0.11489589629562143, 0.11626055546132971], 0.029482218536944906, [0.11216298829805958, 0.11337547716609754], 0.029113690805233093, [0.11682268997468015, 0.1163272865914187], 0.026902524414962225, [0.11527805665471863, 0.1148412091285511], 0.02340151096370002, [0.11387499941604741, 0.1135080630351305], 0.03141698912843192, [0.11571435934677211, 0.11447915002699836], 0.022019531969780726, [0.11417367367532792, 0.11470871377331535], 0.02791597567716971, [0.11522988281724045, 0.11550677838966283], 0.029113690805233093]
# my_list = [[0.11199323356894754, 0.11201703135937718], 0.000552791597567717, [0.1152881937183627, 0.11507600379275036], 0.000552791597567717, [0.11457101992073518, 0.11449019513883152], 0.0018426386585590566, [0.11517184373463533, 0.11511722706535249], 0.0003685277317118113, [0.11660835569362295, 0.11696033545036175], 0.0006449235304956698, [0.11397206369493769, 0.11356580384066786], 0.001013451262207481, [0.11524179422824735, 0.11509082353981445], 0.00018426386585590566, [0.11577857009376978, 0.11546597673178632], 0.000552791597567717, [0.11541750377775245, 0.11540976952206282], 0.0006449235304956698, [0.1147871038309161, 0.1146721463500942], 0.000552791597567717, [0.11442186762383265, 0.1138909162162273], 0.0006449235304956698, [0.11516955999689904, 0.11482545277180518], 0.001013451262207481, [0.11461367286062184, 0.11441893787184476], 0.0014741109268472453, [0.11521851944167935, 0.11555747031499429], 0.0011977151280633867, [0.11514951914806154, 0.11503319307172298], 0.0006449235304956698, [0.11591242320864888, 0.11591513891223228], 0.0003685277317118113, [0.11410023632015669, 0.11443161804237457], 0.000552791597567717, [0.11431359247595708, 0.11440253187029756], 0.0, [0.1166311720549789, 0.11653704067697278], 0.0015662428597751981, [0.11513322073367642, 0.11536633480232505], 0.0015662428597751981, [0.11579090707539356, 0.11568115752011258], 0.0003685277317118113, [0.11603270170192345, 0.1157896446247344], 0.0007370554634236226, [0.11624149769563644, 0.11645283674329121], 0.0002763957987838585, [0.11705462427832398, 0.11712018973226504], 0.0007370554634236226, [0.11408484315214508, 0.11402028428735245], 0.0003685277317118113, [0.11462828875892368, 0.11433212054824313], 0.0007370554634236226, [0.11401718850833244, 0.11365037862056165], 0.0008291873963515755, [0.11532026035616326, 0.11537703516881641], 0.00018426386585590566, [0.11367337643018746, 0.11392035083396358], 0.0009213193292795283, [0.11333462698375095, 0.11320790888915026], 0.0003685277317118113]
#random foreest
# my_list = [[0.13432219487105734, 0.13421934843481498], 0.005804311774461028, [0.13281389953503017, 0.13297155776284222], 0.0013819789939192924, [0.13468038693994472, 0.1344225763249391], 0.002119034457342915, [0.12995581392840735, 0.12955117529345705], 0.005435784042749217, [0.12869002029777676, 0.12851281056984717], 0.0028560899207665377, [0.12884786336753173, 0.12873377399358496], 0.005712179841533075, [0.13483292818340883, 0.13484296822727887], 0.0031324857195503962, [0.13051176215801713, 0.13043491660051412], 0.004053805048829924, [0.12888274447743794, 0.1289648914288499], 0.014741109268472453, [0.13153028886946577, 0.13170529153693916], 0.007002026902524415, [0.130200339012371, 0.13043071048442056], 0.00552791597567717, [0.1307089648981445, 0.13073610271062697], 0.0028560899207665377, [0.13192392488641674, 0.13149633166196928], 0.002763957987838585, [0.1314984938538952, 0.13154282669350253], 0.0068177630366685095, [0.13119120771513867, 0.1313458716304281], 0.0029482218536944905, [0.12947675759760285, 0.12926259888962643], 0.008844665561083471, [0.13100699545011896, 0.13130733527094662], 0.005159388243965358, [0.13049022178768588, 0.13043589957345458], 0.0035931453841901604, [0.1307628267400897, 0.1302122074128966], 0.0034088815183342547, [0.13138492696599852, 0.13117872734442532], 0.003869541182974019, [0.12723248039894464, 0.1272188657507251], 0.005620047908605122, [0.13172247944842164, 0.13134347368556115], 0.002119034457342915, [0.12766979915819687, 0.12752744203436833], 0.0031324857195503962, [0.1302595916461105, 0.12969747871875767], 0.004790860512253547, [0.13186054953582982, 0.1318807068696123], 0.005804311774461028, [0.12947211550790164, 0.13007125579804577], 0.019163442049014188, [0.13247153939369286, 0.13229469536797864], 0.005804311774461028, [0.1311233246955384, 0.1309729224735362], 0.005159388243965358, [0.128783901953921, 0.1288400841185683], 0.006633499170812604, [0.1296926807943182, 0.12927511524552343], 0.011332227750138198]
#gradientBoosting
# my_list = [[0.1135757193835453, 0.11360190864656004], 9.213193292795283e-05, [0.11268906324978728, 0.11270598949905798], 0.0, [0.11518823342268675, 0.11513808910743105], 0.00018426386585590566, [0.11165890383743468, 0.11165890383743468], 0.0, [0.1149394021887055, 0.11490558443502957], 9.213193292795283e-05, [0.11572795451588241, 0.11572883862877445], 0.0, [0.11228458666538313, 0.11229280036338739], 0.0, [0.11288505048940224, 0.11288765567613453], 0.0, [0.11336578252921886, 0.11335987976879461], 0.0, [0.11399161081068558, 0.11400482274553209], 0.0, [0.11339403812222294, 0.11339470713817054], 0.0, [0.11521566184056047, 0.11521750475868962], 0.0, [0.11668324866590772, 0.11668642000349382], 0.0, [0.11303154672928195, 0.11303261188970211], 0.0, [0.1156590193258862, 0.1156590193258862], 0.0, [0.11580656772917387, 0.11578975977957785], 9.213193292795283e-05, [0.11533916935288416, 0.11533916935288416], 0.0, [0.11500596822646288, 0.11505721801059536], 0.0, [0.11364311831291093, 0.1136419966121765], 0.0, [0.11160722579952678, 0.11160883333860974], 0.0, [0.11351248201403125, 0.11351046538206441], 0.0, [0.11469940493070316, 0.11470254615750113], 0.0, [0.11549429123259784, 0.11549429123259784], 0.0, [0.11628993782178067, 0.11628993782178067], 0.0, [0.1128830425574511, 0.11287525974120097], 0.0, [0.11478872666003899, 0.11480475619660878], 9.213193292795283e-05, [0.11539050240115638, 0.11538356160431339], 0.0, [0.11511516956867517, 0.11511267009231607], 0.0, [0.1123744056416138, 0.11237505521152076], 0.0, [0.11260869178247092, 0.11260568822089943], 0.0]
#community linear
# my_list= [[0.020970255669584957, 0.02221572225701174], 0.01804511278195489, [0.023943491504755558, 0.023875144188880586], 0.02406015037593985, [0.022479251339250585, 0.021866584448019432], 0.01804511278195489, [0.020633917796725, 0.020787117065402316], 0.02556390977443609, [0.02255004274656093, 0.020892768513384435], 0.009022556390977444, [0.02089328430934373, 0.020677250032713305], 0.01804511278195489, [0.020978827442126032, 0.021657126736236626], 0.02406015037593985, [0.021333981780250633, 0.01946300986864418], 0.01804511278195489, [0.022014346721662574, 0.023314928326121552], 0.03759398496240601, [0.01937999734899045, 0.018982178115052935], 0.03308270676691729, [0.01914056697764458, 0.01968854135859043], 0.015037593984962405, [0.020589804746091504, 0.021898972124525566], 0.03609022556390978, [0.021030504231785367, 0.01973143179576136], 0.03609022556390978, [0.020817074121775418, 0.020360879455950075], 0.016541353383458645, [0.020822484328922152, 0.019602699935062445], 0.039097744360902256, [0.01879092333754959, 0.019445655280750627], 0.04360902255639098, [0.019561163179138363, 0.021430136695984977], 0.02556390977443609, [0.020105192933474413, 0.018564316249007177], 0.019548872180451128, [0.019195291196558627, 0.018892286447949252], 0.013533834586466165, [0.022638199560302066, 0.022523454649942], 0.02857142857142857, [0.01996065020420491, 0.020660535141213663], 0.022556390977443608, [0.019857396941686006, 0.019492246999225332], 0.03609022556390978, [0.01900072413556751, 0.019948780788496285], 0.03007518796992481, [0.021699417837250976, 0.02149375050832869], 0.012030075187969926, [0.022723634512445124, 0.020931695737526325], 0.042105263157894736, [0.01993229620309353, 0.020679976023882864], 0.039097744360902256, [0.02267943863857396, 0.023900014865186583], 0.022556390977443608, [0.020652933856820602, 0.019188185143087698], 0.02556390977443609, [0.022259937889721138, 0.01935478166885441], 0.03007518796992481, [0.02273582669204629, 0.021438733724202737], 0.03609022556390978]


#

def func(a,b):
    multiplier = (16 / (0.05 * pow(0.2, 2)))
    return round(a - b * (1 / multiplier), 3)
import matplotlib.pyplot as plt
import numpy as np

data_initial = {
    'Dummy Classifier' : [0.5,0.0,0.65,0.015, 0.5,0.0],
    'Disjoint training: logistic/linear regression':[np.nan,np.nan,0.05, 0.027,0.05, 0.016],
    'Disjoint training: Tree':[0.2,0.0,0.24,0.038, 0.24,0.0],
    'Disjoint training: KNN':[0.151,0.0,0.05,0.027,0.3,0.0],
    'Disjoint features: logistic/linear regression':[0.09,0.0,0.1,0.38, np.nan, np.nan],
    'Disjoint features: Tree':[0.08,0.0,0.3,0.023, np.nan, np.nan],
    'Disjoint features: KNN':[0.24, 0.0,0.17,0.033, np.nan, np.nan],
    'Different classifiers: logistic/linear + Tree':[0.16, 0.0,0.15,0.017, 0.2,0.0],
    'Different classifiers: logistic/linear + KNN':[0.12,0.0,np.nan,np.nan,0.21,0.0],
    'Different classifiers: KNN + Tree':[0.17,0.0,0.14,0.043,0.15,0.0],
}
methods = ['Adult Before Reconcile', 'Adult After Reconcile', 'Community Before Reconcile',
           'Community After Reconcile','Compas Before Reconcile', 'Compas After Reconcile']

df = pd.DataFrame(data_initial, index=methods)

# cmap = plt.get_cmap('Blues')
colors = ["#D6EAF8", "#3498DB", "#1B4F72"]  # Light to dark
cmap = mcolors.LinearSegmentedColormap.from_list("mycmap", colors)
cmap.set_bad('black')
sns.heatmap(df, annot=True, cmap=cmap, fmt=".2f")
plt.subplots_adjust(left=0.2, right=0.9, top= 0.97)
plt.xticks(rotation=20, ha='right')
plt.show()
# plt.title('Model Performance Heatmap')