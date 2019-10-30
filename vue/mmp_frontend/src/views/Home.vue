<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Question msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Question from '@/components/Question.vue'

export default {
  name: 'home',
  components: {
    Question
  }
}
</script>
