/* eslint-disable class-methods-use-this */
import React from 'react';
import { observer } from 'mobx-react';
import Button from '../presentations/Button';
import PaymentStore from '../stores/PaymentStore';

@observer
class SharesController extends React.PureComponent {
  constructor(props) {
    super(props);

    PaymentStore.shareAmount = 0;
    PaymentStore.moneyValue = 0;

    this.incrementShareValue = this.incrementShareValue.bind(this);
    this.decrementShareValue = this.decrementShareValue.bind(this);
    this.sellShares = this.sellShares.bind(this);
    this.buyShares = this.buyShares.bind(this);
    this.inputOnChange = this.inputOnChange.bind(this);
  }

  incrementShareValue(e) {
    e.preventDefault();
    PaymentStore.shareAmount += 1;
  }

  decrementShareValue(e) {
    e.preventDefault();
    PaymentStore.shareAmount -= 1;
  }

  sellShares(e) {
    e.preventDefault();
  }

  buyShares(e) {
    e.preventDefault();
  }

  inputOnChange(e) {
    console.log(e.target.value);
    PaymentStore.shareAmount = parseFloat(e.target.value);
  }

  render() {
    return (
      <div className="paymentsContainer">
        <Button cssClass={'changeShareValue'} listener={this.incrementShareValue}>
          +
        </Button>
        <input
          type="text"
          className="valueInput"
          onChange={this.inputOnChange}
          value={PaymentStore.shareAmount}
        />
        <Button cssClass={'changeShareValue'} listener={this.decrementShareValue}>
          -
        </Button>
        <Button cssClass={'shareAction'} listener={this.buyShares}>
          Купить
        </Button>
        <Button cssClass={'shareAction'} listener={this.sellShares}>
          Продать
        </Button>
      </div>
    );
  }
}

module.exports = SharesController;
