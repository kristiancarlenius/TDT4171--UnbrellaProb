import numpy as np
def WhenUmbrella_Rain(liste, tid):
    tid = tid-1
    prob_o = np.array([[[0.1, 0], [0, 0.8]], [[0.9, 0], [0, 0.2]]])
    prob_t = np.array([[0.7, 0.3], [0.3, 0.7]])
    prob_r_u = np.array([0.5, 0.5])
    kon = [1.82, 1.5628, 1.4, 1.3, 1.2]
    for i in range(len(liste)):
        der = np.dot(prob_t.transpose(), prob_r_u)
        print(" der:", der, i+1)
        her = np.dot(prob_o[liste[i]], der)
        print(" her:", her, i+1)
        prob_r_u = np.dot(kon[i], her)
        print(" prob:", prob_r_u, i+1)
        print("")
        if(tid==i):
            return prob_r_u

print(WhenUmbrella_Rain([1, 1, 0, 1, 1], 5))