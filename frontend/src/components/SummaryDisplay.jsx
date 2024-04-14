import Loader from "react-js-loader";

const SummaryDisplay = ({ summary, copied, handleCopySummary, loading }) => (
  <div className="flex-1 bg-gray-200 p-8 flex items-center justify-center">
    <div className="w-full">
      {loading ? (
        <Loader
          type="box-rectangular"
          title={"Getting your summary"}
          size={100}
          color={"#111111"}
          bgColor={"#111111"}
        />
      ) : (
        <>
          <h2 className="text-3xl font-semibold text-gray-800 mb-4">Summary</h2>
          {summary ? (
            <div className="bg-white shadow-md rounded p-4 relative text-center">
              <button
                onClick={handleCopySummary}
                className="absolute top-2 right-2 bg-blue-500 text-white p-2 rounded"
                style={{ zIndex: 1 }}
              >
                {copied ? "Copied" : "Copy"}
              </button>
              <pre className="whitespace-pre-wrap text-left mt-10">
                {summary}
              </pre>
            </div>
          ) : (
            <p className="text-gray-600">Upload a file to see the summary</p>
          )}
        </>
      )}
    </div>
  </div>
);

export default SummaryDisplay;
