<!-- ProgressBarButton.vue -->
<template>
    <div class="progress-bar-button">
      <div class="bar-container">
        <div :style="{ width: progressBarWidth }" class="progress-bar"></div>
        <div class="background-bar"></div>
      </div>
      <button @mousedown="handleButtonPress" @mouseup="handleButtonRelease" @click="handleButtonClick" class="add-button">
        <span class="button-text">+</span>
      </button>
    </div>
</template>

<script>
export default {
  data() {
    return {
      buttonActive: false,
      progress: 0
    };
  },
  methods: {
    handleButtonClick() {
      // Augmente la progression de 10%
      this.progress += 10;

      // Limiter la progression à 100%
      if (this.progress > 100) {
        this.progress = 100;
      }
    },
    handleButtonPress() {
      this.buttonActive = true;
    },
    handleButtonRelease() {
      this.buttonActive = false;
    }
  },
  computed: {
    progressBarWidth() {
      return this.progress + '%';
    }
  }
};
</script>

<style scoped>
.progress-bar-button {
  position: relative;
  display: flex;
  align-items: center;
}

.bar-container {
  position: relative;
  height: 10px;
  flex: 1;
}

.background-bar,
.progress-bar {
  position: absolute;
  top: 0;
  left: 0;
  height: 10px;
  border-radius: 5px;
}

.background-bar {
  width: 100%;
  background-color: #4CAF50; /* Barre verte en arrière-plan */
  z-index: 0;
}

.progress-bar {
  background-color: #BE3144; /* Barre rouge qui représente la progression */
  z-index: 1; /* Met la barre de progression au-dessus de la barre d'arrière-plan */
  transition: width 0.2s ease; /* Ajoute une transition à la propriété width */
}

.add-button {
  width: 30px;
  height: 30px;
  background-color: #4CAF50; /* Couleur de fond du bouton en harmonie avec la barre verte */
  color: black;
  border: none;
  border-radius: 50%;
  margin-left: 10px;
  cursor: pointer;
  position: relative;
}

/* Style lorsque le bouton est actif (enfoncé) */
.add-button:active {
  transform: scale(0.9); /* Réduit légèrement la taille du bouton */
  background-color: #45A049; /* Couleur de fond du bouton légèrement plus claire */
}

/* Style du texte à l'intérieur du bouton */
.button-text {
  font-size: 16px; /* Taille du texte par défaut */
}

/* Style du texte lorsque le bouton est actif (enfoncé) */
.add-button.active .button-text {
  font-size: 14px; /* Taille du texte lorsqu'il est actif */
}
</style>
