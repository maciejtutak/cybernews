<template>
  <div class="sidebar-date">
    <div>
    <datepicker
      name="from"
      v-model="dateFrom.date"
      :disabledDates="dateFrom.disabledDates"
      format="dd/MM/yyyy"
      placeholder="select date"
      :monday-first="true"
      wrapper-class="datepicker"
      input-class="datepicker-input"
      calendar-class="datepicker-calendar"></datepicker>
    </div>
    :
    <!--&#8212;-->
    <div>
      <datepicker
        name="to"
        v-model="dateTo.date"
        :disabledDates="dateTo.disabledDates"
        format="dd/MM/yyyy"
        placeholder="select date"
        :monday-first="true"
        wrapper-class="datepicker"
        input-class="datepicker-input"
        calendar-class="datepicker-calendar"></datepicker>
    </div>
  </div>
</template>

<script>
  import Datepicker from 'vuejs-datepicker';

  import FilterStore from '../stores/FilterStore';
  import QueryStore from '../stores/QueryStore';

    export default {
      name: 'DateInput',
      components: {
        Datepicker
      },

      data () {
        return {
          dateFrom: {
            date: FilterStore.data.dateFrom,
            disabledDates: {
              to: new Date(2013, 0, 1),
              from: new Date()
            }
          },
          dateTo: {
            date: FilterStore.data.dateTo,
            disabledDates: {
              to: new Date(2013, 0, 1)
            }
          }
        };
      },

      watch: {
        dateFrom: {
          handler: function (newDate) {
            this.dateTo.disabledDates.to = newDate.date;
            FilterStore.methods.setDateFrom(newDate.date);
            QueryStore.methods.setQuery(QueryStore.methods.getBaseQuery() + FilterStore.methods.getFilterQuery());
          },
          deep: true,
        },
        dateTo: {
          handler: function (newDate) {
            this.dateFrom.disabledDates.from = newDate.date;
            FilterStore.methods.setDateTo(newDate.date);
            QueryStore.methods.setQuery(QueryStore.methods.getBaseQuery() + FilterStore.methods.getFilterQuery());
          },
          deep: true,
        }
      },
    }
</script>

<style scoped>
.sidebar-date {
  margin: 5px 10px;
}

.sidebar-date div {
  margin: 2px 0 0 0;
  display: inline-block;
}
</style>

<style>
.datepicker {
  margin: 0;
}

.datepicker-input {
  margin: 0;
  padding: 4px;
  width: 100px;
  border: 1px solid var(--primary-accent-color, lightgray);
  border-radius: 5px;
  color: var(--secondary-accent-color, gray);
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16px;
  text-align: center;
}

.datepicker-input:focus {
  box-shadow: 0 0 3px 0 var(--secondary-text-color, darkorange);
}

.datepicker-calendar {
  border: 1px solid var(--primary-accent-color);
  border-radius: 5px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.datepicker-calendar .next {
  border-top-right-radius: 5px;
}

.datepicker-calendar .prev {
  border-top-left-radius: 5px;
}

.datepicker-calendar .cell:not(.blank):not(.disabled).day:hover {
  border-radius: 5px;
  border-color: var(--secondary-text-color, darkorange);
}

.datepicker-calendar .cell.selected {
  border-radius: 5px;
  background-color: var(--secondary-text-color, darkorange);
}

.datepicker-calendar .cell.selected:hover {
  border-radius: 5px;
  background-color: var(--secondary-text-color, darkorange);
}
</style>
