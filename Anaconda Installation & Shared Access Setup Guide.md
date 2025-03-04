

---

# Anaconda Installation & Shared Access Setup Guide

This guide explains how to install Anaconda on Linux (using the 2024.10-1 release) in a designated directory (e.g. `/opt/anaconda3`) and configure it so that a group of users can share the installation.

## 1. Download and Install Anaconda

You have two options to install Anaconda:

### Option A: Silent Installation (Non-Interactive)

Install Anaconda directly into `/opt/anaconda3` without prompts:

```bash
sudo bash Anaconda3-2024.10-1-Linux-x86_64.sh -b -p /opt/anaconda3
```

### Option B: Download then Install Interactively

1. **Download the installer:**

   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
   ```

2. **Run the installer:**

   ```bash
   sudo bash Anaconda3-2024.10-1-Linux-x86_64.sh
   ```

   When prompted, specify the installation path as `/opt/anaconda3`.

> **Note:** Use the silent installation (Option A) if you want a non-interactive install.

## 2. Configure Shared Access via a Group

To allow multiple users to use the same Anaconda installation, follow these steps:

### 2.1 Create a New Group

Create a group (e.g., `condagroup`) for users who need access to Anaconda:

```bash
sudo groupadd condagroup
```

### 2.2 Change Group Ownership

Update the group ownership of the Anaconda installation directory to the new group. Ensure you use the correct installation path (`/opt/anaconda3`):

```bash
sudo chgrp -R condagroup /opt/anaconda3
```

### 2.3 Set Directory Permissions

Allow read, write, and execute permissions for the owner, root, and members of `condagroup`:

```bash
sudo chmod -R 770 /opt/anaconda3
```

### 2.4 Add Users to the Group

Add each user who should have access to the installation. Replace `<USERNAME>` with the actual username. For example, to add user `pipalutt`:

```bash
sudo adduser pipalutt condagroup
```

## 3. Initialize Conda for Users

Run the following command (as each user) to initialize Conda:

```bash
conda init
```

## 4. Update the System PATH

Ensure that Anaconda’s `bin` directory is in the system PATH for all users by creating a profile script:

```bash
echo 'export PATH="/opt/anaconda3/bin:$PATH"' | sudo tee /etc/profile.d/anaconda.sh
```

This will update the PATH automatically on login for all users.

---

This documentation now reflects the correct installation directory (`/opt/anaconda3`) and includes all the necessary commands for setting up a shared Anaconda environment.
