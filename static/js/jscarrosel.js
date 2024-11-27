document.querySelectorAll('.carousel').forEach(carousel => {
  const prevBtn = carousel.querySelector('.prev');
  const nextBtn = carousel.querySelector('.next');
  const carouselSlide = carousel.querySelector('.carousel-slide');
  const cursoId = carousel.dataset.cursoId;

  let currentPage = 0;
  const items = carousel.querySelectorAll('.item');
  const itemsPerPage = 5;
  const totalPages = Math.ceil(items.length / 2) + 1;

  nextBtn.addEventListener('click', () => {
    if (currentPage < totalPages) {
      currentPage++;
      updateSlidePosition();
    }
  });

  prevBtn.addEventListener('click', () => {
    if (currentPage > 0) {
      currentPage--;
      updateSlidePosition();
    }
  });

  function updateSlidePosition() {
    const startPosition = currentPage * itemsPerPage * 1.9;
    carouselSlide.style.transform = `translateX(-${startPosition}%)`;
  }
});
