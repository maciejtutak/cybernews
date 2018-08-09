const QueryStore = {
  data: {
    baseQuery: 'http://localhost:8000/api/entries/',
    query: ''
  },

  methods: {
    getBaseQuery() {
      return QueryStore.data.baseQuery;
    },
    setQuery(query) {
      console.log('setQuery triggered');
      QueryStore.data.query = query;
    }
  }
};

export default QueryStore;
