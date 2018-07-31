<template>
  <masonry
    :cols="{default: 2, 600: 1}"
    :gutter="30"
  >
    <EntryListItem
      v-for="item in items"
      v-bind:item="item"
      v-bind:key="item.id"
    ></EntryListItem>
  </masonry>
</template>

<script>
  import axios from "axios";
  import moment from "moment";

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
        items: []
      }
    },

    created () {
      axios
        .get('http://localhost:8000/api/entries/?limit=50')
        .then((response) => {
            this.count = response.data.count;
            this.next = response.data.next;
            this.items = response.data.results;
          })
        .catch((error) => {
            console.error(error);
          })

    },

    computed: {
      splitIntoDays: function () {
        // return this.splitIntoDays(this.items);
      }
    },

    methods: {
      splitIntoDays: function (results) {
        //   let today = Date.now();
        console.log('splitIntoDays', results, new Date().getDate());
          results.forEach((result) => {
           console.log(new Date(result.article.pub_date).getDate() > (new Date().getDate() - 1));
          });
          // let today = results.filter(result => new Date(result.article.pub_date).getDay());
          // console.log(today);
        return results;
      },
    }
  }
</script>

<style scoped>
  @media (min-width: 48em) {
    .entry-list {
    }
  }
</style>
