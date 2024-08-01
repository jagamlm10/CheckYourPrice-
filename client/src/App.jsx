import { useEffect, useState } from "react";
import "./App.css";
import Search from "./components/Search";
import SearchResults from "./components/SearchResults";
import axios from "axios";

function App() {
  const [value, setValue] = useState("");
  const [product, setProduct] = useState("");
  const [amsearch, setAmsearch] = useState([]);
  const [flipsearch, setFlipsearch] = useState([]);
  // const [snapsearch, setSnapsearch] = useState([]);

  const fetchAmazon = async () => {
    try {
      const response = await axios.post("http://localhost:5000/amazon", {
        data: product,
      });
      console.log(response);
      const data = response.data.message.items; // Updated to access the correct data
      setAmsearch(data);
    } catch (error) {
      console.error("Error fetching Amazon data", error);
    }
  };

  const fetchFlipkart = async () => {
    try {
      const response = await axios.post("http://localhost:5000/flipkart", {
        data: product,
      });
      console.log(response);
      const data = response.data.message.items; // Updated to access the correct data
      setFlipsearch(data);
    } catch (error) {
      console.error("Error fetching Flipkart data", error);
    }
  };

  // const fetchSnapdeal = async () => {
  //   const response1 = await axios.post("http://localhost:5000/snapdeal", {
  //     data: product,
  //   });
  //   const data = response1["message"];
  //   setSnapsearch(data);
  // };

  useEffect(() => {
    if (!product) return;
    fetchAmazon();
    fetchFlipkart();
    // fetchSnapdeal();
  }, [product]);

  return (
    <>
      <Search value={value} setValue={setValue} setProduct={setProduct} />
      <div className="results">
        <SearchResults title={"Amazon"} items={amsearch} />
        <SearchResults title={"Flipkart"} items={flipsearch} className = "flipkart"/>
        {/* <SearchResults title={"Snapdeal"} items={snapsearch}/> */}
      </div>
    </>
  );
}

export default App;
