import typer
from netsec.scanner import port_scanner
from netsec.public_checker import public_check as public_check_func  # ← 別名でimport

app = typer.Typer(
    help="ネットワークセキュリティチェックツール",
    rich_markup_mode="rich",
    add_completion=False,
    no_args_is_help=True,
)

@app.command()
def scan(
    target: str = typer.Argument(..., help="対象IPまたはホスト名"),
    start: int = typer.Option(1, "--start", "-s", help="開始ポート"),
    end: int = typer.Option(1024, "--end", "-e", help="終了ポート"),
    threads: int = typer.Option(100, "--threads", "-t", help="同時スレッド数"),
):
    """内側（LAN内）からポートスキャンを実行"""
    port_scanner(target, start, end, threads)

@app.command()
def public_check():
    """外側（インターネット）からのポート開放状況をチェック"""
    public_check_func()   # ← ここを別名にした関数を呼ぶ

if __name__ == "__main__":
    app()
