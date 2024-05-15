# Pertanyaan Dasar

## Pertanyaan:
1. Jelaskan yang dimaksud dengan DevOps dan pentingnya DevOps!
2. Jelaskan peran dan keterlibatan seorang DevOps Engineer pada pengembangan aplikasi!
3. Jelaskan perbedaan Virtual Machine dan Docker!
4. Jelaskan apa yang dimaksud CI/CD!
5. Jelaskan jenis-jenis IP Address!

## Jawaban:
1. Devops merupakan singkatan dari Deployment and Operation. Devops merupakan sebuah prinsip developer untuk mengkoordinasikan antar tim yaitu tim development dengan tim operations dengan efektif dan efisien. Dengan adanya Devops ini, Tim operation atau development cukup mengkonfigurasi beberapa komponen yang dibutuhkan melalui prosedur yang dibuat. **DevOps** sangat penting karena dengan adanya role ini dapat memastikan bahwa proses pengembangan, pengujian, dan deployment aplikasi berjalan lancar dan konsisten. Selain itu dari dalam pengembangan suatu aplikasi dalam skala menengah ke besar, menurut saya hampir tidak mungkin jika tanggung jawab menyiapkan keperluan deployment dan coding ditanggung oleh role frontend atau backend sekaligus, kita perlu DevOps untuk mengatur dan bertanggung jawab mengenai hal tersebut dan devops ini adalah hal krusial.

2. Berdasarkan apa yang saya jelaskan diakhir jawaban nomor pertama, peran DevOps dalam pengembangan aplikasi sangat krusial karena DevOps engineer dapat membantu organisasi untuk merespons kebutuhan pasar dengan lebih cepat, meningkatkan kualitas perangkat lunak, dan memastikan bahwa aplikasi berjalan dengan stabil dan aman di lingkungan produksi. Tugas DevOps ini adalah menyiapkan **environment** seperti mengkonfigurasi, mengotomatisasi, dan mengelola infrastruktur dan memastikan konsistensi, efisiensi, dan skalabilitas aplikasi.

3. Dari segi fungsi Virtual Machine dirancang untuk memungkinkan beberapa sistem operasi berjalan pada satu mesin fisik. VM mengabstraksikan detail perangkat keras untuk memudahkan menjalankan aplikasi pada arsitektur perangkat keras yang berbeda dan menggunakan sumber daya perangkat keras secara lebih efisien. **Sementara itu,** docker dirancang untuk menyediakan cara yang ringan serta portabel untuk mengemas dan menjalankan aplikasi dalam lingkungan yang terisolasi dan dapat diproduksi kembali. Docker mengabstraksikan detail sistem operasi untuk mengatasi tantangan penerapan aplikasi di berbagai lingkungan, seperti pengembangan, pengujian, dan produksi. Docker mengatasi masalah ini melalui kontainerisasi.

   ![image](https://github.com/SetiaBudii/test-devops/assets/95162227/798d381e-a920-48e6-bfff-5888f2591919)

Sumber: https://s7280.pcdn.co/wp-content/uploads/2018/07/containers-vs-virtual-machines.jpg

  Secara sederhana berdasarkan gambar diatas saya bisa contohkan yakni perbedaan dari Virtual machine dan Docker. Virtual machine mmungkinkan satu sistem perangkat lunak bisa menjalankan banyak OS. Virtual Machine menggunakan mesin hardware untuk menjalankan beberapa sistem operasi lengkap secara simultan dengan bantuan hypervisor. Sedangkan Docker memungkinkan satu sistem operasi menjalankan banyak aplikasi dalam lingkungan yang terisolasi, secara sederhana mungkin bisa dibilang satu sistem operasi bisa berisi atau menjalankan banyak aplikasi.

4. CI/CD (Continuous integration / continuous deployment) meruapakan salah satu praktik DevOps yang digunakan untuk pengembangan perangkat lunak menjadi lebih terorganisir. CI/CD ini merupakan konsep yang mengubah pengerjaan proses yang tadinya manual menjadi otomatis. CI/CD ini mempunyai 3 tahapan yakni :
   - Continuous integration: proses mengkombinasikan sejumlah kode yang diintegrasikan ke repositori yang selanjutnya akan
     diuji secara otomatis.
   - Continuous delivery: proses membawa aplikasi ke delivery environment dan mempersiapkan segala hal yang dibutuhkan
     seperti database, infrastruktur, dan file penting lainnya.
   - Continuous deployment: proses pengujian lanjutan untuk mengecek kompatibilitas aplikasi dengan server. Apabila lancar,
     maka bisa segera di-deploy di server dan dirilis.
     
Dalam praktiknya ada banyak tools CI/CD yang dapat di gunakan. Namun sejauh ini saya hanya pernah menggunakan Jenkins dalam praktik CI/CD. Saya pernah menggunakan jenkins untuk menerapkan konsep CI/CD pada project yang telah saya kerjakan. Dengan menggunakan Jenkins dan Github Webhook memungkinkan saya untuk istilahnya mengambil perubahan dan build project secara otomatis ketikan ada ada perubahan code.
![image](https://github.com/SetiaBudii/test-devops/assets/95162227/ce7d0631-6491-4835-9f22-9a4d98db9593)
![image](https://github.com/SetiaBudii/test-devops/assets/95162227/9ee4836e-1474-489a-a395-d555bb6d5367)

5. Berdasarkan apa yang saya ketahui, secara umum ip address itu dibagi menjadi menjadi dua jenis yakni IPV4 dan IPV6.
   - IPV4: Menggunakan 4 oktet angka, dimana satu okte ini nantinya memiliki nilai maksimal yakni 255. IPV4 merupakan jenis
     yang umum digunakan karena bisa dibilang prefiksnya lebih sederhana dari IPV6. Berdasarkan apa yang saya ketahui, IPV4
     ini nantinya dibagi lagi menjadi 5 class yakni : Class A, Class, B, Class C, Class D, dan Class E. Semakin tinggi
     classnya maka semakin banyak kemungkinan perbedaan ip (makin banyak ip yang didapat) . Class A merupakan class
     tertinggi. Contoh penggunaannya: 192.168.1.10/24 → Class C.
     
   - IPV6: IPv6 adalah versi IP address yang bisa mencapai 128 bit. IPv6 ini ada untuk bisa menangani keterbatasan ip dari
     IPv4. IPV6 ini ditulis dalam rangkaian digit heksadesimal 16 bit dan huruf, dipisahkan oleh titik dua. Contoh
     penggunaan: 2001:3FFE:9D38:FE75:A95A:1C48:50DF:6AB8
     
   Selain itu  jika dilihat dari cakupan jaringannya terdapat dua jenis ip address yakni:
   - Private: Kumpulan ip address yang hanya dikenali pada satu topologi atau satu Local Area Network saja. Contohnya di
     suatu perusahaan bisa diterapkan suatu jaringan yang mempunyai rentang ip 192.168.1.1 - 192.168.1.255 dimana rentang ip
     tersebut hanya dikenali oleh device yang terkoneksi langsung dengan perangkat jaringan yang ada di dalam  LAN tersebut.

   - Public: Ip address yang bisa dikenali oleh public atau bisa dilihat melalui internet. Contoh penggunaannya menurut saya
     ada pada penggunaan internet dimana bisa dibilang handphone yang digunakan akan mendapatkan ip public dari masing
     masing provider.
   
   Terakhir berdasarkan apa yang saya ketahui jenis ip address bisa dilihat dari aspek alokasi dan durasi. Ada dua jeni
   yakni:
   - Static: ip address yang dialokasikan secara manual artinya durasi dan juga pengalokasiannya juga dilakukan secara
     manual.
   - Dinamis: ip address yang dialokasikan secara otomatis, biasanya ip dipetakan oleh suatu layanan dalam server yakni DHCP
     server. Dalam layanan DHCP ini server akan mengalokasikan ip kepada clientnya secara otomatis dan sekaligus bisa untuk
     mengatur berapa durasinya (Lease time).

