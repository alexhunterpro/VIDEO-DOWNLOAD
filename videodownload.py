import Download

if __name__ == "__main__":
    try:
        Download.main()
    except AttributeError:
        print("Module loaded but main() function not found.")
