(ns hello-world.core-test
  (:require [clojure.test :refer :all]
            [hello-world.core :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    (is (= 1 1))))

(deftest something
  (is (= "Hello, Mike" (foo "Mike"))))

;; (deftest day-1-test
;;   (is (= 200 (day-1))))