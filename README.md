# DarkTables Firewall
## Securing your Linux machines has never been easier

Secure your Linux devices easily by creating rules for your network activity via command line interface.

<p align="center">
<img src="https://user-images.githubusercontent.com/63206167/189040436-11a7d4bf-69ce-4e50-a9e0-81f9ba24affc.png" width="200">
</p>

## Features

- Create objects for representing hosts and services on your network
- Use the objects you have created to add different rules easily
- Switch between two modes - Blacklist, and Whitelist
- Block IP addresses from a file list
- Create and load different profiles for easy switching in different situations
- Basic built-in profiles for browsing 🤓, paranoids 😨, and heros (no security  😊 ) ! 
- More to be implemented in the future 

## Notes
- This program must be run as root
- You should have python3 installed on your machine
- Blacklist example file taken from - https://iplists.firehol.org/

<p align="center">
<img src="https://user-images.githubusercontent.com/63206167/189294025-3246e759-0734-422d-92be-77bfb58edd59.gif" alt="demo"  width="800" />
</p>

## Run
```
sudo apt update
sudo apt install python3
sudo python3 darktables.py
```
