import { l as pop, p as push, m as ensure_array_like, n as attr_class, q as attr_style, t as escape_html, u as fallback, v as attr, w as bind_props, x as stringify, y as slot } from "../../chunks/index.js";
import "clsx";
function Header($$payload, $$props) {
  push();
  {
    $$payload.out += "<!--[!-->";
  }
  $$payload.out += `<!--]-->`;
  pop();
}
function NavMenu($$payload, $$props) {
  push();
  const menuItems = [];
  let hoveredIndex = null;
  $$payload.out += `<nav>`;
  if (menuItems.length) {
    $$payload.out += "<!--[-->";
    const each_array = ensure_array_like(menuItems);
    $$payload.out += `<ul class="nav-menu-list svelte-8v1nae"><!--[-->`;
    for (let i = 0, $$length = each_array.length; i < $$length; i++) {
      let item = each_array[i];
      $$payload.out += `<li${attr_class("svelte-8v1nae", void 0, { "selected": item.selected })}${attr_style("", {
        "background-color": hoveredIndex === i && !item.selected ? "var(--nav-menu-hover)" : item.selected ? "var(--accent)" : "transparent",
        color: item.selected ? "var(--main-bg)" : "var(--main-text)"
      })}>${escape_html(item.name)}</li>`;
    }
    $$payload.out += `<!--]--></ul>`;
  } else {
    $$payload.out += "<!--[!-->";
  }
  $$payload.out += `<!--]--></nav>`;
  pop();
}
function UrlInput($$payload, $$props) {
  let placeholder = fallback($$props["placeholder"], "Paste article URL here to depolarize");
  let value = fallback($$props["value"], "");
  let onInput = fallback($$props["onInput"], () => {
  });
  $$payload.out += `<section class="url-input-section"><input type="text" class="url-input"${attr("placeholder", placeholder)}${attr("value", value)}></section>`;
  bind_props($$props, { placeholder, value, onInput });
}
function ContentViewer($$payload) {
  $$payload.out += `<section class="content-viewer"><h2>Comer Refers Cuomo to DOJ for Criminal Prosecution</h2> <div class="article-meta"><span>By Mark Swanson | Monday, 21 April 2025 04:25 PM EDT</span></div> <div class="article-body"><p>House Oversight Committee Chairman James Comer, R-Ky., resent a criminal referral to the Department of Justice on Monday recommending that former New York Gov. Andrew Cuomo be charged with making false statements to Congress.</p> <p>Comer charges that Cuomo, a Democrat, "knowingly and willfully" lied to the House Select Subcommittee about his knowledge and involvement of a 2020 report regarding the COVID-19 "nursing home <span class="polarizing-language">disaster</span>" and "the ensuing <span class="polarizing-language">cover-up</span>."</p> <p>Comer and Select Committee Republicans assert that Cuomo took an active role in drafting and editing the New York State Department of Health report to dodge responsibility for the thousands of lost lives during the pandemic.</p> <p>"Andrew Cuomo is a man with a history of <span class="polarizing-language">corruption</span> and <span class="polarizing-language">deceit</span>, now caught <span class="polarizing-language">red-handed</span> lying to Congress during the Select Subcommittee's investigation into the COVID-19 nursing home <span class="polarizing-language">tragedy</span> in New York. This wasn't a slip-up — it was a <span class="polarizing-language">calculated cover-up</span> by a man seeking to shield himself from responsibility for the <span class="polarizing-language">devastating</span> loss of life in New York's nursing homes," Comer said in a Monday release.</p> <p>Cuomo is polling as one of the top Democrat candidates in the New York City mayoral race. The election is Nov. 4.</p> <p>Select Committee Chairman Brad Wenstrup, R-Ohio, sent a criminal referral against Cuomo dated Oct. 30 to former Attorney General Merrick Garland asserting that Cuomo made false statements in a transcribed interview with the committee on June 11.</p></div></section> `;
  UrlInput($$payload, {});
  $$payload.out += `<!---->`;
}
function FillerTextBlock($$payload, $$props) {
  push();
  const {
    minParagraphs = 2,
    maxParagraphs = 4,
    minLinesPerParagraph = 3,
    maxLinesPerParagraph = 7
  } = $$props;
  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  function generateRandomWidth(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
  }
  function generateRegularLineWidth() {
    return generateRandomWidth(70, 100);
  }
  function generateLastLineWidth() {
    return generateRandomWidth(10, 90);
  }
  function generateParagraphLines() {
    const numLines = getRandomInt(minLinesPerParagraph, maxLinesPerParagraph);
    return Array(numLines).fill(0).map((_, index) => index === numLines - 1 ? generateLastLineWidth() : generateRegularLineWidth());
  }
  function generateAllParagraphs() {
    const numParagraphs = getRandomInt(minParagraphs, maxParagraphs);
    return Array(numParagraphs).fill(0).map(() => generateParagraphLines());
  }
  let paragraphLines = generateAllParagraphs();
  let visible = true;
  setInterval(
    () => {
      visible = false;
      setTimeout(
        () => {
          paragraphLines = generateAllParagraphs();
          visible = true;
        },
        200
      );
    },
    getRandomInt(2e4, 6e4)
  );
  $$payload.out += `<div class="module filler-text-block svelte-18nm7nt"><div>`;
  if (visible) {
    $$payload.out += "<!--[-->";
    const each_array = ensure_array_like(paragraphLines);
    $$payload.out += `<!--[-->`;
    for (let pIndex = 0, $$length = each_array.length; pIndex < $$length; pIndex++) {
      let paragraph = each_array[pIndex];
      const each_array_1 = ensure_array_like(paragraph);
      $$payload.out += `<div class="paragraph svelte-18nm7nt"><!--[-->`;
      for (let lIndex = 0, $$length2 = each_array_1.length; lIndex < $$length2; lIndex++) {
        let lineWidth = each_array_1[lIndex];
        $$payload.out += `<div class="line svelte-18nm7nt"${attr_style(`width: ${stringify(lineWidth)}%`)}></div>`;
      }
      $$payload.out += `<!--]--></div>`;
    }
    $$payload.out += `<!--]-->`;
  } else {
    $$payload.out += "<!--[!-->";
  }
  $$payload.out += `<!--]--></div></div>`;
  pop();
}
function FillerImageBlock($$payload, $$props) {
  let minWidth = fallback($$props["minWidth"], 70);
  let maxWidth = fallback($$props["maxWidth"], 100);
  let height = fallback($$props["height"], "0.8em");
  let gap = fallback($$props["gap"], "0.5em");
  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  function generateWidths() {
    return {
      first: getRandomInt(minWidth, maxWidth),
      second: getRandomInt(minWidth, maxWidth)
    };
  }
  let widths = generateWidths();
  setInterval(
    () => {
      widths = generateWidths();
    },
    getRandomInt(1e4, 15e3)
  );
  $$payload.out += `<div class="module filler-image-block svelte-1ctnizh"><div class="line"${attr_style(`height: ${stringify(height)}; width: ${stringify(widths.first)}%; margin-bottom: ${stringify(gap)};`)}></div> <div class="line"${attr_style(`height: ${stringify(height)}; width: ${stringify(widths.second)}%`)}></div></div>`;
  bind_props($$props, { minWidth, maxWidth, height, gap });
}
function About($$payload) {
  $$payload.out += `<div class="module info-panel svelte-18mnr9x"><p class="svelte-18mnr9x">deconstructed is a tool designed to combat division and distrust in society by providing neutral, emotion-free news.</p></div>`;
}
function SplashOverlay($$payload, $$props) {
  push();
  {
    $$payload.out += "<!--[-->";
    $$payload.out += `<button type="button" class="splash-overlay svelte-128s4zk">`;
    {
      $$payload.out += "<!--[!-->";
    }
    $$payload.out += `<!--]--> <span class="splash-title svelte-128s4zk">de · con · struct · ed</span></button>`;
  }
  $$payload.out += `<!--]-->`;
  pop();
}
function _layout($$payload, $$props) {
  SplashOverlay($$payload);
  $$payload.out += `<!----> <div class="grid-container">`;
  Header($$payload);
  $$payload.out += `<!----> <div class="left-column"><div class="module nav-menu">`;
  NavMenu($$payload);
  $$payload.out += `<!----></div> `;
  FillerImageBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----></div> <div class="main-column"><div class="module content-viewer">`;
  ContentViewer($$payload);
  $$payload.out += `<!----> <!---->`;
  slot($$payload, $$props, "default", {});
  $$payload.out += `<!----></div></div> <div class="right-column">`;
  About($$payload);
  $$payload.out += `<!----> <div class="module url-input-module">`;
  UrlInput($$payload, {});
  $$payload.out += `<!----></div> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----> `;
  FillerTextBlock($$payload, {});
  $$payload.out += `<!----></div></div>`;
}
export {
  _layout as default
};
