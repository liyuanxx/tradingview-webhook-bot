from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 你的 LINE Notify 權杖 (pzpApER45aPOW5kfqZC8AvqxLoxYlo6ebtQMuhhPTmw)
LINE_NOTIFY_TOKEN = "pzpApER45aPOW5kfqZC8AvqxLoxYlo6ebtQMuhhPTmw"

# 發送 LINE 訊息的函式
def send_line_message(message):
    headers = {"Authorization": f"Bearer {pzpApER45aPOW5kfqZC8AvqxLoxYlo6ebtQMuhhPTmw}"}
    data = {"message": message}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)

    # 解析 TradingView 訊號
    symbol = data.get("symbol", "Unknown")
    side = data.get("side", "Unknown")  # "buy" 或 "sell"
    price = data.get("price", "Unknown")
    tp1 = data.get("tp1", "Unknown")
    tp2 = data.get("tp2", "Unknown")
    tp3 = data.get("tp3", "Unknown")
    sl = data.get("sl", "Unknown")
    strategy = data.get("strategy", "前日K + 均線 + RSI + 成交量")

    # 設定報單訊息格式
    message = f"幣種: {symbol}\n方向: {side.upper()}\n進場價位: {price}\nTP1: {tp1}\nTP2: {tp2}\nTP3: {tp3}\nSL: {sl}\n使用指標: {strategy}"

    # 發送 LINE 訊息
    send_line_message(message)

    return jsonify({"status": "success", "message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


