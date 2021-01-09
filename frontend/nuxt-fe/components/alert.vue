<template  >
  <div class=" ">
    <!-- info / green -->
    <div v-if="showAlert">
      <div
        v-if="alertColor == 'green'"
        class="mr-5 text-white py-4 pl-2 pr-0 border-0 rounded mb-4 bg-green-700 flex items-center"
      >
        <span class="inline-block text-center font-bold w-2/12"
          >{{ alertType }}
        </span>
        <span class="inline-block text-left w-9/12 mr-5 pl-4">
          {{ alertID }}
        </span>

        <button
          class="focus:outline-none text-2xl inline-block font-bold w-1/12"
          @click="hideAlert(pkey)"
        >
          <span>×</span>
        </button>
      </div>
    </div>

    <!-- error / red -->
    <div v-if="showAlert">
      <div
        v-if="alertColor == 'red'"
        class="mr-5 text-white py-4 pl-2 pr-0 border-0 rounded mb-4 bg-red-500 flex items-center"
      >
        <span class="inline-block text-center font-bold w-2/12"
          >{{ alertType }}
        </span>
        <span class="inline-block text-left w-9/12 mr-5 pl-4">
          {{ alertID }}
        </span>

        <button
          class="focus:outline-none text-2xl inline-block font-bold w-1/12"
          @click="hideAlert(pkey)"
        >
          <span>×</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "alert",
  props: ["pkey", "alertID", "alertType", "alertColor"],
  data() {
    return {
      showAlert: true,
      deletions: 0,
    };
  },
  methods: {
    hideAlert(id) {
      this.showAlert = false;

      if (this.deletions === 0) {
        this.$store.commit("deleteTaskAlert", id);
        this.deletions++;
      }
    },
  },

  mounted() {
    setTimeout(this.hideAlert, 4000, this.pkey);
  },
};
</script>

<style>
</style>