def naive_methods(data):
    x = data.groupby('TimeOfDay')
    print("day:")
    print("mean", round(x.mean().loc['day', 'CountRate'], 0))
    print("standard variation", round(x.std().loc['day', 'CountRate'], 0))
    print("maximum", round(x.max().loc['day', 'CountRate'], 0))
    print("minimum", round(x.min().loc['day', 'CountRate'], 0))

    print("\nnight:")
    print("mean", round(x.mean().loc['night', 'CountRate'], 0))
    print("standard variation", round(x.std().loc['night', 'CountRate'], 0))
    print("maximum", round(x.max().loc['night', 'CountRate'], 0))
    print("minimum", round(x.min().loc['night', 'CountRate'], 0))
