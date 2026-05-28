# JARVX ⚡

JARVX is a modular Python-based network scanning CLI tool designed for educational cybersecurity analysis and common-port inspection.

## Features

* IP address validation
* Common port scanning
* Risk classification
* Security scoring system
* Command-line interface
* Standalone executable support

---

## Commands

### Scan Target

```bash
jarvx scan <IP>
```

### Quick Scan

```bash
jarvx quick <IP>
```

### Deep Scan

```bash
jarvx deep <IP>
```

### Help

```bash
jarvx help
```

### Version

```bash
jarvx version
```

---

## Technologies Used

* Python
* Socket Programming
* PyInstaller
* Modular CLI Architecture

---

## Example Output

```text
[JARVX SCAN RESULTS]

PORT    STATE     SERVICE     RISK
----------------------------------------
21      CLOSED    FTP         --
22      CLOSED    SSH         --
80      OPEN      HTTP        MEDIUM

[JARVX SECURITY SCORE]
Security Score: 84/100
Status: Moderately Secure
```

---

## Disclaimer

JARVX is an educational cybersecurity project created for learning purposes. It is intended for authorized systems and environments only.

---

## Author

Developed by Adithya
