import React from 'react';
import PropTypes from 'prop-types';
import Category from './Category';

class Categories extends React.PureComponent {
  render() {
    return (
      <div className="categoriesContainer">
        {this.props.previews.map(element => <Category key={element.category} {...element} />)}
      </div>
    );
  }
}

Categories.propTypes = {
  previews: PropTypes.arrayOf({
    category: PropTypes.string.isRequired,
    value: PropTypes.number.isRequired,
    difference: PropTypes.number.isRequired,
  }).isRequired,
};

module.exports = Categories;
