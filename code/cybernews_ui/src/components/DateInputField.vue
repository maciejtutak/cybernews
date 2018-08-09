<template>
  <div
    class="date-input-form"
    @keyup.capture="updateValue">
    <input
      ref="day"
      v-model="day"
      class="date-input-field date-input-day"
      type="number"
      placeholder="dd"
      @input="updateDay"
      @blur="day = day.padStart(2, '0')">
    <span class="date-input-divider">/</span>
    <input
      ref="month"
      v-model="month"
      class="date-input-field date-input-month"
      type="number"
      placeholder="mm"
      @input="updateMonth"
      @blur="month = month.padStart(2, '0')">
    <span class="date-input-divider">/</span>
    <input
      ref="year"
      v-model="year"
      class="date-input-field date-input-year"
      type="number"
      placeholder="yyyy"
      @blur="year = year.padStart(4, '0')">
  </div>
</template>

<script>
  export default {
    name: 'DateInput',
    props: {
      value: {
        type: [Number, String],
        required: true,
      },
    },

    data () {
      return {
        day:`${this.value ? new Date(this.value).getDate() : ''}`,
        month:`${this.value ? new Date(this.value).getMonth() + 1 : ''}`,
        year:`${this.value ? new Date(this.value).getFullYear() : ''}`,
      };
    },

    watch: {
      day(newDay) {
        if (newDay > 31) this.day = 31;
      },
      month(newMonth) {
        if (newMonth > 12) this.month = 12;
      },
      year(newYear, oldYear) {
        if (newYear > 9999) this.year = oldYear;
      }
    },

    methods: {
      updateDay() {
        console.log(this.day);
        if (!this.day.length || parseInt(this.day, 10) < 4) return;
        this.$refs.month.select();
      },
      updateMonth() {
        if (!this.month.length || parseInt(this.month, 10) < 2) return;
        this.$refs.year.select();
      },
      updateValue() {
        console.log(this.year.padStart(4, '0'));
        const timestamp = Date.parse(`${this.year.padStart(4, '0')}-${this.month}-${this.day}`);
        if (Number.isNaN(timestamp)) return;
        this.$emit('input', timestamp);
        console.log(timestamp);
      },
    },
  }
</script>

<style scoped>
.date-input-form {
  display: inline-flex;
  position: relative;
  overflow: hidden;
  border: 1px solid var(--secondary-accent-color, gray);
  border-radius: 5px;

  --spacing: 8px;
}

.date-input-field {
  padding: var(--spacing) var(--spacing) / 2;
  border: none;
  text-align: center;
  -moz-appearance: textfield;
}

.date-input-field::-webkit-inner-spin-button {
  display: none;
}

.date-input-field:first-child {
  padding-left: var(--spacing);
}

.date-input-field:last-child {
  padding-right: var(--spacing);
}

.date-input-field:focus {
  outline: none;
}

.date-input-day, .date-input-month {
  width: 3em;
}

.date-input-year {
  width: 4em;
}

.date-input-divider {
  padding: var(--spacing) 0;
  pointer-events: none;
}
</style>
