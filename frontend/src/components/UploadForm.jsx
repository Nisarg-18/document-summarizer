import ErrorMessage from "./ErrorMessage";

const UploadForm = ({
  handleFileChange,
  handleWordLengthChange,
  handleUpload,
  file,
  wordLength,
  loading,
  error,
}) => (
  <div className="flex-1 bg-gray-100 p-8 flex items-center justify-center">
    <div className="max-w-md w-full">
      <h2 className="text-3xl font-semibold text-gray-800 mb-4">
        Upload a File (PDF only)
      </h2>
      <input
        type="file"
        onChange={handleFileChange}
        className="py-2 px-4 border border-gray-400 rounded w-full mb-4"
      />
      <label
        htmlFor="wordLength"
        className="block text-gray-700 text-sm font-bold mb-2"
      >
        Maximum Word Length of Summary (Minimum 100 is required):
      </label>
      <input
        type="number"
        id="wordLength"
        name="wordLength"
        value={wordLength}
        onChange={handleWordLengthChange}
        className="py-2 px-4 border border-gray-400 rounded w-full mb-4"
      />
      <button
        onClick={handleUpload}
        disabled={!file || loading}
        className={`bg-blue-500 text-white py-2 px-4 rounded w-full ${
          loading ? "opacity-50 cursor-not-allowed" : ""
        }`}
      >
        {loading ? "Uploading..." : "Upload File"}
      </button>
      {error && <ErrorMessage error={error} />}
    </div>
  </div>
);

export default UploadForm;
