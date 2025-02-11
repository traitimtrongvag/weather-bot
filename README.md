# weather-bot

Weather Bot là một bot đơn giản giúp bạn tra cứu thông tin thời tiết hiện tại và dự báo thời tiết cho các thành phố trên toàn thế giới. Bot sử dụng API từ OpenWeatherMap để lấy dữ liệu thời tiết và cung cấp thông tin bằng tiếng Việt.

## Tính năng

- **Xem thời tiết hiện tại**: Nhận thông tin thời tiết hiện tại cho một thành phố cụ thể.
- **Xem dự báo thời tiết**: Nhận dự báo thời tiết trong 5 ngày tới cho một thành phố cụ thể.
- **Đặt thành phố mặc định**: Đặt một thành phố mặc định để không cần nhập lại tên thành phố mỗi khi tra cứu thời tiết.

## Cách sử dụng

1. **Bắt đầu**: Gửi lệnh `/start` để bắt đầu sử dụng bot.
2. **Xem thời tiết hiện tại**: Gửi lệnh `/weather <tên thành phố>` để xem thời tiết hiện tại. Nếu bạn đã đặt thành phố mặc định, chỉ cần gửi `/weather`.
3. **Xem dự báo thời tiết**: Gửi lệnh `/forecast <tên thành phố>` để xem dự báo thời tiết trong 5 ngày tới. Nếu bạn đã đặt thành phố mặc định, chỉ cần gửi `/forecast`.
4. **Đặt thành phố mặc định**: Gửi lệnh `/setcity <tên thành phố>` để đặt thành phố mặc định.

## Cài đặt

1. **Yêu cầu**:
   - Python 3.7 trở lên
   - Các thư viện cần thiết: `aiohttp`, `python-telegram-bot`

2. **Cài đặt các thư viện**:
   ```bash
   pip install aiohttp python-telegram-bot
   ```

3. **Cấu hình**:
   - Tạo một file `.env` và thêm các biến môi trường sau:
     ```plaintext
     API_KEY=<YOUR_OPENWEATHERMAP_API_KEY>
     BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
     ```
   - Thay thế `<YOUR_OPENWEATHERMAP_API_KEY>` và `<YOUR_TELEGRAM_BOT_TOKEN>` bằng API key của bạn từ OpenWeatherMap và token của bot Telegram.

4. **Chạy bot**:
   ```bash
   python bott.py
   ```

## Đóng góp

Nếu bạn muốn đóng góp vào dự án, vui lòng tạo một pull request. Mọi đóng góp đều được hoan nghênh!



