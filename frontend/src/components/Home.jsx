import React, { useState } from "react";
import axios from "axios";
import SummaryDisplay from "./SummaryDisplay";
import UploadForm from "./UploadForm";

const Home = () => {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);
  const [error, setError] = useState(null);
  const [wordLength, setWordLength] = useState(500); // Default word length

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleWordLengthChange = (e) => {
    const value = parseInt(e.target.value, 10);
    setWordLength(value);
  };

  const handleUpload = async () => {
    setLoading(true);
    setError(null);

    if (!wordLength || wordLength < 100) {
      setError("Word length must be at least 100.");
      setLoading(false);
      return;
    }

    try {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("max_length", wordLength);

      const response = await axios.post(
        "http://localhost:8080/upload-document",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log(response.data);
      setSummary(response.data.summary);
      setError(null);
    } catch (error) {
      console.log(error.response.data);
      console.error("Error uploading file:", error);
      setError(error.response.data.error || "An error occurred");
      setSummary(null);
    }
    setLoading(false);
  };

  const handleCopySummary = () => {
    navigator.clipboard.writeText(summary);
    setCopied(true);
    setTimeout(() => {
      setCopied(false);
    }, 2000); // Reset "Copied" status after 2 seconds
  };

  return (
    <div className="flex flex-col lg:flex-row h-screen">
      <UploadForm
        handleFileChange={handleFileChange}
        handleWordLengthChange={handleWordLengthChange}
        handleUpload={handleUpload}
        file={file}
        wordLength={wordLength}
        loading={loading}
        error={error}
      />
      <SummaryDisplay
        summary={summary}
        copied={copied}
        handleCopySummary={handleCopySummary}
        loading={loading}
      />
    </div>
  );
};

export default Home;
