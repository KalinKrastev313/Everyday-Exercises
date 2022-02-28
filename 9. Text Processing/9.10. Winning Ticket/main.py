tickets = input().split(", ")
ticket_value = False
for ticket in tickets:
    if len(ticket) == 20:
        first_half, second_half = ticket[:10], ticket[10:]
        for index in range(5):
            len_sequence = first_half.count(first_half[index])
            if len_sequence >= 6:
                sequence = first_half[index:index + len_sequence]
                if len(set(sequence)) == 1:
                    # Might be edited for cases when sequence in first half is longer than sequence in second half
                    if sequence in second_half:
                        print(f'ticket "{ticket}" - {len_sequence}{first_half[index]}', end="")
                        if len_sequence == 10:
                                print(" Jackpot!")
                        ticket_value = True
                        break
    if not ticket_value:
        print("invalid ticket")
    else:
        ticket_value = False