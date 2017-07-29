import threading


class Core:

    @classmethod
    def run_simple(cls, func, *args, name=None):
        try:
            task = threading.Thread(target=func, name=name, args=list(args))
            task.start()
        except threading.ThreadError:
            pass
