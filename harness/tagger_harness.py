from puncpy.tagger import Tagger


def run_tagger():
    stop_words = []
    tagger = Tagger(stop_words)
    tagged_text = tagger.tag_text('It\'s getting harder')
    return tagged_text


items = run_tagger()

for item in items:
    print('item from tagged text :: {}'.format(item))
