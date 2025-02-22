import { useState, useEffect } from "react";
import { motion } from "framer-motion";

export default function BubbleSort() {
  const [array, setArray] = useState([]);
  const [sorting, setSorting] = useState(false);
  const [comparison, setComparison] = useState([]);

  useEffect(() => {
    generateArray();
  }, []);

  const generateArray = () => {
    const newArr = Array.from(
      { length: 10 },
      () => Math.floor(Math.random() * 100) + 10
    );
    setArray(newArr);
    setComparison([]);
  };

  const bubbleSort = async () => {
    setSorting(true);
    let arr = [...array];
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        setComparison([j, j + 1]);

        await new Promise((resolve) => setTimeout(resolve, 150));
        if (arr[j] > arr[j + 1]) {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
          setArray([...arr]);
          await new Promise((resolve) => setTimeout(resolve, 300));
        }
      }
    }
    setComparison([]);
    setSorting(false);
  };

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="font-bold text-blue-500 text-2xl mb-5">Bubble Sort</h1>
      <div className="flex space-x-2 mb-8">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded disabled:opacity-50 cursor-pointer"
          onClick={generateArray}
          disabled={sorting}
        >
          Generate New Array
        </button>
        <button
          className="bg-green-500 text-white px-4 py-2 rounded disabled:opacity-50 cursor-pointer"
          onClick={bubbleSort}
          disabled={sorting}
        >
          Start Sorting
        </button>
      </div>

      <div className="flex space-x-1 h-48 items-end">
        {array.map((value, index) => (
          <motion.div
            key={index}
            className={`w-8 rounded ${
              comparison.includes(index) ? "bg-red-500" : "bg-blue-400"
            }`}
            initial={{ height: value * 2 }}
            animate={{ height: value * 2 }}
            transition={{ type: "spring", stiffness: 300, damping: 20 }}
          >
            <p className="text-xs text-center text-white">{value}</p>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
