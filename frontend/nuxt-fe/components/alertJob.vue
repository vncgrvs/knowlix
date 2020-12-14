<template  >
  <div v-if="showAlert" id="test">
    <div class="w-full flex justify-end">
      <div class="w-1/4 relative">
        <div
          class="mr-5 text-white px-6 py-4 border-0 rounded mb-4 bg-teal-500 flex items-center"
        >
          <span class="inline-block align-middle mr-8 w-11/12">
            Task {{taskname}} was triggered successfully
          </span>
          <button
            class="focus:outline-none text-2xl inline-block font-bold"
            @click="hideAlert(pkey)"
          >
            <span>×</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "alertJob",
  props: ["pkey", "taskname"],
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
    setTimeout(this.hideAlert, 6000, this.pkey);
  },
};
</script>

<style>
</style>