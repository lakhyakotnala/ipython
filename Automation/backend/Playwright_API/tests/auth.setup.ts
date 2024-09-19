// auth.setup.ts
// This is currently not active but can be made active through the playwright.config.ts
// The below is an example of how you can save your storage state to a file in the .auth directory

import Env from "@helpers/env";
import { test as setup } from "@playwright/test";

const username = Env.ADMIN_NAME;
const password = Env.ADMIN_PASSWORD;
const authFile = ".auth/admin.json";

setup("authenticate", async ({ request, baseURL }) => {
  await request.post(baseURL + "auth/login", {
    data: {
      username: username,
      password: password,
    },
  });
  await request.storageState({ path: authFile });
});
