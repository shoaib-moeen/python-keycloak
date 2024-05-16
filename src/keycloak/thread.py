import threading

class ThreadWithReturnValue(threading.Thread):
    
    def __init__(self, target=None, args=()):
        threading.Thread.__init__(self, target=target, args=args, daemon=True)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return
