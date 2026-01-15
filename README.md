# Wazuh-soc-projet
Mini SOC project using Wazuh SIEM for detection, investigation, and incident response
# 🛡️ Wazuh-Based SOC Project

![SOC Architecture](Wazuh-soc-project/soc_architecture.png)

## 📌 Overview
This project demonstrates a **mini Security Operations Center (SOC)** environment using **Wazuh SIEM**.
The goal is to simulate real-world SOC operations including **log collection, detection, alerting, investigation, and incident response**.

---

## 🧱 Lab Architecture
The lab consists of three systems:

- **Kali Linux** – Attacker machine
- **Ubuntu Server** – Victim machine with Wazuh Agent
- **Ubuntu Server** – Wazuh SIEM (Manager + Dashboard)

Logs generated on the victim machine are forwarded to the Wazuh server for analysis and alerting.

---

## ⚙️ Tools & Technologies
- Wazuh SIEM
- Ubuntu Linux
- Kali Linux
- Python
- SSH, Audit logs
- VMware workstation

---

## 🔍 SOC Workflow Covered
- Log collection
- Attack detection
- Alert analysis
- Incident investigation
- Response & mitigation
- Reporting

---

## 📂 Project Structure
