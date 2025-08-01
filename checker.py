#!/usr/bin/env python3
import subprocess

def check_outdated_packages():
    print("\n[*] Checking for outdated system packages...")
    try:
        result = subprocess.check_output(['apt', 'list', '--upgradable'], stderr=subprocess.DEVNULL)
        lines = result.decode().split('\n')[1:]
        packages = [line for line in lines if line]
        if packages:
            print("[!] Outdated packages found:")
            for pkg in packages:
                print(f"    {pkg}")
        else:
            print("[+] System is up-to-date!")
    except Exception as e:
        print(f"[!] Error checking packages: {e}")

def check_world_writable_files():
    print("\n[*] Searching for world-writable files...")
    try:
        result = subprocess.check_output(['find', '/', '-xdev', '-type', 'f', '-perm', '-0002'], stderr=subprocess.DEVNULL)
        files = result.decode().split('\n')
        if files and files[0]:
            print(f"[!] Found {len(files)} world-writable files. Save to world_writable.txt")
            with open('world_writable.txt', 'w') as f:
                f.write('\n'.join(files))
        else:
            print("[+] No world-writable files found.")
    except subprocess.CalledProcessError:
        print("[!] Some directories could not be scanned (permission denied). Try running with sudo.")

if __name__ == "__main__":
    print("=== Local Vulnerabilities Checker ===")
    check_outdated_packages()
    check_world_writable_files()
    print("\n=== Scan complete! ===")
