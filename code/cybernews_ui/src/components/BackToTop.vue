<template>
  <button v-on:click="backToTop"
       class="back-to-top"
       ref="backToTopBtn">
    <icon-base><icon-arrow-up></icon-arrow-up></icon-base>
  </button>
</template>

<script>
  import IconBase from '../utils/IconBase';
  import IconArrowUp from '../icons/IconArrowUp';

  export default {
    name: 'BackToTop',
    components: {
      IconBase,
      IconArrowUp
    },

    data () {
      return {
      };
    },

    created () {
      window.addEventListener('scroll', this.handleScroll);
    },

    destroyed () {
      window.removeEventListener('scroll', this.handleScroll);
    },

    methods: {
      handleScroll() {
        if (window.scrollY > 1000) {
          this.$refs.backToTopBtn.setAttribute(
            'style',
            'opacity: 0.9; transition: 0.3s'
          );
        } else {
          this.$refs.backToTopBtn.setAttribute(
            'style',
            'opacity: 0; transition: 0.3s'
          );
        }
        return window.scrollY > 1200;
      },
      backToTop() {
        const currentScroll = document.body.scrollTop || document.documentElement.scrollTop;
        if (currentScroll > 0) {
          window.requestAnimationFrame(this.backToTop);
          window.scrollTo(0, Math.floor(currentScroll - (currentScroll / 10)));
          this.$refs.backToTopBtn.setAttribute(
            'style',
            'opacity: 0; transition: 0.1s'
          );
        }
      }
    },
  }
</script>

<style scoped>
.back-to-top {
  position: fixed;
  bottom: 3vh;
  right: 5vw;
  padding: 12px 12px;
  border: 1px solid lightgray;
  border-radius: 10px;
  background-color: white;
  display: block;
  opacity: 0;
  color: gray;
  transition: 0.2s;
  cursor: pointer;
}

.back-to-top:hover {
  color: var(--primary-text-color, black);
  border-color: var(--secondary-text-color, darkorange);
  background-color: var(--secondary-text-color, darkorange);
}
</style>
