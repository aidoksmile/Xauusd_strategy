from signals.signaler import analyze_and_signal
import time

def main():
    while True:
        analyze_and_signal()
        time.sleep(60)  # Запуск каждые 60 секунд

if __name__ == "__main__":
    main()