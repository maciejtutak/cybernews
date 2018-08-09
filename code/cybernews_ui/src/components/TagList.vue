<template>
  <ul class="sidebar-list">
    <li class="sidebar-item" v-for="tag in tags">
      <input type="checkbox"
             :id="tag.name"
             :value="tag.slug"
             v-model="selectedTags">
      <label :for="tag.name">{{ tag.name }}</label>
    </li>
  </ul>
</template>

<script>
  import axios from 'axios';

  import FilterStore from '../stores/FilterStore';
  import QueryStore from '../stores/QueryStore';

  export default {
    name: 'TagList',

    data () {
      return {
        tags: [],
        selectedTags: []
      }
    },

    mounted () {
      axios
        .get('http://localhost:8000/api/tags/')
        .then(response => {
          this.tags = response.data.results
        })
        .catch(error => {
          console.error(error);
        });
    },

    watch: {
      selectedTags (newTags) {
        FilterStore.methods.setSelectedTags(newTags);
        QueryStore.methods.setQuery(QueryStore.methods.getBaseQuery() + FilterStore.methods.getFilterQuery());
      }
    },

  }
</script>

<style scoped>
.sidebar-list {
  margin: 0;
}

.sidebar-item {
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

.sidebar-item label {
  cursor: pointer;
}
</style>
