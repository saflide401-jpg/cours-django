/* =====================================================================
 * BiblioCampus — interactions UI légères (sans framework JS).
 *
 * Volontairement minimal pour rester compréhensible par des étudiants
 * de L3 qui découvrent Django : ce sont uniquement des améliorations
 * UX progressives. Le site reste 100 % fonctionnel si JS est désactivé.
 * ===================================================================== */

(function () {
  "use strict";

  // -------- 1. Fermeture des alertes/messages --------
  // Un clic sur le bouton × dans une alerte fait disparaître le message.
  document.querySelectorAll(".alert-close").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var alert = btn.closest(".alert");
      if (alert) {
        alert.style.transition = "opacity 200ms";
        alert.style.opacity = "0";
        setTimeout(function () { alert.remove(); }, 220);
      }
    });
  });

  // -------- 2. Confirmation avant action sensible --------
  // Tout formulaire avec [data-confirm="..."] demande confirmation
  // avant soumission. Pédagogiquement, ça illustre l'écoute d'événement
  // et la prévention du comportement par défaut.
  document.querySelectorAll("form[data-confirm]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      var message = form.getAttribute("data-confirm");
      if (message && !window.confirm(message)) {
        event.preventDefault();
      }
    });
  });

  // -------- 3. Auto-soumission douce des filtres du catalogue --------
  // Quand l'étudiant change la catégorie ou coche/décoche "disponibles",
  // on resoumet automatiquement le formulaire (pas besoin de cliquer
  // sur le bouton "Filtrer").
  var filtres = document.getElementById("filtres-catalogue");
  if (filtres) {
    filtres.querySelectorAll("select, input[type='checkbox']").forEach(function (input) {
      input.addEventListener("change", function () { filtres.submit(); });
    });
  }

  // -------- 4. Recherche avec petit délai (debounce) --------
  // La recherche texte se déclenche après 600 ms sans frappe,
  // pour éviter une requête à chaque caractère.
  var searchInput = filtres ? filtres.querySelector("input[type='search']") : null;
  if (searchInput) {
    var timer = null;
    searchInput.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(function () { filtres.submit(); }, 600);
    });
  }

  // -------- 5. Disparition automatique des messages de succès --------
  // Les notifications "success" s'effacent après 5 secondes.
  setTimeout(function () {
    document.querySelectorAll(".alert-success").forEach(function (alert) {
      alert.style.transition = "opacity 400ms";
      alert.style.opacity = "0";
      setTimeout(function () { alert.remove(); }, 420);
    });
  }, 5000);
})();
