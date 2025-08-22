# trace_libiomp.py
import os, sys, traceback
import psutil

def print_header(msg):
    print("\n" + "="*10 + " " + msg + " " + "="*10)

def check_libiomp():
    found = []
    try:
        proc = psutil.Process()
        for m in proc.memory_maps():
            path = m.path.lower()
            if "libiomp5md.dll" in path:
                found.append(path)
    except Exception as e:
        print("psutil error:", e)
    if found:
        print("libiomp5md.dll loaded from:")
        for p in found:
            print("  -", p)
    else:
        print("libiomp5md.dll NOT found in memory maps.")

def safe_import(name):
    print_header(f"importing {name}")
    try:
        mod = __import__(name)
        print(f"{name} imported OK, module file: {getattr(mod, '__file__', 'n/a')}")
    except Exception:
        print(f"Exception importing {name}:")
        traceback.print_exc()

if __name__ == "__main__":
    print("PID:", os.getpid())
    print("Python:", sys.executable)
    print("Environment variables (relevant):")
    for k in ("OMP_NUM_THREADS","MKL_NUM_THREADS","KMP_DUPLICATE_LIB_OK"):
        print(f"  {k} =", os.environ.get(k))

    print_header("Before any imports")
    check_libiomp()

    # Import small harmless stdlib first
    safe_import("math")
    check_libiomp()

    # Now try numpy (this is where you saw the crash)
    safe_import("numpy")
    check_libiomp()

    # Optionally try torch if present
    safe_import("torch")
    check_libiomp()

    print_header("Finished")
