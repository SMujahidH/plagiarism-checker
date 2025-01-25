import React from "react";

export default function Results({ results }) {
  return (
    <div className="mt-6">
      <h2 className="text-xl font-bold mb-4">Results</h2>
      <p className="text-lg mb-4">
        Total Plagiarism: <span className="text-red-500">{results.overall_score}</span>
      </p>
      <div className="space-y-4">
        {results.detailed_results.map((result, index) => (
          <div
            key={index}
            className={`p-4 rounded-lg ${
              parseFloat(result.max_similarity) > 30 ? "bg-red-100" : "bg-green-100"
            }`}
          >
            <h3 className="font-semibold">Paragraph {result.paragraph_index}</h3>
            <p className="text-sm text-gray-700">{result.paragraph}</p>
            <p className="text-sm font-semibold mt-2">
              Max Similarity: <span>{result.max_similarity}</span>
            </p>
            <ul className="mt-2 space-y-1">
              {result.matches.map((match, matchIndex) => (
                <li key={matchIndex} className="text-sm">
                  <a
                    href={match.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-500 hover:underline"
                  >
                    {match.title}
                  </a>{" "}
                  ({match.similarity})
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
