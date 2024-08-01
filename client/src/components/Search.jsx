/* eslint-disable react/prop-types */

const Search = ({ value, setValue, setProduct }) => {
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent form submission
    setProduct(value);
  };

  return (
    <form onSubmit={handleSubmit} className="search">
      <input
        type="text"
        placeholder="Search for item"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className="search-bar"
      />
      <button type="submit">Search</button>
    </form>
  );
};

export default Search;
