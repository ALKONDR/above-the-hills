import { observable } from 'mobx';

class PaymentStore {
  @observable shareAmount = 0;
  @observable moneyValue = 0;
}

module.exports = new PaymentStore();
