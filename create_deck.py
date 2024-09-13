import json
from pathlib import Path
import genanki  # type: ignore


# MODEL_ID = random.randrange(1 << 30, 1 << 31)
# Unique values
MODEL_ID = 1607392319
DECK_ID = 2059400110
data = Path(__file__).resolve().parent / "data"


def create_model(hide_extra_fields: bool = True) -> genanki.Model:
    show_hide_script = """
<script>
var button = document.getElementById('toggleButton');
var extra = document.getElementById('extraContent');
button.addEventListener('click', function() {
  if (extra.style.display === 'none') {
    extra.style.display = 'block';
    button.textContent = 'Hide Translation and Answer';
  } else {
    extra.style.display = 'none';
    button.textContent = 'Show Translation and Answer';
  }
});
</script>
"""

    back_template = """
{{FrontSide}}

<hr id="answer">

<div>{{Example Sentence}}</div>
"""

    if hide_extra_fields:
        back_template += (
            """
<button id="toggleButton">Show Translation and Answer</button>

<div id="extraContent" style="display: none;">
  <h3>Translation</h3>
  <div>{{Translation}}</div>
  <h3>Answer</h3>
  <div>{{Answer}}</div>
</div>
"""
            + show_hide_script
        )
    else:
        back_template += """
<h3>Translation</h3>
<div>{{Translation}}</div>
<h3>Answer</h3>
<div>{{Answer}}</div>
"""

    return genanki.Model(
        MODEL_ID,
        "German Vocabulary Model",
        fields=[
            {"name": "Word"},
            {"name": "Example Sentence"},
            {"name": "Translation"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Word}}",
                "afmt": back_template,
            },
        ],
        css="""
.card {
  font-family: arial;
  font-size: 20px;
  text-align: left;
  color: black;
  background-color: white;
}

#toggleButton {
  margin-top: 10px;
  padding: 5px 10px;
  font-size: 16px;
}

#extraContent h3 {
  margin-top: 15px;
  margin-bottom: 5px;
}
""",
    )


def load_notes_from_json(file_path: Path, model: genanki.Model) -> list[genanki.Note]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    notes = []
    for item in data:
        note = genanki.Note(
            model=model,
            fields=[
                item["Word"],
                item["Example Sentence"],
                item["Translation"],
                item["Answer"],
            ],
            guid=genanki.guid_for(item["Word"], item["Example Sentence"]),
        )
        notes.append(note)
    return notes


def main() -> int:
    my_model = create_model(hide_extra_fields=True)
    my_deck = genanki.Deck(DECK_ID, "Schritte_Plus_A2.1")

    for json_file in (data / "a2.1").rglob("*.json"):
        notes = load_notes_from_json(json_file, my_model)
        for note in notes:
            my_deck.add_note(note)

    package = genanki.Package(my_deck)
    package.write_to_file(data / "A2.1_schritte_plus.apkg")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
