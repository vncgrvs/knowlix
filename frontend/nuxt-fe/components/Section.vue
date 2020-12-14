<template>
  <div class="flex justify-around pt-10 font-lix">
    <!-- List One -->
    <div
      class="block justify-center bg-lix-third w-2/5 px-6 mb-10 pb-5 divide-y divide-white divide-solid min-h-screen rounded-md "
    >
      <p class="text-white text-3xl mt-3 -pm-4">Available Sections</p>
      <draggable class="-mt-2 pt-3" v-model="sections" group="sections">
        <div
          v-for="(section, index) in sections"
          v-bind:class="{ drag: isDragging }"
          :key="index"
          class="flex drag bg-white items-center h-10 px-4 shadow-md cursor-move item mt-2 font-medium antialiased"
        >
          <svg
            class="fill-current text-teal-500 mr-8 h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M1,1 L19,1 L19,3 L1,3 L1,1 Z M1,9 L19,9 L19,11 L1,11 L1,9 Z M1,17 L19,17 L19,19 L1,19 L1,17 Z M1,5 L19,5 L19,7 L1,7 L1,5 Z M1,13 L19,13 L19,15 L1,15 L1,13 Z"
            ></path>
          </svg>
          <span class="w-full flex justify-center"> {{ section }}</span>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            @click="moveToUserChoice(index, section)"
            class="h-8 w-8 text-blue-800 hover:text-teal-500 cursor-pointer"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
      </draggable>
    </div>
    <!--   -->

    <!-- List Two -->
    <div
      class="block justify-center bg-lix-second w-2/5 px-6 mb-10 pb-5 divide-y divide-white divide-solid min-h-screen rounded-md "
    >
      <p class="text-white text-3xl mt-3 -pm-4">Your Onboarding Deck</p>
      <draggable
        class="-mt-2 pt-3"
        v-model="userChoice"
        group="sections"
        :swapThreshold="0.9"
      >
        <div
          v-for="(section, index) in userChoice"
          v-bind:class="{ drag: isDragging }"
          :key="index"
          class="flex drag bg-white items-center h-10 px-4 shadow-xl cursor-move item mt-2 font-medium antialiased"
        >
          <div
            class="bg-teal-500 rounded-full h-6 w-10 flex items-center justify-center text-gray-300 font-extrabold"
          >
            {{ index + 1 }}
          </div>
          <span class="w-full flex justify-center"> {{ section }}</span>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            class="h-8 w-8 text-blue-800 hover:text-teal-500 cursor-pointer"
            viewBox="0 0 24 24"
            @click="moveToList(index, section)"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
      </draggable>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  name: "Section",

  data() {
    return {
      isDragging: false,
    };
  },

  computed: {
    sections: {
      get() {
        return this.$store.state.list;
      },
      set(val) {
        const container = [];

        val.map((value, index) => {
          var i_new = index + 1;
          var out = { pos: i_new, name: value };
          container.push(out);
          return container;
        });

        this.$store.dispatch("updateList", val);
      },
    },
    userChoice: {
      get() {
        return this.$store.state.userChoice;
      },
      set(val) {
        const container = [];

        val.map((value, index) => {
          var i_new = index + 1;
          var out = { pos: i_new, name: value };
          container.push(out);
          return container;
        });

        this.$store.dispatch("updateUserChoiceList", val);
      },
    },
  },
  methods: {
    moveToList(index, section) {
      this.$store.dispatch("appendList", section);
      this.$store.dispatch("deleteUserChoice", index);
    },
    moveToUserChoice(index,section){
      this.$store.dispatch('appendUserChoice', section);
      this.$store.dispatch('deleteListItem', index);
    }
  },
};
</script>

<style>
</style>