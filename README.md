Nama: Muhammad Zahran Affan

NPM: 2506586103

Kelas: PBP C

## Tugas 1
1. Saya menggunakan beberapa elemen semantik HTML5 dalam website, yakni:
<header> digunakan untuk bagian navbar yang berisi nama dan navigasi profile serta experience
<nav> digunakan untuk mengelompokkan link navigasi agar pengguna dapat berpindah ke bagian tertentu dalam website
<main> digunakan untuk membungkus bagian utama website
<section> digunakan untuk membagi konten utama menjadi bagian Profile, Experience, dan Achievement
<article> digunakan untuk setiap card pada bagian experience karena masing-masing card merupakan informasi yang berdiri sendiri mengenai suatu kegiatan
<footer> digunakan untuk bagian paling bawah website yang berisi informasi copyright
Saya tidak menggunakan <aside> karena pada website ini tidak ada konten tambahan yang terpisah dari konten utama.

2. Beberapa tantangan yang saya temukan ada pada ukuran dan posisi foto. Ketika layar diperkecil, foto profil awalnya ikut mengecil, padahal saya ingin fotonya tetap berukuran seperti semula dan berpindah ke bawah bagian identitas, bukannya malah mengecil. Saya kemudian menggunakan @media untuk mengubah layout menjadi satu kolom pada ukuran mobile. Saya juga sempat menyesuaikan penggunaan object-fit: cover pada foto karena beberapa foto menjadi terpotong, sedangkan jika menggunakan contain akan muncul ruang kosong. Dari situ saya mencoba menyesuaikan mana yang lebih cocok berdasarkan bentuk dan tujuan masing-masing foto.

3. Karena websitenya masih static, interaksi pada bagian Experience dan Achievement masih terbatas. Saat ini, card di situ hanya bisa digeser secara manual ke kiri dan kanan. Padahal, saya ingin menambahkan fitur dinamis berupa automatic carousel sehingga card pada fitur Experience dan Achievement bisa bergulir otomatis, tetapi tetap bisa dikontrol secara manual oleh pengguna. Selain itu, data card nantinya juga mungkin bisa dibuat lebih mudah diperbarui tanpa harus mengubah HTML satu per satu.

AI Disclosure: Saya menggunakan ChatGPT sebagai tools untuk belajar, diskusi, dan debugging selama pengerjaan. Pada bagian HTML, saya berdiskusi mengenai penggunaan elemen semantik seperti <section> dan <article> serta struktur card Experience dan Achievement. Saya juga beberapa kali meminta rekomendasi nama card yang cocok dan terasa formal untuk websitenya. Pada bagian CSS, saya menggunakan AI untuk memahami dan mencoba solusi terkait responsive layout, terutama saat foto profil ikut mengecil ketika layar diperkecil. Saya juga bertanya mengenai penggunaan object-fit berupa cover dan contain karena awalnya beberapa foto tidak tampil sesuai yang diinginkan. Selain itu, saya menggunakan AI untuk berdiskusi mengenai desain horizontal scrolling pada card Experience dan Achievement agar card dapat digeser ke kiri dan kanan menggunakan CSS. Saya juga meminta bantuan untuk mengecek kode yang redundan, seperti penggabungan @media yang sebelumnya tertulis dua kali. Setiap saran yang diberikan saya coba sendiri di kode dan sesuaikan kembali dengan desain yang saya inginkan.