from multiprocessing import Process, shared_memory
import numpy as np

def run_parallel(n: int, k: int):
    for i in range(n):
        processes = [Process(target=calc, args=(i, j)) for j in range(n)]
        for process in processes:
            process.start()
            process.join()

def calc(arr, *args) -> int:
    i = args[0]
    j = args[1]
    if j == 0 or j == i:
        arr[i, j] = 1
    else:
        arr[i, j] = arr[i - 1, j - 1] + arr[i - 1, j]

def get_bicoeff(n: int, k: int) -> int:
    tmp = np.zeros((n,n), dtype=int)
    shm = shared_memory.SharedMemory(create=True, size=tmp.nbytes)
    existing_shm = shared_memory.SharedMemory(name=shm.name)
    arr = np.ndarray((n, n), dtype=np.int64, buffer=existing_shm.buf)
    run_parallel(n)
    print(arr)
    print("C(n, k)=C({}, {}): ".format(n - 1, k - 1), arr[n-1, k-1])
    existing_shm.close()
    existing_shm.unlink()
    del arr


