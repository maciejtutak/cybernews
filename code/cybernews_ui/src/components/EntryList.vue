<template>
  <ul class="entry-list">
    <li v-for="item in results">
      <EntryListItem v-bind:item="item"></EntryListItem>
    </li>
  </ul>
</template>

<script>
  import EntryListItem from "./EntryListItem";
  export default {
    name: "EntryList",
    components: {
      EntryListItem,
    },
    data () {
      return {
        count: "",
        next: "",
        results: []
      }
    },
    mounted() {
      this.$http.get("http://localhost:8000/api/entries/?limit=25").then(result => {
        this.count = result.body.count;
        this.next = result.body.next;
        this.results = result.body.results;
      }, error => {
        console.error(error);
      })
    },
  }
</script>

<style scoped>
  @media (min-width: 48em) {
    .entry-list {
      column-count: 2;
      column-gap: 10px;
    }
  }
</style>
