import os
from pathlib import Path

# --- Helper Function to Calculate Directory Size ---
def get_directory_size(directory):
    """Recursively calculates the total size of a directory in bytes."""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # Skip if it's a symlink or other non-file type
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
    except FileNotFoundError:
        return 0 # Directory doesn't exist
    except Exception as e:
        print(f"Could not scan {directory}: {e}")
        return 0
    return total_size

# --- Main Logic ---
def analyze_caches():
    """Finds common AI/Python cache locations and reports their size."""
    print("--- Starting Cache Analysis (Read-Only) ---")

    # Get the user's home directory in a reliable way
    home_dir = Path.home()

    # Define the cache directories to check
    # We use the Path object to build paths correctly
    caches_to_check = {
        "Hugging Face": home_dir / ".cache" / "huggingface",
        "Triton": home_dir / ".triton",
        "PyTorch Hub": home_dir / ".cache" / "torch" / "hub",
        "pip": home_dir / ".cache" / "pip"
    }

    report = {}
    grand_total = 0

    for name, path in caches_to_check.items():
        print(f"Analyzing: {path}...")
        if path.exists():
            size_in_bytes = get_directory_size(path)
            # Convert bytes to gigabytes for readability
            size_in_gb = size_in_bytes / (1024 * 1024 * 1024)
            report[name] = size_in_gb
            grand_total += size_in_gb
        else:
            report[name] = 0

    print("\n--- Cache Analysis Report ---")
    for name, size_in_gb in report.items():
        # The ':<15' part aligns the text nicely
        print(f"- {name:<15}: {size_in_gb:.2f} GB")
    print("-------------------------------")
    print(f"Total Combined Cache Size: {grand_total:.2f} GB")
    print("\nThis script is read-only. No files were deleted or modified.")

if __name__ == "__main__":
    analyze_caches()
