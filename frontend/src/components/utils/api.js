import axios from 'axios';

axios.defaults.baseURL = 'http://membrain.ru:8080/api';

module.exports = {
  get id() {
    return window.localStorage.getItem("id");
  },

  get code() {
    return window.localStorage.getItem("code");
  },

  login(code) {
    return axios.get(`/login/?code=${code}`);
  },

  setUser(id, code) {
    window.localStorage.setItem("id", id);
    window.localStorage.setItem("code", code);
  },

  getCategories() {
    return axios.get('/categories');
  },

  getCategory(category) {
    return axios.get(`/categories/${category}`);
  },

  getUser(id) {
     return axios.get(`/users/${id}`);
  },

  buyShares(deal) {
    return axios.post(`/users/${this.id}/buy`, deal);
  },

  sellShares(deal) {
    return axios.post(`/users/${this.id}/sell`, deal);
  }
}
