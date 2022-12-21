from network import Network
import torch
from torch import cuda
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

device = "cuda" if cuda.is_available() else "cpu"
print(f"Using {device} device")
learning_rate = 0.001
batch_size = 64
epochs = 100

train_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

train_dataloader = DataLoader(train_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

net = Network().to(device)

for t in range(epochs):
    net.train_loop(train_dataloader, learning_rate)
    net.test_loop(test_dataloader)

torch.save(net, 'digit_rec.pth')
