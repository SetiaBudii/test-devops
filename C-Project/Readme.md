1. Clone repository : https://github.com/SetiaBudii/test-devops.git
2. Buka folder hasil clone melalui IDE (contoh Vscode) lalu masuk ke direktori cd C-Project
3. Jalankan perintah sudo docker-compose up  --build atau sudo docker-compose up -d --build
4. Jika langkah nomor 5 selesai buka halaman minIO (http://localhost::9001/login ) lalu masukan username “minio_user” dan password “minio_pwd”
   note: untuk username dan password bisa dilihat di file docker-compose.yml
5. Pergi menu access key dan buat access key baru dengan menekan tombol “Create access key”
6. Isikan field yang tersedia seperti tanggal expire, name dan lain-lain dan jika sudah klik create
7. Pergi ke menu bucket dan buat bucket baru dengan menekan tombol Create bucket lalu isikan nama bucket yang ingin digunakan. Jika sudah klik Create.
8. Kembali ke terminal server, masukan perintah docker-compose down dan setting ulang docker-compose.yml dengan memasukan nama bucket, access key, dan secret key yang telah dibuat tadi di minIO.
9. Compose up lagi  semua service menggunakan perintah docker-compose up --build
10. Buka halaman mlflow ui lewat url “localhost:5000”
11. Untuk membuka database bisa melalui pgadmin dengan memasukan url berikut : “localhost:5050”
12. Masukan username “admin@admin.com” dan password “admin” saat login.
13. Create server baru dan masukan nama server, address port dan field lainnya seperti gambar dibawah:
14. Sampai disini mlflow ,minIO dan database sudah dapat diakses.
15. Untuk langkah selanjutnya merupakan test salah satu folder example. Contohnya disini akan mengetes sklearn_elasticnet_diabetes.
16. Untuk mengetes-nya disini saya menggunakan metode bash untuk mengakses secara langsung docker image mlflow_server. Pertama jalankan perintah sudo docker ps dan cari nama container dari mlflow_server.
17. Jika nama kontainer sudah didapat maka jalankan perintah “sudo docker exec -it <nama_kontainer>  /bin/bash” untuk membuka folder atau menjalankan bash pada container. Contoh “sudo docker exec -it mlflow_server  /bin/bash”
18. Selanjutnya buka direktori dari folder contoh yang ingin dijalankan berada menggunakan perintah “cd file/examples/sklearn_elasticnet_diabetes/linux”
19. Jalankan file train_diabetes.py menggunakan python dengan memasukan perintah “python train_diabetes.py”
20. Jika proses selesai maka bisa dilihat hasilnya seperti berikut:
21. Selanjutnya untuk melihat dari tracker atau mlflow ui  buka kembali “localhost:5000” maka secara otomatis contoh eksperimen yang dijalankan akan muncul.
    
