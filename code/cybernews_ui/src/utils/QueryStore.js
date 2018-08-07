const QueryStore = {
  data: {
    query: 'http://localhost:8000/api/entries/'
  },
  methods: {
    setQuery(query) {
      console.log('setQuery triggered');
      QueryStore.data.query = query;
    }
  }
};

export default QueryStore;
