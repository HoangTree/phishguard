Here's how to run it:

1. Gỡ Python 3.13 (nếu muốn)
Settings → Apps → tìm Python → Uninstall
(Không bắt buộc nhưng khuyên dùng Python 3.11 để tránh lỗi dependency.)

2. Cài Python 3.11
Tải installer Python 3.11 (từ python.org). Khi cài: tick “Add Python to PATH”.

3. Mở PowerShell trong thư mục project rồi tạo môi trường ảo:

python -m venv .venv

4. Kích hoạt venv:

.\.venv\Scripts\Activate
(bạn sẽ thấy prompt chuyển sang (.venv))

5. Cập nhật pip/setuptools/wheel:

python -m pip install --upgrade pip setuptools wheel

6. Cài tất cả dependency bằng file:

python -m pip install -r requirements.txt
(Trên Python 3.11, lệnh này sẽ cài numpy, scikit-learn, pandas, flask, v.v. bình thường.)

7. Huấn luyện model (tạo file phishguard_pipeline.joblib):

python train.py

Bạn sẽ thấy output accuracy và file phishguard_pipeline.joblib được lưu.

8. Chạy server Flask:

python app.py
Mục tiêu: bạn nên thấy * Running on http://127.0.0.1:5000

9. Mở giao diện: mở frontend/index.html trong trình duyệt (double-click). Dán email/văn bản, bấm Check Now.

10. (Test API nhanh bằng PowerShell)

Invoke-RestMethod -Uri http://127.0.0.1:5000/health
# hoặc
Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Body (ConvertTo-Json @{text="Test messag
