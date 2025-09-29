# AHI 504 — Cloud Foundations for Health Informatics  
## Lab: Deploy a Flask App on a Cloud VM  

**Purpose.** Learn how to configure and expose, via networking configurations, a simple web application on a cloud-hosted virtual machine (VM). You will (1) choose a cloud provider, (2) create and configure a VM with an open port, (3) install and run a Flask app, and (4) make the app accessible on the internet.  

**What you’ll gain.** Hands-on practice with networking (firewall rules, ports), package installation (Python), application hosting, and optional domain name setup. This builds on the VM lifecycle skills from Assignment 1.  

---

## Outcomes of this assignment: 
1. Create and configure a small VM instance on **one cloud provider (GCP, Azure, or OCI)**.  
2. Open a specific port (**5003**) and confirm external accessibility.  
3. Install Python, copy a Flask template, and run the app. Flask template: https://github.com/hantswilliams/HHA-504-2025-FlaskStarter 
4. Verify that the Flask app is publicly accessible via `http://<PUBLIC_IP>:5003`.  
5. *(Bonus)* Register a domain name (via GitHub Student Pack) and map it to your VM’s IP with DNS.  

---

## Requirements and guardrails
- **Cloud provider:** choose **one** cloud: GCP, Azure, or OCI.  
- **Instance size:** Use a **free-tier eligible or the smallest available** general-purpose shape.  
- **OS image:** Ubuntu LTS (recommended).  
- **Networking:** Must configure firewall/security rules to allow inbound TCP traffic on port **5003**.  
- **No PHI/PII.** Do not store sensitive data on the VM.  
- **Cost hygiene:** Stop/terminate all resources when done. Confirm cleanup.  

---

## Deliverables (submit both)
1. **Screen recording (Loom or Zoom, 7–10 minutes).**  
   - Show:  
     1) VM creation & networking setup (port 5003 open)  
     2) Installing updates and Python  
     3) Copying and running the Flask template: https://github.com/hantswilliams/HHA-504-2025-FlaskStarter  
     4) App accessible at `<PUBLIC_IP>:5003`  
     5) *(Bonus)* DNS configuration with your own domain name  
   - Narrate what you are doing and why (networking, firewall, Flask).  

2. **Markdown tutorial (`README.md`).**  
   - Step-by-step guide with screenshots for each stage.  
   - At least **3 screenshots** (VM setup, Flask app running locally, app accessible at IP).  
   - If you complete the bonus, include screenshot of DNS record and domain working.  

---

## Step-by-step tasks

### Part A — VM Setup
1. **Create a VM** on your chosen provider:  
   - Smallest/free-tier size  
   - Ubuntu LTS image  
   - Public IP assigned  

2. **Open port 5003**:  
   - Add a firewall/security group rule to allow inbound TCP traffic on **5003**.  
   - Verify rule is active.  

---

### Part B — Environment Configuration
1. **SSH into your VM** (cloud console or terminal).  
2. **Update OS**:  
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```  
3. **Install Python 3 + pip**:  
   ```bash
   sudo apt install python3 python3-pip -y
   ```  

---

### Part C — Flask App Deployment
1. **Copy the Flask template**:  
   ```bash
   git clone https://github.com/hantswilliams/HHA-504-2025-FlaskStarter.git
   cd flask_template
   pip3 install -r requirements.txt
   ```  
2. **Run the app on port 5003**:  
   ```bash
   python3 app.py
   ```  
3. **Verify public access**:  
   - In browser: `http://<PUBLIC_IP>:5003`  
   - Take screenshot of the page loading.  

---

### Bonus — Custom Domain Setup
1. Visit: [GitHub Student Pack Domains](https://education.github.com/pack?sort=popularity&tag=Domains).  
2. Claim a free domain via **Namecheap, Name.com, or .tech domains**.  
3. Configure a **DNS A record** pointing your domain to the VM’s public IP.  
4. Verify that `http://<yourdomain>:5003` resolves to your app.  
5. Take screenshot of domain working.  

---

## Submission format
- **GitHub (preferred):**  
  - Repo name: `cloud_vm_networking_flask`  
  - `README.md` with your tutorial + screenshots  
  - Link to Loom/Zoom recording at top of `README.md`  

---

## README.md template (copy/paste)


# Flask on Cloud VM (Assignment 2)

## Student Info
- Name:  
- Cloud Provider:  

## Video recording: 
- Zoom/Loom: 

## Steps
### 1. VM Creation
[screenshot]

### 2. Networking (Port 5003 Open)
[screenshot]

### 3. OS Update + Python Install
[commands + screenshot]

### 4. Flask App Running
[screenshot of terminal + browser]

### 5. Public IP Access
URL: http://XX.XX.XXX.XXX:5003  
[screenshot]

### 6. (Bonus) Domain Name
Domain: http://mydomain.tech:5003  
[screenshot]

