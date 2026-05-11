import random


def gen_event():
    players = ['Alice', 'Bob', 'Charlie', 'David']
    actions = ['score', 'assist', 'rebound', 'steal']

    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(events):
    while len(events) > 0:
        item = random.choice(events)
        events.remove(item)
        yield item


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for event in range(1000):
        player, action = next(event_generator)
        print(f"Event {event}: Player {player} did action {action}")

    lst = []
    for i in range(10):
        lst.append(next(event_generator))

    print(f"Built list of {len(lst)} events: {lst}")

    for item in consume_event(lst):
        print(f"Got event from list: {item}")
        print(f"Remains in list: {lst}")