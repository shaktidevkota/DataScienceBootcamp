validation_loss = [
    0.80,
    0.60,
    0.45,
    0.35,
    0.30,
    0.28,
    0.27,
    0.28,
    0.29,
    0.31
]

best_loss = float("inf")
patience = 2
counter = 0

for epoch, loss in enumerate(validation_loss, start=1):

    print(f"Epoch {epoch} | Validation Loss = {loss}")

    if loss < best_loss:
        best_loss = loss
        counter = 0
        print(" Improved!")
    else:
        counter += 1
        print(f" No improvement ({counter}/{patience})")

    if counter >= patience:
        print(f"\nEarly Stopping at Epoch {epoch}")
        break