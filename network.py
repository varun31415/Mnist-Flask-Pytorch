from torch import nn
from torch import optim
from torch import no_grad
from torch import float as torch_float

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512,10)
        )
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

    def train_loop(self, dataloader, learning_rate):
        self.optimizer = optim.SGD(self.parameters(), lr=learning_rate)
        size = len(dataloader.dataset)
        for batch, (x_train, y_train) in enumerate(dataloader):
            pred = self(x_train)
            loss = self.loss_fn(pred, y_train)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            if batch % 100 == 0:
                loss, current = loss.item(), batch * len(x_train)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    def test_loop(self, dataloader):
        size = len(dataloader.dataset)
        num_batches = len(dataloader)
        test_loss, correct = 0, 0

        with no_grad():
            for (x_test, y_test) in dataloader:
                pred = self(x_test)
                loss = self.loss_fn(pred, y_test)

                test_loss += self.loss_fn(pred, y_test).item()
                correct += (pred.argmax(1) == y_test).type(torch_float).sum().item()

        test_loss /= num_batches
        correct /= size
        print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
        
