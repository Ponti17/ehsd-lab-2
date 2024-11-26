import numpy as np
import pandas as pd

def get_tl_model(case: int):
    """
    Returns the transmission line model for the given case.
    """

    # Length of transmission line
    x = 0.010 # 10 cm

    # Rise time
    T_rise = 500*1e-12

    # Microstrip
    C_matrix_1 = np.array([
        [128.5, -12.0],
        [-12.0, 128.5]
    ]) # pF/m

    L_matrix_1 = np.array([
        [283.4, 52.2],
        [52.2, 283.4]
    ]) # nH/m

    # Side-by-side Stripline
    C_matrix_2 = np.array([
        [153.3, -21.8],
        [-21.8, 153.3]
    ]) # pF/m

    L_matrix_2 = np.array([
        [318.5, 45.3],
        [45.3, 318.5]
    ]) # nH/m

    # Broadside Stripline
    C_matrix_3 = np.array([
        [167.5, -53.5],
        [-53.5, 167.5]
    ]) # pF/m

    L_matrix_3 = np.array([
        [318.0, 101.4],
        [101.4, 318.0]
    ]) # nH/m

    # Z_0
    Z_0_1 = np.sqrt((L_matrix_1[0,0]*1e-9) / (C_matrix_1[0,0]*1e-12))
    Z_0_2 = np.sqrt((L_matrix_2[0,0]*1e-9) / (C_matrix_2[0,0]*1e-12))
    Z_0_3 = np.sqrt((L_matrix_3[0,0]*1e-9) / (C_matrix_3[0,0]*1e-12))

    # Time delays
    TD_1 = x*np.sqrt(C_matrix_1[0,0]*1e-12*L_matrix_1[0,0]*1e-9)
    TD_2 = x*np.sqrt(C_matrix_2[0,0]*1e-12*L_matrix_2[0,0]*1e-9)
    TD_3 = x*np.sqrt(C_matrix_3[0,0]*1e-12*L_matrix_3[0,0]*1e-9)

    # Minimum number of segments
    N_seg_min_1 = 10 * TD_1/T_rise
    N_seg_min_2 = 10 * TD_2/T_rise
    N_seg_min_3 = 10 * TD_3/T_rise

    # Number of segments
    N_seg_1 = np.ceil(N_seg_min_1) # 2 
    N_seg_2 = np.ceil(N_seg_min_2) # 2
    N_seg_3 = np.ceil(N_seg_min_3) # 2
    
    # Inductive Coupling Factor
    K_1 = L_matrix_1[0,1]/np.sqrt(L_matrix_1[0,0]*L_matrix_1[1,1])
    K_2 = L_matrix_2[0,1]/np.sqrt(L_matrix_2[0,0]*L_matrix_2[1,1])
    K_3 = L_matrix_3[0,1]/np.sqrt(L_matrix_3[0,0]*L_matrix_3[1,1])

    # Total C and Total L
    C_total_1 = TD_1/Z_0_1 
    C_total_2 = TD_2/Z_0_2
    C_total_3 = TD_2/Z_0_3

    L_total_1 = TD_1*Z_0_1
    L_total_2 = TD_2*Z_0_2
    L_total_3 = TD_3*Z_0_3

    # C and L for segments
    C_seg_1 = x/N_seg_1 * (C_matrix_1[0,0] + C_matrix_1[0,1])
    C_seg_2 = x/N_seg_2 * (C_matrix_2[0,0] + C_matrix_2[0,1])
    C_seg_3 = x/N_seg_3 * (C_matrix_3[0,0] + C_matrix_3[0,1])

    L_seg_1 = x/N_seg_1 * (L_matrix_1[0,0])
    L_seg_2 = x/N_seg_2 * (L_matrix_2[0,0])
    L_seg_3 = x/N_seg_3 * (L_matrix_3[0,0])

    Cm_seg_1 = x/N_seg_1 * C_matrix_1[0,1] * (-1)
    Cm_seg_2 = x/N_seg_2 * C_matrix_2[0,1] * (-1)
    Cm_seg_3 = x/N_seg_3 * C_matrix_3[0,1] * (-1)

    tl_param_1 = {
        'C_matrix': C_matrix_1,
        'L_matrix': L_matrix_1,
        'Z_0': Z_0_1,
        'TD': TD_1,
        'N_min': N_seg_min_1,
        'N': N_seg_1,
        'K': K_1,
        'C_tot': C_total_1,
        'L_tot': L_total_1,
        'C_seg': C_seg_1,
        'L_seg': L_seg_1,
        'Cm_seg': Cm_seg_1
    }

    tl_param_2 = {
        'C_matrix': C_matrix_2,
        'L_matrix': L_matrix_2,
        'Z_0': Z_0_2,
        'TD': TD_2,
        'N_min': N_seg_min_2,
        'N': N_seg_2,
        'K': K_2,
        'C_tot': C_total_2,
        'L_tot': L_total_2,
        'C_seg': C_seg_2,
        'L_seg': L_seg_2,
        'Cm_seg': Cm_seg_2
    }

    tl_param_3 = {
        'C_matrix': C_matrix_3,
        'L_matrix': L_matrix_3,
        'Z_0': Z_0_3,
        'TD': TD_3,
        'N_min': N_seg_min_3,
        'N': N_seg_3,
        'K': K_3,
        'C_tot': C_total_3,
        'L_tot': L_total_3,
        'C_seg': C_seg_3,
        'L_seg': L_seg_3,
        'Cm_seg': Cm_seg_3
    }

    if case == 1:
        return tl_param_1
    if case == 2:
        return tl_param_2
    if case == 3:
        return tl_param_3

    raise ValueError("Invalid case. Choose 1, 2 or 3.")
