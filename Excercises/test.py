import sys
import torch

# Print Python version
print("Python version:", sys.version)

# Print PyTorch version
try:
    print("PyTorch version:", torch.__version__)
except ImportError:
    print("PyTorch is not installed, please check your environment.")

# Check if PyTorch is installed successfully
print("PyTorch version:", torch.__version__)

# Check if CUDA is available (if PyTorch GPU version is installed)
print("CUDA availability:", torch.cuda.is_available())

# If a GPU is available, print the GPU device name
if torch.cuda.is_available():
    print("GPU device name:", torch.cuda.get_device_name(0))

# Check if MPS (Apple Metal acceleration) is available
print("MPS availability:", torch.backends.mps.is_available())

# Check MPS compatibility
print("MPS compatibility:", torch.backends.mps.is_built())

# Select the appropriate device
if torch.cuda.is_available():
    device = torch.device("cuda")  # CUDA device for HPC servers
elif torch.backends.mps.is_available():
    device = torch.device("mps")  # MPS device for MacBook
else:
    device = torch.device("cpu")  # Fallback to CPU

print(f"Selected computing device: {device}")

# Example: Create a tensor and move it to the selected device
x = torch.tensor([1.0, 2.0, 3.0]).to(device)
print(f"x device: {x.device}")

# Select the computing device again (redundant but included for clarity)
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print(f"Selected computing device: {device}")

# # Initialize the model
# model = YourModel().to(device)
#
# # Create data
# x = torch.randn(32, 3, 224, 224).to(device)  # Assuming 32 images of size 224x224
# y = torch.randint(0, 10, (32,)).to(device)  # Assuming 10 classes
#
# # Define loss function and optimizer
# criterion = torch.nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
#
# # Training step
# optimizer.zero_grad()
# outputs = model(x)
# loss = criterion(outputs, y)
# loss.backward()
#
# # `optimizer.step()` is needed only for CUDA devices
# if device.type == "cuda":
#     optimizer.step()
#
# print("Training completed!")

# String operations
s = "Hello world!"
print(len(s))  # Print string length
print(s[len(s)-1])  # Print the last character
print(s[0])  # Print the first character

# Boolean type
b1 = True
b2 = False

# Null value type
n = None

# Type function usage
print(type(s))
print(type(b1))

# # BMI calculation = weight / (height ** 2)
# user_weight = float(input("What is your weight? "))
# user_height = float(input("What is your height? "))
# user_BMI = user_weight / (user_height ** 2)
# print("Your BMI is: " + str(user_BMI))

## If-else statement
#
# mood_index = int(input("What is your partner's mood today? "))
# if mood_index >= 60:
#     print("Congratulations, you can probably play games tonight! Go Pikachu!")
#     print("hahaha")
# else: # mood_index < 60
#     print("For the sake of your life, better not play!")

# Nested conditional statements

# mood_index = int(input("What is your wife's mood today? (Enter a number) "))
# at_home = bool(input("Is she at home? Enter 'T' for yes, 'F' for no "))
# play_game = "Time to play games! Haha, let's go!"
# dont_play = "For the sake of your life, better not play!"
# if at_home == False:
#     print(play_game)
# else:
#     if mood_index >= 60:
#         print(play_game)
#     else:
#         print(dont_play)
