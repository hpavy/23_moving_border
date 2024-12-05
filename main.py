import torch
from run import RunSimulation

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

############# VARIABLES ################

folder_result_name = "9_model_3_case_1_zoom_weights_modified"  # name of the result folder

# Uniquement si nouveau modèle

hyper_param_init = {
    "H": 261.39,
    "ya0": 0.0175,
    "m": 1.57,
    "file": "data_john_3_case_1.csv",
    "nb_epoch": 10000,
    "save_rate": 50,
    "weight_data": 0.4,
    "weight_pde": 0.4,
    "weight_border": 0.1,
    "batch_size": 10000,
    "nb_points_pde": 1000000,
    "Re": 100,
    "lr_init": 0.001,
    "gamma_scheduler": 0.999,
    "nb_layers": 10,
    "nb_neurons": 64,
    "n_pde_test": 5000,
    "n_data_test": 5000,
    "nb_points_axes": 12,  # le nombre de points pris par axe par pas de temps
    "x_min": -0.03,
    "x_max": 0.03,
    "y_min": -0.03,
    "y_max": 0.03,
    "t_min": 6.5,
    "t_max": 8,
    "transfert_learning": "None",
    "nb_points_close_cylinder": 50,
    "nb_points_border": 25,
}

param_adim = {
    'V': 1.,
    'L': 0.025,
    'rho': 1.2
}

simu = RunSimulation(hyper_param_init, folder_result_name, param_adim)

simu.run()
