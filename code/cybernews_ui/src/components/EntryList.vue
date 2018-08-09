<template>
  <div>
    <template v-for="(day, index) in splitIntoDays">
      <h1 v-if="day.length > 0">{{ sections[index] }}</h1>
      <masonry
        :cols="{default: 2, 600: 1}"
        :gutter="30">
          <EntryListItem
            v-for="item in day"
            v-bind:item="item"
            v-bind:key="item.id">
          </EntryListItem>
      </masonry>
      <div v-if="day.length > 0" class="spacer"></div>
    </template>
    <button v-on:click="loadMoreEntries" class="load-more-button">Load More</button>
  </div>
</template>

<script>
  import axios from 'axios';
  import moment from 'moment';

  import QueryStore from '../stores/QueryStore';
  import EntryListItem from './EntryListItem';

  export default {
    name: 'EntryList',
    components: {
      EntryListItem,
    },
    data () {
      return {
        count: '',
        next: '',
        items: [],
        QueryStore: QueryStore.data,
        sections: ['Today', 'Yesterday', 'Past Stories']
      }
    },

    watch: {
      QueryStore: {
        handler: function(newQuery, oldQuery) {
        axios
          .get(newQuery.query)
          .then((response) => {
            this.count = response.data.count;
            this.next = response.data.next;
            this.items = response.data.results;
          })
          .catch((error) => {
            console.error(error);
          })
        },
        deep: true,
      },
    },

    mounted () {
      axios
        .get(QueryStore.methods.getBaseQuery())
        .then((response) => {
          this.count = response.data.count;
          this.next = response.data.next;
          this.items = response.data.results;
          })
        .catch((error) => {
          console.error(error);
        });
    },

    methods: {
      loadMoreEntries () {
        console.log(this.next);
        axios
          .get(this.next)
          .then((response) => {
            this.next = response.data.next;
            this.items.push(...response.data.results);
          })
          .catch((error) => {
            console.error(error);
          })
      }
    },

    computed: {
      splitIntoDays () {
        let today = [];
        let yesterday = [];
        let past = [];
        this.items.forEach((item) => {
          if (moment(item.article.pub_date).date() === moment().date()) {
            today.push(item);
          } else if (moment(item.article.pub_date).date() === moment().subtract(1, 'days').date()) {
            yesterday.push(item);
          } else {
            past.push(item);
          }
        });
        return [today, yesterday, past];
      }
    },
  }
</script>

<style scoped>
h1 {
  margin: 20px 0 20px 0;
  width: 100%;
}

.spacer {
  padding-bottom: 40px;
}

.load-more-button {
  margin: 0 auto 10px;
  padding: 10px 30px;
  border: 0;
  display: block;
  border-radius: 5px;
  background-color: lightgray;
  font-size: 100%;
  font-family: inherit;
  font-weight: 500;
  transition: 0.2s;
  cursor: pointer;
}

.load-more-button:hover {
  background-color: var(--secondary-text-color, orange);
}
</style>
