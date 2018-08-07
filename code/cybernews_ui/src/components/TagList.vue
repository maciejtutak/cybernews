<template>
  <ul>
    <li class="sidebar-item" v-for="tag in tags">{{ tag.name }}</li>
    <li class="sidebar-item"><a v-on:click="filterTag">something</a></li>
    <li class="sidebar-item"><a v-on:click="filterTag2">something2</a></li>
  </ul>
</template>

<script>
  import axios from 'axios';

  import QueryStore from '../utils/QueryStore';

  export default {
    name: 'TagList',

    data () {
      return {
        tags: [],
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

    methods: {
      filterTag() {
        console.log('something clicked');
        QueryStore.methods.setQuery('http://localhost:8000/api/entries/?limit=30');
      },
      filterTag2() {
        console.log('something2 clicked');
        QueryStore.methods.setQuery('http://localhost:8000/api/entries/?limit=10');
      }
    },

  }
</script>

<style scoped>
.sidebar-item {
  font-size: calc(16px + (24 - 16) * (100vw - 320px) / (1200 - 320));
  font-weight: 500;
  text-transform: uppercase;
  color: var(--primary-text-color, black);
}

@media screen and (min-width: 1200px) {
  .sidebar-item {
    font-size: 24px;
  }
}

.sidebar-item:hover {
  color: var(--secondary-text-color, orangered);
}
</style>
