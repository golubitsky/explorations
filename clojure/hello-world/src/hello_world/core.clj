(ns hello-world.core)

(require '[clojure.java.io :as io]
         '[hello-world.day-1 :refer :all])

(defn foo
  "I don't do a whole lot."
  [x]
  (str "Hello, " x))

(defn day-1 []
  (with-open [rdr (clojure.java.io/reader "/Users/mikegolubitsky/source/explorations/clojure/hello-world/resources/01_input.txt")]
    (doall (line-seq rdr))))

