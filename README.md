# automation-framework
Playwright Python automation test for SauceDemo

## Cấu trúc framework
pages/          - Page Object Model, locator và hàm theo từng màn hình
tests/          - Test cases phân chia theo chức năng
test_data/      - Dữ liệu test (JSON, CSV) tách riêng
utils/          - Helper đọc file data và constants
conftest.py     - Fixtures dùng chung

## Cách chạy test

```bash
# Cài thư viện
pip install -r requirements.txt
playwright install

# Chạy tất cả test
python3 -m pytest tests/ -v

# Chạy theo module
python3 -m pytest tests/login/ -v
python3 -m pytest tests/product/ -v
python3 -m pytest tests/cart/ -v
```

## Cách thêm test data

Thêm data vào `test_data/users.json`:
- Mở file users.json
- Thêm object mới với username và password
- Gọi trong test case bằng `load_json("users.json")`

## Cách áp dụng POM
- Locator khai báo trong `pages/` — không viết trong test case
- Test case chỉ gọi method từ Page Object
- Mỗi test tự chuẩn bị dữ liệu qua fixture trong `conftest.py`
- Các test không phụ thuộc nhau