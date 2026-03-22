import subprocess

def run_script(script_name):
    print(f"\nRunning {script_name}...")
    result = subprocess.run(["python", script_name])
    
    if result.returncode != 0:
        print(f"{script_name} failed ❌")
        exit()
    else:
        print(f"{script_name} completed ✅")


def main():
    run_script("C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/scripts/fetch_data.py")
    run_script("C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/scripts/transform_data.py")
    run_script("C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/scripts/load_to_db.py")
    
    print("\nFull pipeline executed successfully 🚀")


if __name__ == "__main__":
    main()