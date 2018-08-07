const QueryStore = {
  data: {
    query: 'http://localhost:8000/api/entries/?limit=50'
  },
  methods: {
    setQuery(query) {
      console.log('setQuery triggered');
      QueryStore.data.query = query;
    }
  }
};

export default QueryStore;
