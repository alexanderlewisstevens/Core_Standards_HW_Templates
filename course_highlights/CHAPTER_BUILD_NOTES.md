# Course Highlights Build Modes

- Full compendium: `latexmk -pdf course_highlights_compendium.tex`
- Single chapter wrappers:
  - `latexmk -pdf course_highlights_chapter_01_foundations.tex`
  - `latexmk -pdf course_highlights_chapter_02_sets_functions_sequences_sums_matrices.tex`
  - `latexmk -pdf course_highlights_chapter_03_algorithms.tex`
  - `latexmk -pdf course_highlights_chapter_04_number_theory_cryptography.tex`
  - `latexmk -pdf course_highlights_chapter_05_induction.tex`
  - `latexmk -pdf course_highlights_chapter_06_counting.tex`
  - `latexmk -pdf course_highlights_chapter_07_discrete_probability.tex`

Chapter source files live in `chapters/` and are included by the compendium.
