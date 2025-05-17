import data_fetcher


def main():
    data = data_fetcher.fetch_data("Fox")
    print(data)


if __name__ == '__main__':
    main()