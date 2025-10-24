import torch_directml

# Abfragen der Anzahl verfügbarer DirectML-Geräte
num_devices = torch_directml.device_count()
print(f"Number of DirecML devices: {num_devices}")

# Iteration durch die verfügbaren Geräte
for device_id in range(num_devices):
    device_name = torch_directml.device_name(device_id)
    print(f"Device {device_id}: {device_name}")