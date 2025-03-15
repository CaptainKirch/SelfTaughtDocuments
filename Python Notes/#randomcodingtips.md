# Setting Up A New Anaconda Environment Steps

## **Step 1: Open Terminal**

- **On Mac**: Open **Terminal** or **Anaconda Prompt**.
- **On Windows**: Open **Anaconda Prompt**.
- **On VSCode**: Open the integrated terminal with `Ctrl+` ` (backtick).

---

## **Step 2: Create a New Environment**

Use the following command:

```bash
bash
CopyEdit
conda create -n myenv python=3.x

```

- **Replace `myenv`** with a descriptive name for your environment.
- **Replace `3.x`** with the Python version you need.

**Example**:

```bash
bash
CopyEdit
conda create -n project1 python=3.9

```

This creates an environment named `project1` using **Python 3.9**.

---

## **Step 3: Activate the Environment**

Before installing packages or running code, **activate** the environment:

```bash
bash
CopyEdit
conda activate myenv

```

**Example**:

```bash
bash
CopyEdit
conda activate project1

```

**Tip:** When activated, you’ll see the environment name on the left of your terminal prompt:

```
ruby
CopyEdit
(project1) user@computer:~$

```

---

## **Step 4: Install Packages**

Install packages specific to your project. You can use:

```bash
bash
CopyEdit
conda install package-name

```

**Example**:

```bash
bash
CopyEdit
conda install numpy pandas matplotlib

```

You can also install packages using `pip` within Conda:

```bash
bash
CopyEdit
pip install requests beautifulsoup4

```

**Tip:** It’s better to use `conda install` when possible because it manages dependencies better, but `pip` works too.

---

## **Step 5: List Installed Packages (Optional)**

To see which packages are installed in the environment:

```bash
bash
CopyEdit
conda list

```

---

## **Step 6: Verify the Python Version (Optional)**

To check the Python version in your environment:

```bash
bash
CopyEdit
python --version

```

You should see the version you specified during creation.

---

## **Step 7: Deactivate the Environment**

When you’re done coding:

```bash
bash
CopyEdit
conda deactivate

```

Your terminal prompt will return to normal, indicating the environment is no longer active.

---

## **Step 8: Select the Environment in VSCode (Optional)**

1. **Open VSCode**.
2. Open the **Command Palette** with `Ctrl+Shift+P`.
3. Type:
    
    ```
    vbnet
    CopyEdit
    Python: Select Interpreter
    
    ```
    
4. Choose the environment you created (`myenv`). It should look like:
    
    ```
    bash
    CopyEdit
    (project1) /Users/YourUsername/anaconda3/envs/project1/bin/python
    
    ```
    

This ensures VSCode is using the environment’s Python interpreter and packages.

---

## **Step 9: (Optional) Exporting the Environment**

To share the environment or recreate it later:

```bash
bash
CopyEdit
conda env export > environment.yml

```

This creates an `environment.yml` file listing all installed packages.

**To recreate the environment**:

```bash
bash
CopyEdit
conda env create -f environment.yml

```

---

## **Step 10: (Optional) Delete an Environment**

If you no longer need an environment:

```bash
bash
CopyEdit
conda remove --name myenv --all

```

**Example**:

```bash
bash
CopyEdit
conda remove --name project1 --all

```

---

## **Summary of Commands**

| Action | Command |
| --- | --- |
| **Create an environment** | `conda create -n myenv python=3.x` |
| **Activate the environment** | `conda activate myenv` |
| **Deactivate the environment** | `conda deactivate` |
| **Install packages** | `conda install package-name` |
| **List installed packages** | `conda list` |
| **Export environment** | `conda env export > environment.yml` |
| **Recreate from environment.yml** | `conda env create -f environment.yml` |
| **Delete an environment** | `conda remove --name myenv --all` |

---

## **Example Workflow**

```bash
bash
CopyEdit
# Step 1: Create a new environment with Python 3.9
conda create -n data_analysis python=3.9

# Step 2: Activate the environment
conda activate data_analysis

# Step 3: Install necessary packages
conda install numpy pandas matplotlib seaborn

# Step 4: Check installed packages
conda list

# Step 5: Start coding in VSCode or Jupyter Notebook

# Step 6: Deactivate the environment when done
conda deactivate

```

---

## **Tips and Best Practices**

1. **Use descriptive names** for environments (e.g., `data_analysis`, `web_dev`).
2. **Keep environments project-specific** to avoid conflicts.
3. **Export and save `environment.yml` files** for reproducibility.
4. **Delete unused environments** to keep your system clean.

---

## **When to Create a New Environment?**

- **New project with different dependencies**.
- **Experimenting with new libraries**.
- **Using a different Python version**.
- **Collaborating and sharing code**.

Otherwise, feel free to reuse an existing environment for similar tasks!


# **SOP: Pushing Files to GitHub from VS Code**

**Last Updated:** March 12, 2025

### **🛠 Prerequisites**

✅ Git installed → Check with `git --version`

✅ GitHub account created → [https://github.com](https://github.com/)

✅ Repository created on GitHub

---

## **Step 1: Navigate to Your Project Folder**

Open **Terminal** in **VS Code** or **Mac Terminal** and move to your project folder:

```bash
bash
CopyEdit
cd ~/Documents/AI-Journey

```

(Adjust the path if your folder is in a different location.)

To confirm you’re in the correct directory:

```bash

ls -la

```

You should see your project files listed (e.g., `README.md`, `.py` files).

---

## **Step 2: Initialize Git (If Not Already Initialized)**

If this is the **first time** using Git in the folder, initialize it:

```bash

git init

```

---

## **Step 3: Add Files to Git**

Stage all files for the commit:

```bash

git add .

```

Check the status to ensure files are staged:

```bash

git status

```

It should list all files under **"Changes to be committed"**.

---

## **Step 4: Commit Your Changes**

Save your changes with a commit message:

```bash
bash
CopyEdit
git commit -m "Initial commit - added project files"

```

---

## **Step 5: Connect to GitHub**

If this is your **first time linking the project to GitHub**, run:

```bash
bash
CopyEdit
git remote add origin https://github.com/yourusername/AI-Journey.git

```

To confirm the remote is set up correctly:

```bash
bash
CopyEdit
git remote -v

```

You should see:

```
perl
CopyEdit
origin  https://github.com/yourusername/AI-Journey.git (fetch)
origin  https://github.com/yourusername/AI-Journey.git (push)

```

---

## **Step 6: Push to GitHub**

Send everything to GitHub:

```bash
bash
CopyEdit
git branch -M main
git push -u origin main

```

✅ **Done!** Your files are now live on GitHub.

---

## **Step 7: Updating GitHub in the Future**

Whenever you make changes to your files, follow these steps:

```bash
bash
CopyEdit
git add .
git commit -m "Updated [describe change]"
git push origin main

```

Example commit message:

```bash
bash
CopyEdit
git commit -m "Updated Python script for data analysis"

```

---

## **Troubleshooting**

### **🔴 "remote origin already exists" Error**

Fix it by removing and re-adding the remote:

```bash
bash
CopyEdit
git remote remove origin
git remote add origin https://github.com/yourusername/AI-Journey.git

```

### **🔴 Forgot to Commit Before Pushing?**

Run:

```bash
bash
CopyEdit
git commit -am "Quick commit before push"
git push origin main

```

### **🔴 Need to Force Push?**

If Git refuses to push, use:

```bash
bash
CopyEdit
git push --force origin main

```

(Only use this if necessary, as it overwrites remote changes.)
