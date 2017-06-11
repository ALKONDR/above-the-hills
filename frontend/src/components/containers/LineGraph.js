import React from 'react';
import PropTypes from 'prop-types';
import { Line } from 'react-chartjs-2';

class LineGraph extends React.PureComponent {
  render() {
    const data = {
      labels: [1, 2, 3, 4, 5, 6, 7], // this.props.x
      datasets: [{
        label: 'MemeGraph',
        fill: true,
        lineTension: 0.1,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBorderColor: 'rgba(75,192,192,1)',
        pointBackgroundColor: '#fff',
        pointBorderWidth: 1,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: 'rgba(75,192,192,1)',
        pointHoverBorderColor: 'rgba(220,220,220,1)',
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [65, 59, 80, 81, 56, 55, 40], // this.props.y
      }],
    };

    return (
      <div className="linegraph">
        <Line data={data} />
      </div>
    );
  }
}

LineGraph.propTypes = {
  x: PropTypes.arrayOf(PropTypes.number.isRequired).isRequired,
  y: PropTypes.arrayOf(PropTypes.number.isRequired).isRequired,
};

module.exports = LineGraph;
