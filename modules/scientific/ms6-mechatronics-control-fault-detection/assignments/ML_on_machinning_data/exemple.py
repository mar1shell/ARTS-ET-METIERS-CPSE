import data_capteurs
import matplotlib.pyplot as plt

plt.plot(data_capteurs.data['D_Cyl'])
plt.xlabel("Trous")
plt.ylabel("Diamètre moyen sur la paroi")
plt.show()