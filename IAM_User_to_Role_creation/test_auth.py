#!/usr/bin/env python3
"""
Test script to verify authentication functionality
"""

import requests
import json
import time
import subprocess
import signal
import os
from threading import Thread

def start_server():
    """Start the backend server in a separate process"""
    return subprocess.Popen(['python3', 'iam_conversion_backend.py'], 
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE)

def test_authentication():
    """Test the authentication endpoints"""
    base_url = "http://localhost:8081"
    
    print("🧪 Testing Authentication System")
    print("=" * 50)
    
    # Test 1: Valid credentials
    print("\n1. Testing valid credentials...")
    try:
        response = requests.post(f"{base_url}/api/login", 
                               json={"username": "admin", "password": "123@admin"},
                               timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Valid credentials accepted")
            else:
                print("❌ Valid credentials rejected")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing valid credentials: {e}")
    
    # Test 2: Invalid credentials
    print("\n2. Testing invalid credentials...")
    try:
        response = requests.post(f"{base_url}/api/login", 
                               json={"username": "admin", "password": "wrong"},
                               timeout=5)
        if response.status_code == 401:
            print("✅ Invalid credentials properly rejected")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing invalid credentials: {e}")
    
    # Test 3: Status endpoint
    print("\n3. Testing status endpoint...")
    try:
        response = requests.get(f"{base_url}/api/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'connected':
                print("✅ Status endpoint working")
                print(f"   Account ID: {data.get('account_id', 'Unknown')}")
            else:
                print("⚠️ Status endpoint returned disconnected")
        else:
            print(f"❌ Status endpoint error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing status endpoint: {e}")
    
    # Test 4: HTML page
    print("\n4. Testing HTML page...")
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200 and "IAM User to Role Converter" in response.text:
            print("✅ HTML page loads correctly")
            if "loginModal" in response.text:
                print("✅ Login modal present in HTML")
            else:
                print("❌ Login modal not found in HTML")
        else:
            print(f"❌ HTML page error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing HTML page: {e}")

def main():
    """Main test function"""
    print("Starting IAM Converter Authentication Test")
    print("=" * 50)
    
    # Start the server
    print("Starting backend server...")
    server_process = start_server()
    
    # Wait for server to start
    time.sleep(3)
    
    try:
        # Run tests
        test_authentication()
        
        print("\n" + "=" * 50)
        print("🎉 Authentication test completed!")
        print("\nTo manually test:")
        print("1. Open http://localhost:8081 in your browser")
        print("2. Login with username: admin, password: 123@admin")
        print("3. Verify the interface loads after login")
        
    finally:
        # Clean up
        print("\nStopping server...")
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()
        print("Server stopped.")

if __name__ == "__main__":
    main()
