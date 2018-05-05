from puncpy.tagger import Tagger


def run_tagger():
    tagger = Tagger('It\'s getting harder')
    tagged_text = tagger.tag_text()
    return tagged_text


items = run_tagger()

for item in items:
    print('item from tagged text :: {}'.format(item))
