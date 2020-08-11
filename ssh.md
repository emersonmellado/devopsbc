SSH - Secure SHell

** MSTC - Microsoft Terminal Connection - RDP (Remote Desktop)


1. Review what shell is
    - A program that allows you to manage the computer
    - It also allows you to run shell scripts (FILENAME.sh)
    - PowerShell on Windows is the closest we have of the Linux shell (powershell scripts FILENAME.ps1)

2. What Secure means on SSH (briefly)
    - It means we need to have some type of encryption
    - This encryption will use an algorithm and it will some sort of key pair
        - A key pair is composed of a public key and a private key
        - Public key (i.e: AWS Key) - One can also think of this as your username
        - Private Key (i.e: AWS Secret) - This is like your password.

        Pub: ssh-rsa AAAAB3Nz... aws-eb
        Structure (Syntax): Algorithm KEY alias

        Pri: 
            -----BEGIN OPENSSH PRIVATE KEY-----
            b3BlbnNzaC1rZXktdjEAA...
            -----END OPENSSH PRIVATE KEY-----
        Structure: BEGINING KEY END

3. List basics of SSH
4. Create a remote server on AWS (Lightsail)
5. Connect to it using SSH