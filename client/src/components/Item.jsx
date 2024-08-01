/* eslint-disable react/prop-types */

const Item = ({name,price}) => {
  return (
    <div className="product">
        <h5>{name}</h5>
        <p>{price}</p>
    </div>
  )
}

export default Item