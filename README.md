# CV
# Dùng tập dữ liệu: cifar10
# Sử dụng: color histogram

Bước 1: Chia tập dữ liệu

python dividedataset.py --dataset_test <Tên folder tập test> --dataset_train <Tên folder tập train>
Ví dụ: python dividedataset.py --dataset_test test --dataset_train train
(Bước này để lấy ảnh từ tập cifar10, chia thành 2 tập train,test và lưu vào máy tính)
ảnh trong tập train: i_train.png ( i = 0 .... 799)
ảnh trong tập test: i_test.png ( i = 0 .... 299)

Bước 2: Tính đặc trưng với từng ảnh trong tập train và lưu vào file index.csv

python index.py --dataset <Tên folder tập train> --index index.csv
Ví dụ: python index.py --dataset train --index index.csv

Bước 3: Retrieve image

python search.py --index index.csv --query <đường dẫn ảnh trong tập test> --result-path <Tên folder tập train> --limit <Số lượng ảnh trả về>
Ví dụ: python search.py --index index.csv --query test/0_test.png --result-path train --limit 5



