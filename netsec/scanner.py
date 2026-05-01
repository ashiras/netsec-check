import socket
import threading
from datetime import datetime
from rich.console import Console
from rich.progress import Progress

console = Console()

def scan_port(target: str, port: int, open_ports: list):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            console.print(f"[green][+] ポート {port} は開いています[/green]")
        sock.close()
    except:
        pass

def port_scanner(
    target: str,
    start_port: int = 1,
    end_port: int = 1024,
    max_threads: int = 100,
):
    console.print(f"[bold blue][{datetime.now()}] {target} のポートスキャンを開始...[/bold blue]")
    
    open_ports: list[int] = []
    threads: list[threading.Thread] = []
    
    with Progress() as progress:
        task = progress.add_task("[cyan]スキャン中...", total=end_port - start_port + 1)
        
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(target, port, open_ports))
            threads.append(t)
            t.start()
            
            if len(threads) >= max_threads:
                for t in threads:
                    t.join()
                threads.clear()
            
            progress.advance(task)
    
    # 残りのスレッドを待機
    for t in threads:
        t.join()
    
    if open_ports:
        console.print(f"\n[bold green]✅ オープンなポート: {sorted(open_ports)}[/bold green]")
    else:
        console.print("[yellow]オープンなポートは見つかりませんでした[/yellow]")
    
    console.print(f"[bold blue][{datetime.now()}] スキャン完了！[/bold blue]")