
# 🧠 TL;DR:
# You're absolutely correct: threading doesn’t help with CPU-bound tasks in Python because of the GIL.
# re.search() is CPU-bound, and threads don’t run in parallel (in CPython).
# So, Python threads won't speed up CPU-bound search — and won’t improve time complexity either.


# ✅ If you want true parallelism for CPU-bound tasks, use multiprocessing, not threading.
# ✅ So Why Did We Use Threads Then?
# Mainly because:
    # It's simpler to explain concurrency and thread-safe access patterns.
    # If you imagine:
        # The documents were coming in at runtime
        # The searching operation was I/O-bound (e.g., reading large files from disk or network)
        # ...then threads would help.
    # But you're 100% right — in our current example:
        # All documents are in memory
        # Search is re.search (CPU-bound string scanning)
        # No file or network I/O
        # ➡️ So threading doesn't help — and might even add slight overhead.


import re
import threading


class DocumentSearch:
    def __init__(self):
        self.documents = []
        self.lock = threading.Lock()  # To safely add new documents

    def add_document(self, text: str):
        with self.lock:  # Lock only for writing
            self.documents.append(text)

    def search(self, pattern: str):
        """Search for a pattern (phrase or regex) in all documents"""
        results = []

        def search_in_doc(doc_id, text):
            if re.search(pattern, text, re.IGNORECASE):
                results.append((doc_id, "MATCH"))

        threads = []
        for idx, doc in enumerate(self.documents):
            t = threading.Thread(target=search_in_doc, args=(idx, doc))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

        return results


if __name__ == "__main__":
    ds = DocumentSearch()

    ds.add_document("Pattern matching is fun and powerful.")
    ds.add_document("We study string algorithms in computer science.")
    ds.add_document("This document does not mention matching.")
    ds.add_document("Machine learning uses pattern recognition.")

    pattern = "pattern matching"
    matches = ds.search(pattern)

    print("Search Results:")
    for doc_id, _ in matches:
        print(f"Match found in document {doc_id}")









