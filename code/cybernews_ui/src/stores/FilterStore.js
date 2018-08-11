import moment from 'moment';

const FilterStore = {
  data: {
    selectedTags: [],
    reviewedByEditor: false,
    dateFrom: undefined,
    dateTo: undefined
  },

  methods: {
    getFilterQuery() {
      let filterString = '?';
      FilterStore.data.selectedTags.forEach((tag) => {
        filterString += 'tags=' + tag + '&';
      });
      if (FilterStore.data.reviewedByEditor) {
        filterString += 'user_reviewed=' + FilterStore.data.reviewedByEditor + '&';
      }
      if (FilterStore.data.dateFrom) {
        filterString += 'date_range_0=' + moment(FilterStore.data.dateFrom).format('YYYY-MM-DD') + '&';
      }
      if (FilterStore.data.dateTo) {
        filterString += 'date_range_1=' + moment(FilterStore.data.dateTo).format('YYYY-MM-DD') + '&';
      }
      console.log(filterString);
      return filterString;
    },
    setSelectedTags(selectedTags) {
      console.log(selectedTags);
      FilterStore.data.selectedTags.splice(0, FilterStore.data.selectedTags.length, ...selectedTags);
    },
    setReviewedByEditor(reviewedByEditor) {
      FilterStore.data.reviewedByEditor = reviewedByEditor;
    },
    setDateFrom(dateFrom) {
      FilterStore.data.dateFrom = dateFrom;
    },
    setDateTo(dateTo) {
      FilterStore.data.dateTo = dateTo;
    }
  }
};

export default FilterStore;
