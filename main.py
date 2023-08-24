import sys, is_haiku, create_haiku, get_examples

# args = sys.argv
# arg = args[1]
# is_haiku.main(haiku)
examples = get_examples.main()
haiku = create_haiku.main(examples=examples)
# print(haiku)
generated_haiku_is_haiku = is_haiku.main(haiku)

