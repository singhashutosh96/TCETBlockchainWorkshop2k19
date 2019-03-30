module.exports = {
  // See <http://truffleframework.com/docs/advanced/configuration>
  // for more about customizing your Truffle configuration!
  networks: {
    development: {
      host: "172.22.6.121",
      port: 8081,
      network_id: "*" ,// Match any network id
      from: "f6e00498350aca1ccf1c62947d8b31bc432a9155",
      gas: 8000000
    }
  }
};
