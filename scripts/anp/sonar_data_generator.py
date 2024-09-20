import numpy as np

class SonarDataGenerator:
    def __init__(self, P_W, R_SW, t_S, theta_noise=0.0005, d_noise=0.0002):
        self.P_W = P_W
        self.R_SW = R_SW
        self.t_S = t_S
        self.theta_noise = theta_noise
        self.d_noise = d_noise
        self.n = P_W.shape[1]

    def generate_data(self):
        P_S = np.zeros((3, self.n))
        P_SI = np.zeros((2, self.n))
        P_SI_Noise = np.zeros((2, self.n))

        for i in range(self.n):
            # P_S[:, i] = self.R_SW @ self.P_W[:, i] + self.t_S
            P_S[:, i] = self.R_SW @ (self.P_W[:, i] - self.t_S)
            d = np.linalg.norm(P_S[:, i])
            tan_theta = P_S[1, i] / P_S[0, i]
            theta = np.arctan(tan_theta)
            P_SI[0, i] = d * np.cos(theta)
            P_SI[1, i] = d * np.sin(theta)
            
            tan_theta_noise = tan_theta + np.random.normal(0, self.theta_noise)
            theta_noise = np.arctan(tan_theta_noise)
            d_noise = d + np.random.normal(0, self.d_noise)
            P_SI_Noise[0, i] = d_noise * np.cos(theta_noise)
            P_SI_Noise[1, i] = d_noise * np.sin(theta_noise)
        
        return P_S, P_SI, P_SI_Noise

# {'position': {'x': -1.9911273634093725, 'y': 0.13173626125675536, 'z': -0.4955636817046862}, 'orientation': {'x': -0.09976494819535225, 'y': -0.0033706835545049877, 'z': -0.09976494819535225, 'w': 0.989991186180732}}
pose = np.array([[ 0.98007119,  0.19820539,  0.0132322 , -1.99112736],
       [-0.19686029,  0.96018782,  0.19820539,  0.13173626],
       [ 0.02657998, -0.19686029,  0.98007119, -0.49556368],
       [ 0.        ,  0.        ,  0.        ,  1.        ]])
sonar_position=np.array([-0.07827157, -0.35747939,  0.46086422])
P_W = np.array([[ 4.01398693,  3.32507861,  0.00793917],
                [ 4.14420807,  2.98633423,  0.11863106],
                [ 4.32659229,  0.36589002,  0.20218476],
                [ 3.57898031,  1.76739533,  0.45847291],
                [ 4.62524004,  3.40097916,  0.4032435 ],
                [ 2.53439912,  1.94232965,  0.06235353],
                [ 2.37290791,  1.42191891,  0.34978184],
                [ 2.92203137, -0.59761111, -0.11087785],
                [ 4.74740917, -0.97792378, -0.38486538],
                [ 4.4339805 ,  2.89282256,  0.49727416],
                [ 4.65539456, -1.10248539, -0.50759619],
                [ 2.69388094, -0.27824162, -0.37549141],
                [ 5.05178386, -0.71949274, -0.51327746],
                [ 2.2541195 ,  0.4283563 ,  0.37311051],
                [ 2.8000855 ,  2.29046146,  0.11160917],
                [ 4.553101  ,  1.71617653,  0.14894067],
                [ 4.0377846 ,  0.45081748,  0.4736446 ],
                [ 3.54886843, -0.02527929, -0.13407187],
                [ 3.15894055, -0.57252434,  0.36255587],
                [ 3.86783644, -0.10329507,  0.45950438],
                [ 3.225728  ,  2.70341004,  0.50665149],
                [ 4.81897145, -0.19826834, -0.10995821],
                [ 2.97160881, -0.45016959,  0.20389852],
                [ 2.66377559,  0.11943769,  0.42015753],
                [ 4.14797142,  1.48413903, -0.28143116],
                [ 5.04479198, -0.38693323, -0.17127721],
                [ 4.91589477,  0.03323147, -0.17202155],
                [ 3.80825367, -0.87652375, -0.28689548],
                [ 2.33517812,  2.02522025, -0.04151965]])
#########################


sp = np.array([[ 4.5973495 ,  4.65272402,  4.32333326,  3.86648957,  5.20234448,
         2.86875486,  2.6128153 ,  2.74805788,  4.45827376,  4.9187137 ,
         4.34321738,  2.59186472,  4.80999746,  2.3241905 ,  3.19650768,
         4.80195802,  4.08190743,  3.47351726,  3.0360147 ,  3.81976354,
         3.6975363 ,  4.68556971,  2.85026187,  2.67946572,  4.37597224,
         4.86903315,  4.82508217,  3.55840043,  2.69556671],
       [ 2.45615134,  2.11160725, -0.45049368,  1.09235621,  2.46124398,
         1.40355152,  0.97369854, -1.16442181, -1.94065586,  2.02043128,
        -2.06936928, -0.87042745, -1.77920438,  0.04351778,  1.69749455,
         0.79960808, -0.26327138, -0.74010765, -1.10487602, -0.76901194,
         2.07332295, -1.14861809, -0.97503511, -0.3270498 ,  0.58172675,
        -1.3861802 , -0.95671267, -1.64048325,  1.5133466 ]])

if __name__ == "__main__":
    # 初始化参数
    # P_W = np.array([[30, 41, 21, 13, 23, 73, 35, 66, 72, 82, 15],
    #                 [44, 26, 63, 34, 15, 22, 14, 33, 25, 23, 42],
    #                 [35, 17, 16, 57, 54, 61, 42, 11, 13, 3, 47]])
    
    # R_SW = np.array( [[0.689673028293550, 0.423447870703166, 0.587403621746887],
    #                   [0.176155229057263, 0.688715772969376, -0.703306419236294],
    #                   [-0.702367745073895, 0.588525687510876, 0.400396136119796]])
    
    # t_S = np.array([6, 4, 8])
    
    # # 模拟生成 P_SI 和 P_SI_Noise 数据
    # data_generator = SonarDataGenerator(P_W, R_SW, t_S, Var_Noise=0.1)
    # P_S, P_SI, P_SI_Noise = data_generator.generate_data()
    
    # 初始化参数
    P_W = np.array([[ 1.06468565,  2.31759309,  0.35106129,  3.633026  , -0.30355716,
        -1.99571699, -0.17747571,  1.88155627, -1.5290993 , -1.72765435,
         3.16261278,  4.63730969,  2.74471633,  3.97951076, -0.14802812,
         4.43218987,  4.04127959, -0.26189836,  0.912736  ,  2.6847464 ,
         0.3559706 , -0.81076358, -0.25064624, -1.85310636,  0.4857652 ,
         2.9175314 ,  2.15640638, -0.71552746,  3.78229859, -0.26303752,
         2.40594241,  2.68300674, -2.03231184,  0.5881672 ,  0.17541774],
       [ 2.15335171,  2.22427009,  0.13722424,  1.62571457,  2.30703358,
         1.62333665,  2.5212474 ,  2.93972395,  0.29379445,  0.85940493,
         0.78559129,  0.75710126,  2.36389638,  1.58152865,  1.96476345,
         0.70284667,  0.80582551,  2.11508347,  0.17749674,  0.90879937,
         2.60368177,  2.55750701,  2.09008228,  0.09527522,  0.07861022,
         2.42931478,  0.36894649,  0.96179572,  0.60865037,  1.34471242,
         2.44394798,  1.48191296,  2.30470538,  0.72382554,  2.55085797],
       [ 0.4460043 , -0.92815562, -0.36306902,  0.02044748, -0.01997227,
        -0.66784918,  0.30280853, -0.58435965, -0.4538    , -0.83419368,
         0.38298784, -0.31159393,  0.32168943, -0.10436606, -0.71233136,
        -0.93288816,  0.27015596, -0.99035812, -0.77765151, -0.565299  ,
        -0.38056115, -0.89752559, -0.637542  , -0.7976791 , -0.17864977,
         0.17748862, -0.25419538, -0.21643761, -0.83896555, -0.04488033,
        -0.14467027,  0.34145294, -0.1916855 , -0.94122864, -0.19017877]])
    
    R_SW = np.array([[ 0.99015653, -0.09001756,  0.10717691],
                    [ 0.10717691,  0.98012199, -0.16695508],
                    [-0.09001756,  0.17679855,  0.98012199]])
    
    t_S = np.array([-0.562109, 1.41947194, 0.58107842])
    
    # 模拟生成 P_SI 和 P_SI_Noise 数据
    data_generator = SonarDataGenerator(P_W, R_SW, t_S, Var_Noise=0.1)
    P_S, P_SI, P_SI_Noise = data_generator.generate_data()
    print(P_SI)