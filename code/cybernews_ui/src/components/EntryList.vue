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
    </template>
  </div>
</template>

<script>
  import axios from 'axios';
  import moment from 'moment';

  import QueryStore from '../utils/QueryStore';
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
        sections: ['Today', 'Yesterday', 'Past Week']
      }
    },

    watch: {
      QueryStore: {
        handler: function(newQuery, oldQuery) {
        console.log('query watch triggered');
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
      items: function(newItems, oldItems) {
        console.log('items watch triggered');
        console.log(newItems);
      }
    },

    mounted () {
      axios
        .get(this.QueryStore.query)
        .then((response) => {
            this.count = response.data.count;
            this.next = response.data.next;
            this.items = response.data.results;
          })
        .catch((error) => {
            console.error(error);
          });
    },

    computed: {
      splitIntoDays () {
        let today = [];
        let yesterday = [];
        let pastWeek = [];
        this.items.forEach((item) => {
          if (moment(item.article.pub_date).date() === moment().date()) {
            today.push(item);
          } else if (moment(item.article.pub_date).date() === moment().subtract(1, 'days').date()) {
            yesterday.push(item);
          } else {
            pastWeek.push(item);
          }
        });
        return [today, yesterday, pastWeek];
      }
    },
  }
</script>

<style scoped>
h1 {
  margin: 40px 0 20px 0;
  width: 100%;
}
</style>
