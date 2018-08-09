<template>
  <div id="app">
    <TheHeader class="grid-header"></TheHeader>
    <div class="grid">
      <!--<h2 class="grid-trending">TRENDING TOPICS: TRUMP | APPLE | FACEBOOK</h2>-->
      <div class="grid-sidebar">
        <h2>Topic</h2>
        <TagList></TagList>
        <h2>Date</h2>
        <DateInput></DateInput>
        <h2>Meta</h2>
        <MetaList></MetaList>
      </div>
      <EntryList class="grid-list"></EntryList>
    </div>
  </div>
</template>

<script>
  import TheHeader from './components/TheHeader.vue';
  import EntryList from './components/EntryList.vue';
  import TagList from './components/TagList.vue';
  import DateInput from './components/DateInput.vue';
  import MetaList from './components/MetaList.vue';

  export default {
    components: {
      TheHeader,
      EntryList,
      TagList,
      MetaList,
      DateInput
    },
  }
</script>


<style>
/* variables */
:root {
  --primary-text-color: #242124;
  --secondary-text-color: orange;
  --small-text-color: #655d5f;
  --primary-bg-color: #fafafa;
  --primary-accent-color: lightgray;
  --secondary-accent-color: gray;
  --primary-tag-color: lightgray;
  --success-color: #1ecd62;

  --gutter: 20px;
}

#app {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  margin: 0 auto;
  padding: 0;
  color: var(--primary-text-color, black);
}

a {
  text-decoration: none;
  color: var(--primary-text-color, black);
}

/* fonts */
h1 {
  font-size: calc(22px + (32 - 22) * (100vw - 320px) / (1200 - 320));
  font-weight: 500;
}

h2 {
  font-size: calc(18px + (22 - 18) * (100vw - 320px) / (1200 - 320));
  font-weight: 500;
}

p {
  font-size: calc(12px + (14 - 12) * (100vw - 320px) / (1200 - 320));
}

@media screen and (min-width: 1200px) {
  h1 {
    font-size: 32px;
  }

  h2 {
    font-size: 24px;
  }

  p {
    font-size: 14px;
  }
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: block;
  margin: 5px 10px;
}

@media screen and (max-width: 48em) {
  li {
    display: inline-block;
  }
}


/* main grid layout */
.grid {
  display: grid;
  grid-template-areas:
    "head"
    "trending"
    "aside"
    "main";
  grid-template-columns: auto;
  grid-template-rows: auto;
  min-width: 320px;
  margin: auto;
}

@media screen and (min-width: 48em) {
  .grid {
    display: grid;
    grid-template-areas:
      "head head"
      "trending trending"
      "aside main";
    grid-template-columns: 3fr 7fr;
    grid-template-rows: auto;
    justify-items: center;
    padding: 0 20px;
    max-width: 1200px;
  }
}

.grid-header {
  grid-area: head;
  padding: 0 20px;
  /*position: fixed;*/
}

.grid-trending {
  grid-area: trending;
  justify-self: center;
  align-self: center;
  width: 100%;
  height: auto;
  padding: 10px 20px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  background: ghostwhite;
  color: var(--primary-text-color, black);
}

.grid-sidebar {
  grid-area: aside;
  width: 100%;
  height: auto;
  padding: 10px;
  justify-content: space-between;
}

.grid-sidebar h2 {
  margin: 20px 0 0 0;
}

.grid-list {
  grid-area: main;
  padding: 10px;
}

</style>
