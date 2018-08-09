<template>
  <div class="sidebar-item">
    <input type="checkbox"
           id="editor"
           v-model="reviewedByEditor">
    <label for="editor">only reviewed: {{ reviewedByEditor }}</label>
  </div>
</template>

<script>
  import FilterStore from '../stores/FilterStore';
  import QueryStore from '../stores/QueryStore';

  export default {
    name: 'MetaList',

    data () {
      return {
        reviewedByEditor: FilterStore.data.reviewedByEditor
      }
    },

    watch: {
      reviewedByEditor(newValue) {
        FilterStore.methods.setReviewedByEditor(newValue);
        QueryStore.methods.setQuery(QueryStore.methods.getBaseQuery() + FilterStore.methods.getFilterQuery());
      }
    }
  }
</script>

<style scoped>
.sidebar-item {
  margin: 5px 10px;
  font-size: calc(16px + (24 - 16) * (100vw - 320px) / (1200 - 320));
  font-weight: 500;
  color: var(--primary-text-color, black);
}

@media screen and (min-width: 1200px) {
  .sidebar-item {
    font-size: 24px;
  }
}

.sidebar-item:hover {
  color: var(--secondary-text-color, orange);
}

.sidebar-item input[type=checkbox] {
  display: none;
}

.sidebar-item input[type=checkbox]:checked + label {
  color: var(--secondary-text-color, orange);
}
</style>
