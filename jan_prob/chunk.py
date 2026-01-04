

def read_lines_in_batches(file_path, batch_size=1000):
    batch = []
    with open(file_path, "r") as f:
        for line in f:
            batch.append(line)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch



class SingletonLogger:
    _instance = None  # Class-level private variable to store the single instance

    def __new__(cls):
        if cls._instance is None:
            print("Creating new logger instance")
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, msg):
        print(f"[LOG]: {msg}")