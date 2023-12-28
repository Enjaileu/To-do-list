<!-- AddListBtn.vue -->
<template>
    <button @click="handleClick" class="add-list-btn">
      <span class="button-text">+</span>
    </button>
    <add-list-modal :isModalVisible="isModalVisible" @add-list="handleAddList" @cancel="handleCancel" />
  </template>
  
  <script>
  import AddListModal from "@/components/AddListModal.vue";
  
  export default {
    data() {
        return {
            isModalVisible: false,
        };
    },
    methods: {
        handleClick() {
            this.isModalVisible = true;
        },
        handleAddList(listTitle) {
            // Logique pour ajouter la nouvelle liste
            console.log("Adding new list with title:", listTitle);
            // Ferme la fenêtre modale
            this.isModalVisible = false;
        },
        handleCancel(){
            this.isModalVisible = false;
        }
    },
    components: {
        AddListModal,
     },
  };
  </script>
  
  <style scoped>
  @import "style/variables.css";
  .add-list-btn {
    width: calc(100vw / 6); /* 1/6 de la largeur de l'écran */
    height: calc(100vw / 6); /* 1/6 de la largeur de l'écran */
    background-color: var(--primary-color);
    color: black;
    border: none;
    border-radius: 10px; /* Bords arrondis */
    cursor: pointer;
  }
  
  /* Style du texte à l'intérieur du bouton */
  .button-text {
    font-size: 24px; /* Taille du texte par défaut */
    line-height: calc(100vw / 6); /* Centrage vertical du texte dans le bouton */
  }
  </style>
  