if __name__ == '__main__':
    name = 'Mississipi'
    i_counter = 0
    m_counter = 0

    for i in name:
        if i == 'i':
            i_counter += 1
        if i == 's':
            m_counter += 1

    print(i_counter, m_counter)
