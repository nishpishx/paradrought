import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Generate synthetic data
np.random.seed(42)
n_samples = 1000

# Variables
host_density = np.random.uniform(50, 150, size=n_samples)
parasite_prevalence = np.random.uniform(0.1, 0.5, size=n_samples)
biomass = np.random.uniform(300, 700, size=n_samples)
salinity = np.random.uniform(20, 50, size=n_samples)

# Combine into a DataFrame
data = pd.DataFrame({
    "host_density": host_density,
    "parasite_prevalence": parasite_prevalence,
    "biomass": biomass,
    "salinity": salinity
})

# Pairplot to visualize relationships
sns.pairplot(data)
plt.show()
# Display sample data
#print(data.head())
