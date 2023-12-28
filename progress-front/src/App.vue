<!-- partie html  -->
<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <add-list-btn></add-list-btn>
    <!-- <progress-bar-button></progress-bar-button> -->

  </div>
</template>

<script>
// import ProgressBarButton from '@/components/ProgressBarButton.vue';
import AddListBtn from '@/components/AddListBtn.vue';

export default {
  components: {
    // ProgressBarButton
    AddListBtn
  },
  data() {
    return {
      message: 'Bonjour Angele !'
    };
  }
};

</script>

<!-- style css -->
<style>
  @import "@/components/style/variables.css";


  body {
    background-color: var(--bg-color);
    margin: 0; /* Supprime la marge par défaut du corps */
    font-family: 'Rubik', sans-serif;
    color: white;
  }

  #app {
    padding: 20px; /* Ajoute un peu de marge intérieure pour plus de visibilité du texte */
  }

  h1 {
    font-size: 24px; /* Tu peux ajuster la taille de la police selon tes préférences */
    font-weight: bold; /* Pour rendre le texte en gras */
  }
</style>
