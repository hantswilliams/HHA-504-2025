# AHI 504 – Cloud Informatics
## Homework: Multi‑Cloud Serverless Function (Blood Pressure Triage)

**Due:** October 15 2025 
**Submission:** GitHub repo link + public function URLs + short recording (Zoom or Loom)

---

### 1) Overview
In this assignment you will implement the **same HTTP serverless function** in **at least two** of the following clouds:
- **Google Cloud** (Cloud Functions 2nd gen or Cloud Run Functions)
- **Microsoft Azure** (Azure Functions)
- **Oracle Cloud Infrastructure (OCI)** (OCI Functions)

Your function will accept JSON input describing one laboratory value that you choose (e.g., serum potassium, fasting glucose, HbA1c, creatinine, total bilirubin). You must implement a binary classifier (return normal or abnormal) based on a published reference range or clinical cut-point that you cite. Keep the logic simple (one threshold or a small range check).

You **CAN NOT** choose blood pressure. 

> For grading consistency, use this simplified rule:  
> **Normal** if `systolic < 120` **and** `diastolic < 80`; otherwise **Abnormal**.

You must also record a brief walkthrough (2–4 minutes) showing deployment, a live test, and where the code lives in your repo.

---

### 2) Learning Objectives
- Deploy and invoke HTTP serverless functions across multiple cloud providers.
- Parse JSON payloads and return structured JSON responses.
- Configure authentication for public web access appropriate for a brief demo.
- Compare experience, logs, and deployment across selected clouds.
- Translate a published clinical reference range into executable logic with proper citation.
- Design a clear JSON contract for a simple clinical rule and return a binary result.

---

### 3) Deliverables
- **Code repository (GitHub)** called `504_serverless_functions` with a top‑level `README.md` and separate folders per cloud (e.g., `gcp/`, `azure/`, `oci/` as needed that will contain screenshots). Inside of this readme/github repo:   
    - Include a short section on the **Lab Rules**, starting with your chosen lab, the rule you implemented (plain English + formula/threshold), and a citation (journal/book/authoritative website with URL/DOI).
    - **Publicly accessible endpoint URLs** for each deployed function (paste into the README).  
    - **Recording (Zoom or Loom)** showing:
        - A quick code tour.
        - At least one **live GET/POST request** using python `requests` in either a notebook or script file, and the **JSON response**.
        - Where logs/monitoring appear in each cloud.
    - **One short paragraph** in the README comparing the two clouds you chose (what felt easier/harder and why).

---

### 4) Input/Output Contract, Example with BP: 
**Request (JSON):**
```json
{ "systolic": 118, "diastolic": 76 }
```

**Response (JSON):**
```json
{
  "systolic": 118,
  "diastolic": 76,
  "status": "normal",
  "category": "Normal (<120/<80)"
}
```

**Error responses (JSON):**
- Missing fields: `{ "error": "Both 'systolic' and 'diastolic' are required." }`
- Non‑numeric: `{ "error": "'systolic' and 'diastolic' must be numbers." }`

---

### 5) Templates (Python)

- Please see `assignment_3/example_gcp.py` 

---

### 6) Testing Instructions


**Python (requests):**
```python
import requests, json
url = "<YOUR_ENDPOINT_URL>"
## if post 
r = requests.post(url, json={"systolic": 130, "diastolic": 85})
## if get 
r = requests.get(url, json={"systolic": 130, "diastolic": 85})
print(r.status_code, r.json())
```

**Expected behavior:**
- `118/76` → `"status": "normal"`
- `130/85` → `"status": "abnormal"`

---

### 7) Recording Requirements (2–4 minutes)
- Brief intro (name, which two clouds you chose).
- Show your repository and where the cloud‑specific code lives.
- Show the live endpoint(s) and execute a POST request with two examples (one normal, one abnormal).
- Show where to find **logs** or **monitoring** in each cloud’s portal.
- Mention any gotchas (permissions, runtime version, cold starts).

Upload the recording and place a **shareable link** in your README.

---

### 8) README Requirements
- Cloud environments used and regions.
- Deployment commands or steps you executed.
- Screenshots showing functionality that have your custom URLs, along with outputs
- Public endpoint URLs (+ notes on auth: unauthenticated vs key‑based).
- Example `requests` invocations that **work as shown** in your video.
- Short comparison paragraph of the two clouds.

---
