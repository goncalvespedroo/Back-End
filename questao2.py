def q2_contar_frequencia_palavra(text):
    words = text.lower().split()
    
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    order_frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    
    return order_frequency

print(q2_contar_frequencia_palavra("Hello world hello"))

