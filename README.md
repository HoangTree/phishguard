# 🛡️ PhishGuard AI

> A simple AI-powered web app that detects potential phishing messages and scam emails.

![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🚀 Quick Start

Follow these steps to run **PhishGuard AI** on your local machine.
### 1. Gỡ Python 3.13 (nếu muốn)
Settings → Apps → tìm Python → Uninstall
(Không bắt buộc nhưng khuyên dùng Python 3.11 để tránh lỗi dependency.)

### 2. Cài Python 3.11
Tải installer Python 3.11 (từ python.org). Khi cài: tick “Add Python to PATH”.

### 3. Mở PowerShell trong thư mục project rồi tạo môi trường ảo:
```bash
python -m venv .venv
```
### 4. Kích hoạt venv:
```bash
.\.venv\Scripts\Activate
```
(bạn sẽ thấy prompt chuyển sang (.venv))

### 5. Cập nhật pip/setuptools/wheel:

```bash
python -m pip install --upgrade pip setuptools wheel
```
### 6. Cài tất cả dependency bằng file:
```bash
python -m pip install -r requirements.txt
```
(Trên Python 3.11, lệnh này sẽ cài numpy, scikit-learn, pandas, flask, v.v. bình thường.)

### 7. Huấn luyện model (tạo file phishguard_pipeline.joblib):
```bash
python train.py
```
Bạn sẽ thấy output accuracy và file phishguard_pipeline.joblib được lưu.

### 8. Chạy server Flask:
```bash
python app.py
```
Mục tiêu: bạn nên thấy * Running on http://127.0.0.1:5000

### 9. Mở giao diện: mở __frontend/index.html__ trong trình duyệt (double-click). Dán email/văn bản, bấm Check Now.

### 10. (Test API nhanh bằng PowerShell)
```bash
Invoke-RestMethod -Uri http://127.0.0.1:5000/health
# hoặc
Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Body (ConvertTo-Json @{text="Test message"}) -ContentType "application/json"
```
