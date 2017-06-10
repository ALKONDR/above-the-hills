import React from 'react';
import Categories from '../presentations/Categories';

class CategoriesContainer extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      previews: [],
    };
  }

  componentWillMount() {
    this.setState({
      previews: [
        {
          category: 'vzhuh',
          value: 100.52,
          difference: 10.34,
        },
        {
          category: 'potracheno',
          value: 45.23,
          difference: -4.12,
        },
        {
          category: 'agutin',
          value: 76.24,
          difference: -34.03,
        },
      ],
    });
  }

  render() {
    return <Categories previews={this.state.previews} />;
  }
}

module.exports = CategoriesContainer;
