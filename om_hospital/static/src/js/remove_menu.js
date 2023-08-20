// import { registry } from "@web/static/src/core/registry";
// import { patch } from "@web/static/src/core/utils/patch";
// import { preferencesItem } from "@web/webclient/user_menu/user_menu_items";
// import { routeToUrl } from "@web/core/browser/router_service";
// import { browser } from "web/static/src/core/browser/browser";
// import { Dialog } from "web/static/src/core/dialog/dialog";
// import { _lt } from "web/static/src/core/l10n/translation";
// import { session } from "@web/static/src/session";

// const usersMenuRegistry = registry.category("user_menuitems");

// function debugItems(env) {
//   const URL = $.param.querystring(window.location.href, 'debug=1');
//   return {
//       type: "item",
//       id: "debug",
//       description: env._t("Activate developer mode"),
//       href: URL,
//       callback: () => {
//           browser.open(URL, "_self");
//       },
//       sequence: 50,
//   };
// }
// registry.category("user_menuitems").remove("documentation", documentationItem)