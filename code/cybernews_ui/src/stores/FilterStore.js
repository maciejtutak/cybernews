const FilterStore = {
  data: {
    selectedTags: [],
    reviewedByEditor: false
  },

  methods: {
    getFilterQuery() {
      let filterString = '?';
      FilterStore.data.selectedTags.forEach((tag) => {
        filterString += 'tags=' + tag + '&';
      });
      if (FilterStore.data.reviewedByEditor) {
        filterString += 'user_reviewed=' + FilterStore.data.reviewedByEditor;
      }
      return filterString;
    },
    setSelectedTags(selectedTags) {
      console.log(selectedTags);
      FilterStore.data.selectedTags.splice(0, FilterStore.data.selectedTags.length, ...selectedTags);
    },
    setReviewedByEditor(reviewedByEditor) {
      FilterStore.data.reviewedByEditor = reviewedByEditor;
    }
  }
};

export default FilterStore;
