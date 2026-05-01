import requests
import socket
from rich.console import Console
from datetime import datetime

console = Console()

def get_public_ip():
    """パブリックIPを取得"""
    try:
        # IPv4
        ipv4 = requests.get("https://api.ipify.org", timeout=5).text
        # IPv6
        ipv6 = requests.get("https://api6.ipify.org", timeout=5).text
        return ipv4, ipv6
    except:
        return None, None

def check_port_from_outside(host: str, port: int, timeout=3):
    """外側からポートが開いているか簡易チェック"""
    try:
        sock = socket.socket(socket.AF_INET6 if ':' in host else socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def public_check():
    console.print("[bold blue][外側チェック] 開始...[/bold blue]")
    
    ipv4, ipv6 = get_public_ip()
    
    if ipv4:
        console.print(f"🌐 パブリック IPv4: [cyan]{ipv4}[/cyan]")
    if ipv6:
        console.print(f"🌐 パブリック IPv6: [cyan]{ipv6}[/cyan]")

    check_ports = [80, 443, 53, 22, 3389]
    console.print("\n[bold]外側からポート開放チェック中...[/bold]")
    
    for port in check_ports:
        # IPv4でチェック（IPv6はNATの問題で難しいため簡易的に）
        open = check_port_from_outside(ipv4 or ipv6, port)
        status = "[red]OPEN（危険）[/red]" if open else "[green]CLOSED（安全）[/green]"
        service = {80:"HTTP", 443:"HTTPS", 53:"DNS", 22:"SSH", 3389:"RDP"}.get(port, "")
        console.print(f"ポート {port:>4} ({service}) → {status}")
    
    console.print("\n[bold green]※ 注意: Pythonからの外側チェックは精度が100%ではありません[/bold green]")
    console.print("より正確に知りたい場合は https://port.tools などを併用してください")
