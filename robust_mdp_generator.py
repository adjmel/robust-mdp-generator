# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    robust_mdp_generator.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    by: madjogou                                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    created: 2024/08/20 20:07:06 by madjogou          #+#    #+#              #
#    updated: 2024/08/20 20:07:06 by madjogou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import random

def generer_mot_de_passe(taille):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(taille))
    return mot_de_passe

mot_de_passe = generer_mot_de_passe(16)
print(mot_de_passe)

