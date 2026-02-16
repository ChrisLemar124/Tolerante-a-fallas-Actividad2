import pickle

with open("pesos.pkl", "rb") as f:
    pesos = pickle.load(f)

print(pesos.shape)
print(f"Pesos: \n{pesos}")