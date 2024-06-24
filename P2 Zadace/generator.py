def par(broj):
    for i in range(broj + 1):
        if i % 2 == 0:
            yield f"Parni broj je: {i}"
        else:
            yield f"Neparni broj je: {i}"

for broj in par(30):
    print(broj)
