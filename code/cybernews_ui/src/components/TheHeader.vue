<template>
  <header>
    <div class="header-wrapper">
      <div class="logo">CyberNews</div>
    </div>
  </header>
</template>

<script>
    export default {
      data () {
        return {

        }
      }
    }
</script>

<style scoped>
header {
  width: 100%;
  /* background-color: var(--primary-bg-color, white); */
  background-color: white;
  color: var(--primary-text-color, black);
  box-shadow: 0 8px 10px -10px lightgray;
  /*border-bottom: 2px solid rgba(191, 191, 191, 0.99);*/
  padding: 15px 0;
}

.header-wrapper {
  max-width: 1200px;
  margin: auto;
}

.logo {
  margin: 0 10px;
  font-size: 26px;
  font-weight: bold;
  text-transform: uppercase;
  justify-self: start;
  align-self: center;
}

</style>
