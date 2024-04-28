def read_from_file(path):
    try:
        with open(path) as file:
            data = [line.strip() for line in file.readlines()]
        return data
    except FileExistsError:
        raise FileExistsError("File does not exist")
    except FileNotFoundError:
        raise FileNotFoundError("File was not found")
    except Exception:
        raise Exception("Exception occured")


def convertBoardToGraph(board: str) -> dict:
    # ["1234", "2345", "5312"]

    graph = {}
    for i, elem in enumerate(board):
        graph[i + 1] = []
        for j, char in enumerate(elem):
            if char != '0':
                graph[i + 1].append((j + 1, char))
    return graph
