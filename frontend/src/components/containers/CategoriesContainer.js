/* eslint-disable */
import React from 'react';
import PropTypes from 'prop-types';
import Categories from '../presentations/Categories';
import api from '../utils/api';

class CategoriesContainer extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      previews: [],
    };

    this.setState = this.setState.bind(this);
  }

  componentWillMount() {
    api.getCategories().then((response) => {
      if (response.status >= 200 && response.status < 300) {
        this.setState({
          previews: response.data.map((element) => {
            return {
              category: element.name,
              value: element.price,
              difference: 10,
            }
          }),
        });
      }
    });
  }

  render() {
    console.log(this.props.location.search);
    return <Categories previews={this.state.previews} />;
  }
}

module.exports = CategoriesContainer;
