<template>
  <div>
    <template v-for="(day, index) in splitIntoDays">
      <h1 v-if="day.length">{{ sections[index] }}</h1>
      <masonry
        v-if="day.length"
        :cols="{default: 2, 600: 1}"
        :gutter="30"
        :key="sections[index]">
          <EntryListItem
            v-if="day.length"
            v-for="item in day"
            :item="item"
            :key="item.id">
          </EntryListItem>
      </masonry>
      <div v-if="day.length > 0" class="spacer"></div>
    </template>
    <button v-on:click="loadMoreEntries"
            class="load-more-button"
            v-if="next != undefined && loadMoreVisible">Load More</button>
    <p v-if="next == undefined" class="no-more-items">There are no more items to show.</p>
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
        sections: ['Today', 'Yesterday', 'Past Stories'],
        loadMoreVisible: false
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

    created () {
      window.addEventListener('scroll', this.handleScroll);
    },

    destroyed () {
      window.removeEventListener('scroll', this.handleScroll);
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
        axios
          .get(this.next)
          .then((response) => {
            this.next = response.data.next;
            this.items.push(...response.data.results);
          })
          .catch((error) => {
            console.error(error);
          })
      },
      handleScroll () {
        if (window.scrollY > document.body.scrollHeight - 1000) {
          this.loadMoreVisible = true;
        }
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
  margin: 0 auto 50px;
  padding: 12px 24px;
  border: 1px solid lightgrey;
  display: block;
  border-radius: 10px;
  background-color: white;
  color: gray;
  font-size: 100%;
  font-family: inherit;
  font-weight: 500;
  transition: 0.2s;
  cursor: pointer;
}

.load-more-button:hover {
  color: var(--primary-text-color, black);
  border-color: var(--secondary-text-color, darkorange);
  background-color: var(--secondary-text-color, darkorange);
}

.no-more-items {
  text-align: center;
  color: var(--secondary-accent-color, gray);
  font-style: italic;
}
</style>
