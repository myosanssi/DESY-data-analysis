import pandas as pd
import numpy as np

# Number of rows you want
num_rows = 1000000

# Generate random unsigned 32-bit integers
data = {
    "trigger_data": np.random.randint(0, 2**32, size=num_rows, dtype=np.uint32),
    "trigger_clk": np.random.randint(0, 2**64, size=num_rows, dtype=np.uint64),
    "trigger_id": np.random.randint(0, 2**16, size=num_rows, dtype=np.uint16),
    "veto_in": np.random.choice([True, False], size=num_rows),
    "internal_trigger": np.random.choice([True, False], size=num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("example_trigger_data_large.csv", index=False)