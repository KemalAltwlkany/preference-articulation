import os as os

folder = "/home/kemal/Programming/Python/Preference_Articulation/Reports/TestResults/LocalSearch/LS_apriori/BK1"
if not os.path.exists(folder):
    os.makedirs(folder)

print(os.listdir(folder))
