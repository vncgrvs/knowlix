<template>
  <!-- header text -->
  <div
    class="w-full h-full min-h-screen py-12 px-6 bg-gray-100 bg-opacity-50 font-lix overflow-hidden"
  >
    <div class="flex-col mb-6">
      <h2
        class="text-5xl text-center text-gray-700 font-extrabold tracking-tight mb-2"
      >
        Onboarding Plan
      </h2>
      <p class="text-center font-thin text-gray-600 text-xl mb-6">
        Choose your approach according to your customer's profile
      </p>
      <div class="h-1 mx-auto bg-lix-main w-24 rounded"></div>
    </div>

    <!-- cards pane -->
    <div class="px-40 mt-20 flex flex-row justify-evenly">
      <!-- Onboarding Basic -->
      <transition name="test">
        <div
          class="flex flex-col h-auto w-4/12 bg-white rounded border border-gray-300 shadow-md hover:border-blue-600 hover:border-4"
        >
          <div>
            <!-- card/header section -->
            <div class="flex-col border-b border-gray-300">
              <div class="pt-5 px-8">
                <h2
                  class="font-medium tracking-tight text-left text-2xl text-gray-700 mb-6"
                >
                  Basic
                </h2>
                <p class="h-10 font-thin text-left text-md text-gray-600 mb-12">
                  Very rigid 4-week sprint onboarding guide
                </p>

                <button
                  class="focus:outline-none bg-lix-second rounded-md w-full py-1 px-16 hover:bg-opacity-80 mb-10"
                >
                  <p class="text-white text-center">Get Basic Plan</p>
                </button>
              </div>
            </div>
            <!-- card/body section -->
            <div class="flex-col">
              <div class="pt-5 px-8">
                <p
                  class="text-left uppercase tracking-tight text-sm text-gray-600 mb-3"
                >
                  Customer Profile
                </p>
                <!-- card/body section/ticks -->
                <div class="mb-4 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis iste natus error sit
                  </p>
                </div>
                <!-- card/body section/ticks -->
                <div class="mb-4 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis
                  </p>
                </div>
                <!-- card/body section/ticks -->
                <div class="mb-4 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis
                  </p>
                </div>
                <!-- card/body section/ticks -->
                <div class="mb-8 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
      <!-- Onboarding Modularh -->
      <transition name="modular_onboarding">
        <div
          class="flex flex-col h-auto w-4/12 bg-white rounded border border-gray-300 shadow-md hover:border-blue-600 hover:border-4"
        >
          <div>
            <!-- card/header section -->
            <div class="flex-col border-b border-gray-300">
              <div class="pt-5 px-8">
                <h2
                  class="font-medium tracking-tight text-left text-2xl text-gray-700 mb-6"
                >
                  Modular
                </h2>
                <p class="h-10 font-thin text-left text-md text-gray-600 mb-12">
                  Tailor your onboarding flexibily to your customer's need. It's
                  buffet time!
                </p>
                <nuxt-link to="/onboarding/modular">
                  <button
                    class="focus:outline-none bg-lix-second rounded-md w-full py-1 px-16 hover:bg-opacity-80 mb-10"
                  >
                    <p class="text-white text-center">Get Modular Plan</p>
                  </button>
                </nuxt-link>
              </div>
            </div>
            <!-- card/body section -->
            <div class="flex-col">
              <div class="pt-5 px-8">
                <p
                  class="text-left uppercase tracking-tight text-sm text-gray-600 mb-3"
                >
                  Customer Profile
                </p>
                <!-- card/body section/ticks -->
                <div class="mb-4 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis iste natus error sit
                  </p>
                </div>
                <!-- card/body section/ticks -->
                <div class="mb-4 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis
                  </p>
                </div>
                <!-- card/body section/ticks -->
                <div class="mb-4 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis
                  </p>
                </div>
                <!-- card/body section/ticks -->
                <div class="mb-8 flex flex-nowrap">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="h-5 w-5 text-green-600 mr-4 flex-shrink-0 self-center justify-self-center"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <p class="font-thin text-left text-sm text-gray-600">
                    Sed ut perspiciatis unde omnis
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "landingpage",
};
</script>

<style>
.test-enter{
  animation:fadeIn ;
  animation-duration:0.8s ;
  
}

</style>