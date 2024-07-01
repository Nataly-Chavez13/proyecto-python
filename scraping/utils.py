import logging
import time

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Decorador para medir tiempo de ejecución
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f'Function {func.__name__} took {end_time - start_time:.4f} seconds')
        return result
    return wrapper

# Decorador para logging
def logit(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Executing function {func.__name__}')
        return func(*args, **kwargs)
    return wrapper
