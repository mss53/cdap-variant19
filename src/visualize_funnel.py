import matplotlib.pyplot as plt

def visualize_sales_funnel():
    """Визуализация воронки продаж (вариант 19)"""
    stages = ['Посетители', 'Добавили в корзину', 'Начали оформление', 'Оплата']
    values = [10000, 4200, 1800, 950]
    
    plt.figure(figsize=(10, 6))
    plt.barh(stages, values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.xlabel('Количество клиентов')
    plt.title('Воронка продаж — Retail (Вариант 19)')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3)
    print("Воронка продаж визуализирована (заглушка)")
    plt.savefig('docs/funnel.png')

if __name__ == "__main__":
    visualize_sales_funnel()
