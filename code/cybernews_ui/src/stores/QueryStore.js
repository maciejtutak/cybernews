const QueryStore = {
  data: {
    query: 'http://localhost:8000/api/entries/'
  },

  methods: {
    getQuery() {
      return QueryStore.data.query;
    },
    setQuery(query) {
      console.log('setQuery triggered');
      QueryStore.data.query = query;
    }
  }
};

export default QueryStore;
