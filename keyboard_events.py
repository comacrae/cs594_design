from utils import get_keys_down_dict

keys_down = get_keys_down_dict() # keeps track of valid keys and which ones are pressed

def press_key(e, k,func, *args):
    if not keys_down[k]:
        keys_down[k] = True
        func(*args)
def release_key(e,k,func, *args):
    keys_down[k] = False
    if func is not None:
        func(*args)


