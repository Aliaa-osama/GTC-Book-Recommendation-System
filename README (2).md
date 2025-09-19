# BRS – Data Preprocessing Notes

## books.csv

- **ID columns:**

  - `id` → Main dataset identifier.  Keep.
  - `goodreads_book_id`, `best_book_id`, `work_id` → External Goodreads references.  Drop unless cross-referencing.

- **books\_count:** Number of editions. Not relevant.  Drop.

- **isbn, isbn13:** Book identifiers. Many missing.  Drop.

- **title vs original\_title:**

  - `title` = edition-specific title.
  - `original_title` = canonical/original version.
    → Keep one (preferably `original_title`).

- **average\_rating, ratings\_count, work\_ratings\_count, work\_text\_reviews\_count:**

  - `average_rating` = mean user rating.  Useful.
  - `ratings_count` = ratings for this edition.
  - `work_ratings_count` = ratings across all editions.  More robust.
  - `work_text_reviews_count` = text reviews. Optional.

- **rating\_1 … rating\_5:** Raw counts of ratings by star value.  Could be normalized into distributions.

- **image\_url:** Useful for UI/web app (not model).  Keep separately.

---

## ratings.csv

- `user_id`, `book_id`, `rating`
- **book\_id → corresponds to ********`id`******** in books.csv.**
- This is the **core user–item interaction dataset** for collaborative filtering.

---

## to\_read.csv

- Represents users’ wishlists.
- `book_id` again matches `id` in books.csv.
- Can be used for **implicit feedback** (interest without rating).

---

## book\_tags.csv & tags.csv

- **tags.csv:** Dictionary of `tag_id` → `tag_name` (e.g., “fantasy”, “romance”).

- **book\_tags.csv:** Links `goodreads_book_id` → `tag_id` + `count` (frequency of user tagging).

---

## Preprocessing Action Plan

1. **Keep ********`id`******** as main book identifier.**
2. **Drop redundant/noisy columns** (`books_count`, `isbn`, etc.).
3. **Decide on text fields** (`original_title` preferred).
4. **Clean and merge datasets:**
   - Merge ratings with books.
   - Map tags through book\_tags + tags.
5. **Feature engineering:**
   - Create book–tag matrix.
   - Normalize ratings distributions if needed.
   - Build user profiles (from ratings & tags).
6. **Provide cleaned data** to model training team.

---
