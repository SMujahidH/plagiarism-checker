import React, { useState } from "react";
import axios from "axios";

export default function FileUploader({ setResults, setError }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError(null); // Clear previous errors
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file.");
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/plagiarism/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setResults(response.data);
    } catch (err) {
      setError("Failed to check plagiarism. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="text-center">
      <input
        type="file"
        accept=".txt,.pdf,.docx"
        onChange={handleFileChange}
        className="block w-full mb-4"
      />
      <button
        type="submit"
        className={`w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 ${
          loading ? "opacity-50 cursor-not-allowed" : ""
        }`}
        disabled={loading}
      >
        {loading ? "Checking..." : "Upload and Check"}
      </button>
    </form>
  );
}
