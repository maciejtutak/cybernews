<template>
  <div>
    <template v-for="(day, index) in splitIntoDays">
      <h1 v-if="day.length > 0">{{ sections[index] }}</h1>
      <masonry
        :cols="{default: 2, 600: 1}"
        :gutter="30"
      >
      <EntryListItem
        v-for="item in day"
        v-bind:item="item"
        v-bind:key="item.id"
        ></EntryListItem>
      </masonry>
    </template>
  </div>
</template>

<script>
  import {axiosBase} from '../utils/axiosBase';
  import moment from 'moment';

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
        sections: ['Today', 'Yesterday', 'Past Week']
      }
    },

    mounted () {
      axiosBase
        .get('/api/entries/?limit=50')
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
      splitIntoDays: function () {
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

    methods: {
    },
  }
</script>

<style scoped>
</style>
