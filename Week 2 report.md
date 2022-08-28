# Week 2 report

## From: tuanlt24 (tuanlt26)

## **Phần 6. Passive information Gathering**  

Là quá  trình thu thập các thông tin của đối tượng mà không có sự tác động vào đối tượng.  

Quá trình này là một quá trình "xoay vòng" bởi bước sau được xác định bởi output của bước trước  
Mục đích chính của quá trình passive gathering là dùng để làm rõ hoặc mở rộng các mục tiêu có thể tấn công. Và cung cấp những thông tin hỗ trợ cho các bước Phising hoặc Password Guessing

### **Phân loại về định nghĩa thu thập bị động**  

Có 2 trường phái chính:  

1. Trường phái cổ điển vị kỷ: Không có tiếp xúc với mục tiêu, hoàn toàn là sử dụng các công cụ bên thứ ba  
\+ Giữ bí mật cho các hành vi cao  
\- Thu thập được ít thông tin

2. Trường phái tân tiến: Có thể tiếp xúc với mục tiêu nhưng chỉ với "vai trò" là một người dùng rất bình thường.  
\+ \- Ngược lại với ý trên

Tuy nhiên định nghĩa về tiếp cận là không cần thiết bởi tuỳ vào mục tiêu mà cần tuân thủ những phương pháp khác nhau. Và quá trình passive gathering cũng không phải là một quá trình hoàn toàn bắt buộc.  

### **6.1 Taking note**  

Các thông tin trong quá trình thu thập nên được ghi chú theo format và chi tiết để dễ dàng tìm kiếm trong các bước sau này  

### **6.2 Website recon**  

Xem xét website (nếu có) của mục tiêu để có những cái nhìn tổng quan về mục tiêu  

#### **6.3 whois**  

TCP tool, là 1 db, cung cấp thông tin về: domain name(nameserver, registrar)  
Cách sử dụng:  
```whois <ip>```  
Có thể chú ý các thông tin về: Người đăng ký tên miền, Name server,...  

Crcx@grd1363

### **6.4 Google hacking**

Sử dụng những câu truy vấn "sáng tạo" để tìm kiếm những bản ghi có giá trị.  

***site***: search domain  
***filetype***: search theo loại file
.... more research  

### **6.5 netcraft**  

...  

### **6.6 recon-ng**  

Một module-based framework để thu thập thông tin của web-based.  
Các kết quả trước sẽ update thông tin cho các modules sau.  

search tools:  
```marketplace search github```

lấy thông tin của tools  
```marketplace info recon/domains-hosts/google_site_web```

cài đặt thông tin  
```marketplace install recon/domains-hosts/google_site_web```

cài đặt modules  
```marketplace install recon/domains-hosts/google_site_web```

load modules  
```modules load recon/domains-hosts/google_site_web```

show info of modules  
```info```

cài đặt thông tin các options  
```options set SOURCE <ip>```

run tools  
```run```

### **6.7 Open-source code**

tìm kiếm trong github, tìm với  
```filename:users```
Tìm kiếm các file có users trong tên.  

### **6.8 shodan**

### **6.9 Security headers scanner**

Có mấy trang web cho scan header  
<https://securityheaders.com/>  

### **6.10 SSL server test**  

So sánh cài đặt ssl/tls giữa trang web và cài đặt tốt nhất.  

### **6.11 Pastebin**  

...

### **6.15 Information gathering frameworks**

<https://osintframework.com/>

## phần 7: Active information Gathering

### 7.1 DNS Enumeration

NS - tên của máy chủ có quyền lưu trữ bản ghi DNS cho một tên miền  
A - chứa IP của 1 hostname  
MX - Mail exchange chứa tên của server chịu trách nhiệm cho việc xử lý mail cho domain. 1 domain có thể chứa nhiều MX records.  
PTR - pointer records chứa tên domain của 1 địa chỉ ip.  
CNAME -  
TXT - Text record chứa thông tin bất kì, được dùng cho nhiều mục đích khác nhau  

#### 7.1.6 relevant tools  

##### dnsrecon  

```bash
dnsrecon -d <ip> -t axfr 
-d: ip  
-t: xác định loại của liệt kê sẽ thực hiện 
...
```

##### dnsenum  

Cách dùng: `dnsenum \<ip\>`

### 7.2 Port Scanning  

Quét các cổng TCP, UDP để phát hiện các dịch vụ đang chạy trên máy remote  

#### **TCP scanning**  

`nc -nvv -w 1 -z <ip> <from port - to port>`

-w: connection timeout in seconds  
-z: chế độ zero-I/O.  

#### **UDP scanning**  

`nc -nv -u -z -w 1 <ip> <from port - to port>`  
-u: udp scan

#### Port scanning with Nmap  

Account for our traffic :
Khi nmap scan 1000 port thường được sử dụng nhiều nhất.
Dùng iptables để theo dõi khối lượng gói được gửi bởi loại scan này.  

```bash
sudo iptables -I INPUT 1 -s ip -j ACCEPT
sudo iptables -I OUTPUT 1 -d 10.11.1.220 -j ACCEPT
sudo iptables -Z

-I: thêm 1 luật mới vào chuỗi đã có
    ví dụ: INPUT, OUTPUT
-s: địa chỉ ip nguồn
-d: địa chỉ ip đích
-j ACCEPT: chấp nhận gói đi qua.
-z: reset bộ đếm gói và byte trong chuỗi thành 0  
-v: verbose output
-n: numeric output
-L: list the rule hiện tại trong chains
```

**Stealth/SYN scanning:**
SYN là kĩ thuật scan được yêu thích nhất.  
Có nhiều lợi ích:  

- Là kỹ thuật scan mặc định và để thực thi thì user cần có quyền gửi các gói raw sockets.  
- Raw socket: có thể xác định từng phần của 1 gói tin, cả header và payload của tất cả các tầng từ L2. So sánh với non-Raw socket chỉ có thể chỉnh sửa payload trên lớp transport.  
- Kỹ thuật này gửi các gói tin SYN đến tất cả các port và không hoàn thành việc bắt tay theo giao thưc TCP. Nó nhận gói SYN-ACK trả về nếu port được mở và không quan tâm gói ACK được gửi hay không.  
- Bởi vì quá trình bắt tay không thành công nên hành vi này sẽ không được gửi đến lớp ứng dụng nên sẽ không xuất hiện trong log của ứng dụng.  
- Nhanh và hiệu quả bởi vì ít các gói được gửi và nhận.  

**TCP connect scanning:**  

- Khi user không có quyền raw socket. Nmap thực hiện kết nối theo giao thức tcp mặc định.  
- Vì cần đợi các kết nối xác nhận nên thời gian hoàn thành lâu.  
Cách dùng:
`nmap -sT ip`

**UDP scanning:**  

- kết hợp 2 kĩ thuật khác nhau: gửi các gói ICMP mặc định và gửi các gói riêng biệt theo từng giao thức cụ thể trên các port cụ thể.  
- sudo required  
Cách dùng:
`nmap -sU ip`  

kết hợp bằng cách sử dụng -sU và -sS để lấy được tất cả các cổng tcp và udp:
`nmap -sU -sS ip`  

**Network sweeping:**  

Cách dùng:
`nmap -sn 192.168.1.1-254 -oG output_file.txt`  

Tìm kiếm các host up:  
`grep Up output_file.txt | cut -d " " -f 2`  

Quét trên 1 port nhất định:
`nmap -p [port] [ip].1-254 -oG file.txt`  

Quét trên 1 số lượng port phổ biến thay vì 1000 port phổ biến như mặc định:
`nmap --top-port [số lượng]`  

Quét tất cả các option sau: os version, script scanning , tracerout
`nmap -A`

**Banner grabbing/service numeration:**  

-sV: service banners  
-A: service enumeration  

**Nmap scripting engine (NSE):**  

- Dùng các script để tự động các task scanning. Các scripts này thực hiện nhiều loại chức năng như: DNS enumeration, brute force attacks, xác thực vulnerable.  
- Chứa trong thư mục: /usr/share/nmap/scripts  
- `--script-help <tên script>` để xem hướng dẫn sử dụng của scripts.  
