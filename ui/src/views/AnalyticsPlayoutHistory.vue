<template>
  <div class="about">
    <h2>{{ $t('Playout History') }}</h2>
    <vc-date-picker mode="dateTime" v-model="range" is-range>
      <template v-slot="{ inputValue, inputEvents }">
        <input :value="inputValue.start" v-on="inputEvents.start" class="border px-2 py-1 w-32 rounded focus:outline-none focus:border-indigo-300"/>
        <input :value="inputValue.end" v-on="inputEvents.end" class="border px-2 py-1 w-32 rounded focus:outline-none focus:border-indigo-300"/>
      </template>
    </vc-date-picker>


    <v-data-table :items="items" :headers="headers"/>

  </div>
</template>

<script>
import PlayoutHistoryService from '../services/PlayoutHistoryService';

export default {
  name: 'AnalyticsPlayoutHistory',

  components: {
  },

  data: () => ({
    range: {
      start: new Date(),
      end: new Date(),
    },
    headers: [
      {
        text: "Start Time",
        value: "starts",
      },
      {
        text: "End Time",
        value: "ends"
      },
      {
        text: "Title",
        value: "file.track_title",
      },
      {
        text: "Creator",
        value: "file.artist_name",
      },
      {
        text: "Show",
        value: "metadata.showname",
      },
      {
        text: "Show Creator",
        value: "metadata.artist_name"
      },
    ],
    items: [],
    err: null,
  }),

  methods: {
    fetch() {
      PlayoutHistoryService.getAll()
        .then(response => {
          this.items = response.data;
        })
        .catch(e => {
          this.items = []
          this.err = e
        })
    },
    refreshList() {
      this.fetch()
    },
  },
  mounted() {
    this.fetch();
  }
};
</script>
