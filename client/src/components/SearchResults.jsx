/* eslint-disable react/prop-types */
import Item from "./Item";

const SearchResults = ({ title, items }) => {
  return (
    <div className="search-result">
      <h3>{title}</h3>
      <div>
        {items.length > 0 ? items.map(({ name, price }, idx) => (
          <Item key={idx} name={name} price={price} />
        )) : "No Items to show"}
      </div>
    </div>
  );
};

export default SearchResults;
