(defn closest-odd [n]
  (-> n
      inc
      (/ 2)
      int
      (* 2)
      dec)
  )

(defn pos-for-n [n]
  (let [inner-ring-n (closest-odd (int (Math/sqrt (dec n))))
        max-dim (inc (Math/floor (/ inner-ring-n 2)))
        num-on-ring (dec (- n (* inner-ring-n inner-ring-n)))
        side-len (inc inner-ring-n)
        outer-ring-n (inc side-len)
        side-num (int (Math/floor (/ num-on-ring side-len)))
        side-dist (mod num-on-ring side-len)
        
        start-k (/ (dec inner-ring-n) 2)
        start-k-1 (inc start-k)
        
        side-start
        (case side-num
              0 [start-k start-k-1]
              1 [(- start-k-1) start-k]
              2 [(- start-k) (- start-k-1)]
              3 [start-k-1 (- start-k)]
              )
        side-inc
        (case side-num
              0 [-1 0]
              1 [0 -1]
              2 [1 0]
              3 [0 1])
        ]
      [(+
         (first side-start)
         (* side-dist (first side-inc)))
       (+
         (last side-start)
         (* side-dist (last side-inc)))
       ]))

(defn neighbors-sum [pos grid]
  (let [[x y] pos]
       (reduce
         (fn [sum x2]
           (+ sum
             (reduce
               #(+ %1 (get grid [(+ x x2) (+ y %2)] 0))
               0
               (range -1 2))
               ))
         0
         (range -1 2))
       )
  )
     
(defn val-for-n [grid n]

  (let [pos (pos-for-n n)]
       ;(println pos)
       (println (neighbors-sum pos grid))
       (assoc grid pos (neighbors-sum pos grid))
  )
  )

(count (reduce val-for-n {[0 0] 1} (range 2 100)))


