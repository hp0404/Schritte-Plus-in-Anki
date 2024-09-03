# **Task Overview**
Your task is to manually transcribe the vocabulary words and their corresponding example sentences from the provided image. You will create a structured table for each vocabulary word with four specific columns. The goal is to accurately reflect the vocabulary list and example sentences, ensuring the data is well-organized and insightful.
## Required Columns:
1. **Word**: The German vocabulary word (and all its related parts and forms) as it appears on the left side of the image.
2. **Translation**: The English translation of the word, based on the context provided in the example sentence.
3. **Example Sentence**: The example sentence from the right side of the image, with the vocabulary word (and all its parts if the word is separable) replaced by an underscore.
4. **Answer**: The original vocabulary word that was replaced by the underscore in the example sentence.
## Output Format:
The output should be a structured JSON array where each vocabulary word and its associated details are represented as an object. Below is an example of how the output should be formatted:
Output format structure:
```json
[
  {
    "Word": "weil",
    "Translation": "because",
    "Example Sentence": "(H) Ich bin traurig, (N) ______ ich hier keinen Menschen kenne.",
    "Answer": "weil"
  }
]
```

You may only respond in JSON format, as shown in the output format structure. Do not add any comments before or after the JSON object.

Input data:\n