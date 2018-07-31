<template>
  <div id="app">
    <TheHeader class="grid-header"></TheHeader>
    <div class="grid">
      <h2 class="grid-trending">TRENDING TOPICS: TRUMP | APPLE | FACEBOOK</h2>
      <ul class="grid-sidebar">
      </ul>
      <EntryList class="grid-list"></EntryList>
    </div>
  </div>
</template>

<script>
  import TheHeader from './components/TheHeader.vue';
  import EntryList from './components/EntryList.vue';
  import TagList from './components/TagList.vue';

  export default {
    components: {
      TheHeader,
      EntryList,
      TagList,
    }
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
  font-size: 24px;
  font-weight: 500;
}

h2 {
  font-size: 18px;
  font-weight: 600;
}

h3 {
  font-size: 16px;
}

p {
  font-size: 14px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}


.grid {
  display: grid;
  grid-template-areas:
    "head"
    "trending"
    "aside"
    "main";
  grid-template-columns: auto;
  grid-template-rows: auto;
  max-width: 1200px;
  margin: auto;
}

@media (min-width: 48em) {
  .grid {
    display: grid;
    grid-template-areas:
      "head head"
      "trending trending"
      "aside main";
    grid-template-columns: 1fr 3fr;
    grid-template-rows: auto;
    justify-items: center;
    padding: 0 20px;
    max-width: 1200px;
    margin: auto;
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
}

.sidebar-item {
  font-size: 20px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  color: var(--primary-text-color, black);
}

.sidebar-item:hover {
  color: var(--secondary-text-color);
}


.grid-list {
  grid-area: main;
  padding: 10px;
}

</style>
