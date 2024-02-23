document.addEventListener("DOMContentLoaded", () => {
    const latinText = document.querySelector(".latin-text");
    const translationText = document.querySelector(".translation-text");

    let isSyncingLeftScroll = false;
    let isSyncingRightScroll = false;

    latinText.addEventListener("scroll", () => {
        if (!isSyncingLeftScroll) {
            isSyncingRightScroll = true;
            translationText.scrollTop = latinText.scrollTop;
        }
        isSyncingLeftScroll = false;
    });

    translationText.addEventListener("scroll", () => {
        if (!isSyncingRightScroll) {
            isSyncingLeftScroll = true;
            latinText.scrollTop = translationText.scrollTop;
        }
        isSyncingRightScroll = false;
    });
});
