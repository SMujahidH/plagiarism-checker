"use client";

import React, { useState } from "react";
import FileUploader from "./FileUploader";
import Results from "./results";

export default function PlagiarismPage() {
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold text-center mb-6">Plagiarism Checker</h1>
      <div className="max-w-4xl mx-auto bg-white shadow-md rounded-lg p-6">
        <FileUploader setResults={setResults} setError={setError} />
        {error && <p className="text-red-500 mt-4">{error}</p>}
        {results && <Results results={results} />}
      </div>
    </div>
  );
}
