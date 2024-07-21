import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount; // Use the setter for validation
    this.currency = currency; // Use the setter for validation
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a class of Currency');
    }
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      throw new Error('Amount must be a number');
    }
    this._amount = amount;
  }

  displayFullPrice() {
    const code = this.currency._code;
    const name = this.currency._name;
    return `${this.amount} ${name} (${code})`;
  }

  static convertPrice(amount = 0, conversionRate = 0) {
    if (typeof amount !== 'number') {
      throw new TypeError('amount must be a number');
    }

    if (typeof conversionRate !== 'number') {
      throw new TypeError('conversionRate must be a number');
    }

    return (amount * conversionRate);
  }
}
