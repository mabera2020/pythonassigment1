import random
import datetime
sensors = []
cluster = []
filename = datetime.datetime.now()
filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# solution for problem 1
# dummy dataset  generate
for i in range(32):
    for j in range(16):
        cluster = random.uniform(0, 1)
        sensors.append(cluster)
# solution for problem 2
f = open("Sensors output " +filename1, "a")
f.write(str(sensors))
f.close()
# solution for problem 3
#Create a copy of a "corrupted" data set containing at least one entry where the value is "err"
courupt = [0.9183335248509713, 0.06370697264535341, 'err', 0.857489453763951, 0.4906892064121531, 4906892064121531, 0.4458665719248851, 0.33199732121360404, 0.13773350488224678, 0.6549212010120222, 0.5179277073582614, 0.6906801100495233, 0.029927630102307146, 0.3826723748249865, 0.7369499629631183, 0.3164368180508125, 0.9058198494991481, 0.28566615361628067, 0.5614508327889665, 0.3152218022966108, 0.6417928804688325, 0.22128167571143886, 0.983342658398711, 0.268168949020532, 0.22999715277126676, 0.19446267915111348, 0.1769318048474653, 0.7116851567872651, 0.27698285633519015, 0.7385850495345454, 0.37389641372874916, 0.5975879611763857, 0.8901770810935749, 0.006949106962234497, 0.1620893687843955, 0.5843629857265402, 0.5636188059994501, 0.3291224443820999, 0.7694701383870274, 0.1835898126022668, 0.627783513777405, 0.21303129420544553, 0.8110573169238319, 0.3864066587822991, 0.3213000435735771, 0.6089471910787265, 0.3176663358185463, 0.5992066719963952, 0.2687049632772516, 0.7350852033923664, 0.5629976679976202, 0.6772016879068536, 0.9571985272456913, 0.15237269210275828, 0.14834171271701724, 0.7629797843154957, 0.4654217090448495, 0.4191294183861506, 0.25441858891392954, 0.9524575081797638, 0.16678268404190333, 0.8536649958378805, 0.8610390169506154, 0.5740510288987882, 0.07131270261142397, 0.2799251638880299, 0.7899885858264765, 0.29066843956675825, 0.6389054386904972, 0.37802436043259247, 0.4745995458511656, 0.1579331513421347, 0.9420288778933684, 0.9940459407763144, 0.9519548274508876, 0.2431208666216863, 0.9268008328833987, 0.9190347657016015, 0.04228165129307948, 0.7544873254140912, 0.38144591491744995, 0.04911116203114563, 0.47364407821958554, 0.6800737886443553, 0.4476930575553095, 0.801791780069548, 0.986105645150965, 0.23534163183500267, 0.7309624827999828, 0.8683087816985501, 0.7824204721167034, 0.17696874227504478, 0.2528796990269032, 0.890562092043477, 0.45146481435432095, 0.0736303721036421, 0.36861831050909233, 0.14887739035152303, 0.5308084781602748, 0.19681484045558661, 0.8719181951522398, 0.3026516844873641, 0.21123859003218304, 0.963237673951113, 0.46443522888098, 0.019646552285333962, 0.15974131845401052, 0.8480092634299568, 0.14730523972558596, 0.752030734123025, 0.4586085344814219, 0.9607246826387159, 0.5644613318039485, 0.6405279399354908, 0.17273914273846225, 0.7061981364552677, 0.2522277090219578, 0.8831223214305337, 0.7650847315293973, 0.7488762072646057, 0.36864883171847074, 0.7265123078302741, 0.820215353985303, 0.9403963677195133, 0.3602711084463589, 0.1705849485383757, 0.5444963013508167, 0.8476312455103591, 0.30268931665249554, 0.5244032108283607, 0.26475712776759974, 0.7133257422492192, 0.5500282343001595, 0.7335336377705209, 0.4892638787374868, 0.8416699911610815, 0.7485010320601866, 0.8740252625613744, 0.7434546950513848, 0.061458666645173965, 0.9738007472534529, 0.003715219207785392, 0.9608798498295702, 0.6608308414401192, 0.8395776745789553, 0.9758748077136832, 0.3253164381393544, 0.9193126635147534, 0.4765075712679523, 0.3759699345886399, 0.07311823375594884, 0.3437001008589188, 0.36197444748571106, 0.8092092324780228, 0.4421007026237783, 0.3072035901546848, 0.4440973467841305, 0.21197194455376134, 0.070845592250953, 0.4932654892503574, 0.5345599615705918, 0.3700662245691153, 0.3833394103596466, 0.35687375091279094, 0.7945167328964323, 0.053549330354881186, 0.05390717553093893, 0.9026291158752469, 0.6803468616583506, 0.4982925153127511, 0.24611452341163265, 0.22005026525566784, 0.7984671833884629, 0.6086438678157235, 0.9812625214224728, 0.15398140801646465, 0.3986048714801894, 0.020502419539615513, 0.718551103576061, 0.3466994874647791, 0.644213553678267, 0.4678743674008202, 0.22532181197893775, 0.7903110578174385, 0.21709562863223952, 0.9569930043487824, 0.33200474797301016, 0.5306388057418406, 0.5449332069623436, 0.7955548666959296, 0.4685539238527794, 0.1949227492022897, 0.3094217010193894, 0.4715281360605913, 0.5710303614949331, 0.5042991413833959, 0.9467771157851766, 0.1536237050058048, 0.5402045923915387, 0.949169753827335, 0.9464259388660696, 0.9426624447538156, 0.26193673930439865, 0.03712649351026587, 0.41279190748427097, 0.5191793351239179, 0.10874280476598419, 0.13436711285404157, 0.6493438533635476, 0.7133943143118026, 0.07235506369075517, 0.707807324044315, 0.6951402204089799, 0.27017525547267374, 0.5053108329474848, 0.9765913751252866, 0.4378486383942203, 0.3800524281752734, 0.6757798173937593, 0.6557727428954538, 0.647495366200123, 0.21699189755595372, 0.9221510836874569, 0.35277412965854527, 0.42732735241056086, 0.782030999662808, 0.4562118858405204, 0.9294687689898555, 0.8235456757902584, 0.5922985937820128, 0.2938758898665115, 0.5996547858068315, 0.9568149061434695, 0.872053105301765, 0.5902360021189221, 0.21234392429133242, 0.9415217861737296, 0.6838743121087274, 0.8447230486961709, 0.1619755581300919, 0.7382617091223489, 0.723860128537826, 0.9461380386378341, 0.4953601157113874, 0.28409163959500683, 0.166445056681798, 0.4182192179999471, 0.054790568715726296, 0.6256408453471662, 0.08164463203700123, 0.2642090578927403, 0.9803729956120943, 0.23783289756724302, 0.8139785589112986, 0.753517737218952, 0.4735676789845522, 0.9212881793244456, 0.3583963304681915, 0.31589568058139017, 0.7301075721048521, 0.6931549843338433, 0.450619595787483, 0.09266058763725205, 0.4055813752565959, 0.5216720443384066, 0.6291497788416077, 0.9000617760447777, 0.6119278044295946, 0.51937993617818, 0.8254527908678028, 0.6490169779700129, 0.4333724397916304, 0.5761687738805634, 0.9214412263632775, 0.7724160545957903, 0.038536053599340314, 0.4131645911801308, 0.8982074724780101, 0.09910721195612315, 0.33719292389470734, 0.45615196490473897, 0.9355240706925342, 0.9677819543629488, 0.7523074676388136, 0.343403084756553, 0.9169344805608396, 0.5085272075194575, 0.4983422740128416, 0.28246458942434927, 0.7797902705527793, 0.3732638203339914, 0.6298835234983106, 0.9847458153889312, 0.9345913232426283, 0.21134483919008318, 0.24695497536275768, 0.7424158747108937, 0.6279109446028919, 0.7488022574212424, 0.21877050357378425, 0.6451029298458613, 0.26005422572643866, 0.0695565402874524, 0.5043927008703932, 0.09811467464953494, 0.9522845310158283, 0.22592724060035585, 0.09536932228787975, 0.7969478048443068, 0.9066652319174162, 0.6822150903674667, 0.07200304950318126, 0.40094469011002565, 0.2873592638231788, 0.9507315507761426, 0.9026804573828694, 0.19449124777078075, 0.3399722719808437, 0.7136408568505532, 0.1332199413101166, 0.7239618139249155, 0.30144896754402783, 0.5726552623750091, 0.590865890973548, 0.7303910678950735, 0.8507752679838275, 0.5627291800198979, 0.7232068900530993, 0.4766722773768223, 0.4727372345173223, 0.19695232719208544, 0.19022448539915715, 0.6368587774862219, 0.2215648117101625, 0.5034243703813558, 0.8341642733250667, 0.35334167274213113, 0.40887482114672247, 0.35407829269624314, 0.4295020290447059, 0.3955435150545501, 0.21307813070442438, 0.776379719817349, 0.07936541050019974, 0.8770697932069101, 0.38025404144529906, 0.1753578604272089, 0.2819786491957996, 0.7113026831543863, 0.1053449076031282, 0.8359212757966041, 0.4628206814043645, 0.6542677790310825, 0.7203174720406321, 0.3124575686091826, 0.9851494363712697, 0.8495969121887303, 0.2535019652643291, 0.214146751463814, 0.059107093520155196, 0.2178174137792942, 0.22094009417334137, 0.6360414543358122, 0.012404750742889159, 0.5076881164442926, 0.3576754650282775, 0.4579356045344103, 0.8636038486617802, 0.9364778482370907, 0.3123553409832509, 0.9144168319958678, 0.037342795138801566, 0.04385090898492139, 0.7304547191636295, 0.41654225393180344, 0.1257277079488731, 0.3658356324911941, 0.46809048528991126, 0.718428773204002, 0.8429805420086122, 0.27720870246587503, 0.5440862053811715, 0.13771031658869404, 0.7113747935558408, 0.10162791977373742, 0.1365763817949247, 0.8125558637426681, 0.23586637577053893, 0.9017483700904128, 0.4223397710508725, 0.7649716390669917, 0.33704688901732394, 0.2185251235876744, 0.29924876980196413, 0.7402086999199747, 0.46718923768539433, 0.07585691586714616, 0.956112026313118, 0.5119019715340771, 0.9949642268419125, 0.7689948688024542, 0.0643404698588923, 0.7902305154154667, 0.6540348315286386, 0.9534434313400387, 0.12261730453062825, 0.09493850222886391, 0.2514613584775768, 0.7971705221057636, 0.45811712502586455, 0.9138342812574786, 0.44201368179753, 0.8549511057250776, 0.2782001483473493, 0.35487395262932453, 0.05124003987331727, 0.09145709766479193, 0.5779815605681686, 0.872551623874122, 0.7534557835334289, 0.4233171309140662, 0.15473299423876408, 0.015361171720434386, 0.883186063611738, 0.9985578095580973, 0.5423630707124162, 0.904211024805427, 0.09591782512608749, 0.9812826969082084, 0.4851766073067133, 0.32547690029722154, 0.2753490486311523, 0.09172255263269591, 0.0033429343845188253, 0.6053829010340646, 0.46792510207837634, 0.7458726590151067, 0.46708790946683654, 0.652639779797187, 0.8574502919136621, 0.52455537440885, 0.8357765311502562, 0.22101698709154272, 0.6063715334664055, 0.9867409203529611, 0.02012042164485106, 0.33291895603206456, 0.17914198649344226, 0.9485434979991745, 0.9881546099473252, 0.7332390597995143, 0.5130603730661079, 0.09709482841857942, 0.4107451346948069, 0.2269070266161224, 0.5531305374413895, 0.15389700855652966, 0.7182515607248046, 0.5004496907298623, 0.18016005044088235, 0.9371850443246519, 0.7699200438545191, 0.9471770205318708, 0.6768352158294354, 0.2332256320099817, 0.8740144430480444, 0.15634667078944786, 0.14127766367770578, 0.184026787321938, 0.11302197074167919, 0.637630157925993, 0.8891615267029523, 0.9697807078266136, 0.11326229515821429, 0.4501596771111429, 0.3530259225641572, 0.8027925612209271, 0.9508530432762923, 0.32501958398290864, 0.34644564911632525, 0.5561436991248647, 0.7037852577175073, 0.8914608782926923, 0.7341094283023871, 0.25422941670593036, 0.3248824398428257, 0.49377138146436006, 0.9845482443183402, 0.6155875049287955, 0.09406642522705888, 0.07960587076041281, 0.5173249276829739, 0.9094176939387228, 0.6982495931217249, 0.8922465565244997, 0.9918497971106345, 0.8321868322212137, 0.04124169437142566, 0.1513169566666671, 0.4144970417276105, 0.22420745278205545, 0.6993870700259532, 0.5655478953625753, 0.6623952604528146, 0.34194856123327766, 0.41445296121588704, 0.2149336676452459, 0.29729797807821146, 0.9018472241628932, 0.8354808507819762, 0.024109593843354205, 0.08941051094374464]
def err_check():
    for i in courupt:
        if i == "err":
           m = open("Error "+filename1,"a")
           m.write("Error detected")
           m.close()

err_check()
