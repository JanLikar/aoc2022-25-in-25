(use 'clojure.java.io)
(require '[clojure.string :as str])

(defn shape-score [line]
    (case (second line)
        "X" 1
        "Y" 2
        "Z" 3
        0
))

(defn xyz-to-abc [move]
    (case move
        "X" "A"
        "Y" "B"
        "C"
))

(defn beats? [m n]
    (or
        (and (= m "A") (= n "C"))
        (and (= m "B") (= n "A"))
        (and (= m "C") (= n "B"))
))

(defn outcome-score [line]
    (let [theirs (first line) ours (xyz-to-abc (second line))]
        (cond
            (beats? theirs ours) 0
            (= theirs ours) 3
            :else 6
        )))

(defn score [line]
    (+ (shape-score line) (outcome-score line)))

(defn split-spaces [in]
    (str/split in #" "))

(defn total-scores [rdr]
    (->> (line-seq rdr)
        (map split-spaces)
        (map score)
        (reduce +)))
    

(with-open [rdr (reader "input.txt")]
    (println (total-scores rdr))
)
