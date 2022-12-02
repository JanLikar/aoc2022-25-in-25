(use 'clojure.java.io)
(require '[clojure.string :as str])

(defn shape-score [shape] (
    case shape
        "A" 1
        "B" 2
        "C" 3
        0
))

(defn beater [move] (
    case move
        "A" "B"
        "B" "C"
        "A"
))

(defn move-to-play [line] (
    let [outcome (second line) theirs (first line)]
    (case outcome
        "X" (beater (beater theirs))
        "Y" theirs
        (beater theirs))
))

(defn outcome-score [line] (
    case (second line)
        "X" 0
        "Y" 3
        6
))

(defn score [line] (+ (shape-score (move-to-play line)) (outcome-score line)))


(def total_score 0)

(with-open [rdr (reader "input.txt")]
  (doseq [line (line-seq rdr)]
    (def total_score (+ total_score (score (str/split line #" "))))
    ))

(println total_score)
