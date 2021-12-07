def decorator(fn):
    print("Я вызываюсь при декарировании")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        return fn(*args, **kwargs)
    return wrapper


@decorator
def test():
    ...


if __name__ == "__main__":
    test()