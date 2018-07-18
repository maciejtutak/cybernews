<template>
  <a :href="item.article.url">
    <div class="item-card">
      <img class="item-image" :src="item.article.image_url" />
      <div class="item-description">
        <div class="item-source">{{ item.article.source }}</div>
        <h1>{{ item.article.title }}</h1>
        <div class="item-date">{{ item.article.pub_date | moment }}</div>
        <div class="item-meta">{{ item.article.length | duration }} min read &bull; {{ item.article.author }}</div>
      </div>
    </div>
  </a>
</template>

<script>
  import moment from 'moment';

  export default {
    name: "EntryListItem",
    props: ['item'],

    methods: {
    },

    filters: {
      moment: function (date) {
        return moment(date).calendar(null, {
          sameDay: '[Today at] h:mm',
          lastDay: '[Yesterday at] h:mm',
          lastWeek: 'DD/MM/YYYY [at] h:mm',
          sameElse: 'DD/MM/YYYY [at] h:mm'
        });
      },
      duration: function (length) {
        return Math.round(length / 250);
      }
    }
  }
</script>

<style scoped>
.item-card {
  margin-bottom: 25px;
  background: white;
  box-shadow: 0 3px 5px 0 lightgray;
  border-radius: 10px;
}

.item-card:hover {
  box-shadow: 0 2px 8px 0 var(--secondary-accent-color);
  transition-duration: 0.5s;
}

.item-image {
  width: 100%;
  height: auto;
  object-fit: fill;
  border-radius: 10px 10px 0 0;
}

.item-description {
  padding: 20px 15px;
}

.item-date {
  font-size: 0.9em;
  color: var(--small-text-color, gray);
}

.item-meta {
  font-size: 0.9em;
  color: var(--small-text-color, gray);
}
</style>
