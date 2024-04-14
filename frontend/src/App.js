import Home from "./components/Home";
import Navbar from "./components/NavBar";

function App() {
  return (
    <>
      <div className="flex flex-col h-screen">
        <Navbar></Navbar>
        <Home></Home>
      </div>
    </>
  );
}

export default App;
