(defn rep-sum [s]
  (->>
    (map vector
         s
         (concat (drop 1 s) (take 1 s)))
    (filter #(= (first %) (second %)))
    (map #(read-string (.toString (first %))))
    (reduce +)))

(defn rep-sum-2 [s]
  (->>
    (map vector
         s
         (concat (drop (/ (count s) 2) s) (take (/ (count s) 2) s)))
    (filter #(= (first %) (second %)))
    (map #(read-string (.toString (first %))))
    (reduce +)))

(rep-sum "1122")
(rep-sum "1111")
(rep-sum "1234")

"==="

(rep-sum-2 "1212")
(rep-sum-2 "1221")
(rep-sum-2 "123425")
(rep-sum-2 "123123")
(rep-sum-2 "12131415")
