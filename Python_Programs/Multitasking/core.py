import multiprocessing

def main():
    print("NUMBER OF CORES ARE : ",multiprocessing.cpu_count())

if __name__ == "__main__":
    main()