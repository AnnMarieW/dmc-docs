import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Center("Slide-1", bg="blue", c="white", p=60)),
        dmc.CarouselSlide(dmc.Center("Slide-2", bg="blue", c="white", p=60)),
        dmc.CarouselSlide(dmc.Center("Slide-3", bg="blue", c="white", p=60)),
    ],
    id="carousel-autoplay-props",
    emblaOptions={"loop": True},
    autoplay={"delay": 2000, "stopOnMouseEnter": True, "stopOnInteraction": False},
)
