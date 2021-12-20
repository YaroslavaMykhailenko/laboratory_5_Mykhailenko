import math
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from matplotlib.pyplot import figure


def Birth_Death():
    
    k = 10
    lambda_ = [0.8, 0.1, 0.3, 0.2, 0.4, 0.7, 0.2, 0.8, 0.1, 0.5, 0.4]
    mu_ = [0.2, 0.3, 0.1, 0.4, 0.6, 0.7, 0.8, 0.1, 0.3, 0.4, 0.5]
    y = [0.1, 0.3, 0.2, 0.8, 0.5, 0.4, 0.3, 0.9, 0.2, 0.6, 0.7]


    def differential_system(y, t):
            
        system = [-lambda_[0] * y[0] + mu_[1] * y[1],
                -(lambda_[1] + mu_[1]) * y[1] + mu_[2] * y[2] + lambda_[0] * y[0],
                -(lambda_[2] + mu_[2]) * y[2] + mu_[3] * y[3] + lambda_[1] * y[1],
                -(lambda_[3] + mu_[3]) * y[3] + mu_[4] * y[4] + lambda_[2] * y[2],
                -(lambda_[4] + mu_[4]) * y[4] + mu_[5] * y[5] + lambda_[3] * y[3],
                -(lambda_[5] + mu_[5]) * y[5] + mu_[6] * y[6] + lambda_[4] * y[4],
                -(lambda_[6] + mu_[6]) * y[6] + mu_[7] * y[7] + lambda_[5] * y[5],
                -(lambda_[7] + mu_[7]) * y[7] + mu_[8] * y[8] + lambda_[6] * y[6],
                -(lambda_[8] + mu_[8]) * y[8] + mu_[9] * y[9] + lambda_[7] * y[7],
                -(lambda_[9] + mu_[9]) * y[9] + mu_[10] * y[10] + lambda_[8] * y[8],
                -(lambda_[10] + mu_[10]) * y[10] + lambda_[9] * y[9],
                ]
        return system

    model = odeint(differential_system, y, np.linspace(0, k, 1000))

#  Побудова графіку

    figure(figsize=(10, 5), dpi=100)
    for i in range(k):
        plt.plot(np.linspace(0, k, 1000), model[:, i])

    plt.grid()
    plt.show()


def Erlang():

    k = 8
    lambda_ = 3
    mu_ = 4
    y = [0.1, 0.3, 0.2, 0.8, 0.5, 0.4, 0.3, 0.9, 0.2]


    def differential_system(y, t):

        system = [-lambda_ * y[0] +mu_ * y[1],
                -(lambda_ + mu_) * y[1] + mu_ * y[2] + lambda_ * y[0],
                -(lambda_ + mu_) * y[2] + mu_ * y[3] + lambda_ * y[1],
                -(lambda_ + mu_) * y[3] + mu_ * y[4] + lambda_ * y[2],
                -(lambda_ + mu_) * y[4] + mu_ * y[5] + lambda_ * y[3],
                -(lambda_ + mu_) * y[5] + mu_ * y[6] + lambda_ * y[4],
                -(lambda_ + mu_) * y[6] + mu_  * y[7] + lambda_ * y[5],
                -(lambda_ + mu_) * y[7] + mu_  * y[8] + lambda_ * y[6],
                -(lambda_ + mu_) * y[8] + lambda_ * y[7],
                ]
        return system

    model = odeint(differential_system, y, np.linspace(0, 10, 1000))

#  Побудова графіку

    figure(figsize=(10, 5), dpi=100)
    for i in range(k):
        plt.plot(np.linspace(0, 10, 1000), model[:, i])

    plt.grid()
    plt.show()


#   ------------- Перевірка стаціонарних ймовірностей

    stat_probability = []

    for i in range(k):

        stat_probability.append(pow(lambda_ / mu_, i) / sum([pow(lambda_ / mu_, k) for k in range(k)]))
    
    print(sum(stat_probability))
    print(stat_probability)








def start():
    print("Choose task you want to solve: \n1 - Birth-Death Model\n2 - Erlang Model")
    number = int(input(""))

    if number == 1:
        Birth_Death()
        again()
    elif number == 2:
        Erlang()
        again()   
    else:
        print("Wrong number!")


def again():
    print("Would you like to try again?:\n1 - yes\n2 - no")
    choice = int(input(""))
    if choice == 1:
        start()
    
    elif choice == 2:
        return 0 


start()