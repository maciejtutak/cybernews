<template>
  <transition name="fade">
  <a :href="item.article.url">
    <div class="item-card">
      <div v-if="item.user_reviewed" class="item-reviewed">
        &#10004;
      </div>
      <img class="item-image" :src="item.article.image_url" />
      <div class="item-description">
        <div class="item-source">{{ item.article.source }}</div>
        <h2>{{ item.article.title }}</h2>
        <ul>
          <li v-for="tag in item.tags">{{ tag }}</li>
        </ul>
        <hr>
        <div class="item-date">{{ item.article.pub_date | moment }}</div>
        <div class="item-meta">{{ item.article.length | duration }} min read &bull; {{ item.article.author }}</div>
      </div>
    </div>
  </a>
  </transition>
</template>

<script>
  import moment from 'moment';

  export default {
    name: 'EntryListItem',
    props: ['item'],

    methods: {
    },

    filters: {
      moment: function (date) {
        return moment(date).calendar(null, {
          sameDay: '[Today at] HH:mm',
          lastDay: '[Yesterday at] HH:mm',
          lastWeek: 'DD/MM/YYYY [at] HH:mm',
          sameElse: 'DD/MM/YYYY [at] HH:mm'
        });
      },
      duration: function (length) {
        return Math.round(length / 200);
      }
    }
  }
</script>

<style scoped>
 .fade-enter-active, .fade-leave-active {
   -webkit-transition: opacity .5s ease-in;
   transition: opacity .5s ease-in;
 }

 .fade-leave-active {
   -webkit-transition: opacity .3s ease-out;
   transition: opacity .3s ease-out;
 }

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.item-card {
  position: relative;
  margin-bottom: 25px;
  background: white;
  box-shadow: 0 3px 5px 0 lightgray;
  border-radius: 10px;
}

.item-card:hover {
  box-shadow: 0 3px 5px 0 var(--secondary-accent-color);
  transition-duration: 0.5s;
}

.item-card ul {
  list-style-type: none;
  padding: 0;
}

.item-card li {
  display: inline-block;
  margin: 0 5px 5px 0;
  padding: 5px;
  border-radius: 5px;
  background-color: var(--primary-tag-color);
  font-size: calc(14px + (16 - 14) * (100vw - 320px) / (1200 - 320));
}

@media screen and (min-width: 1200px) {
  .item-card li {
    font-size: 16px;
  }
}

.item-reviewed {
  display: grid;
  position: absolute;
  top: 220px;
  right: 0;
  width: 32px;
  height: 24px;
  border-radius: 10px 0 0 10px;
  background-color: var(--success-color, green);
  text-align: center;
  font-size: 20px;
}

.item-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.item-description {
  padding: 20px 15px;
}

.item-description hr {
  margin-top: -5px;
  border-top: 1px solid lightgray;
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
