# 🛡️ netsec-check

**Python + uv で作るシンプルで美しいネットワークセキュリティチェックツール**

内側（LAN内）と外側（インターネット側）の両方を1つのCLIでサクッと確認できる、  
セキュリティ意識の高い人向けの軽量ツールです。

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![uv](https://img.shields.io/badge/uv-0.5+-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ 主な機能

- **内側スキャン** (`scan`)：自分のネットワーク内で開いているポートを高速検出
- **外側チェック** (`public-check`)：インターネット側から自分のポートがどう見えているかを確認
- Rich を使った見やすいカラー出力
- uv 対応で爆速インストール＆起動

---

## 🚀 インストール（超簡単）

```bash
# 1. リポジトリをクローン
git clone https://github.com/yourname/netsec-check.git
cd netsec-check

# 2. 依存関係インストール
uv sync

# 3. インストール完了
uv run netsec --help
```

## 使い方

### 1. 内側（LAN内）スキャンbash

```bash
# 基本
uv run netsec scan 192.168.11.1

# 詳細指定
uv run netsec scan 192.168.11.1 --start 1 --end 1000 --threads 200
```

### 2. 外側（インターネット）チェック ★新機能bash

```bash
uv run netsec public-check
```

#### 出力例

```text
🌐 パブリック IPv4: 180.26.228.143
🌐 パブリック IPv6: 2400:4153:9923:ee10:d9:69e1:7e69:adc3

外側からポート開放チェック中...
ポート   80 (HTTP)   → CLOSED（安全）
ポート  443 (HTTPS) → CLOSED（安全）
ポート   53 (DNS)   → CLOSED（安全）
```

---

## コマンド一覧bash

```bash
uv run netsec --help
```

---

## 注意事項（必ず読んでください）自分のネットワーク、または明確な許可を得た対象に対してのみ使用してください。

- 無許可での他者ネットワークへのスキャンは違法行為になる可能性があります。
- 外側チェックは簡易版です。より正確に知りたい場合は port.tools などを併用してください。

---

## 将来の拡張予定サービス名・バージョン検知

- HTMLレポート出力
- Slack/メール通知機能
- Wi-Fiセキュリティチェック

---

## License

MIT License
