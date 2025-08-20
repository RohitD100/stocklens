/* eslint-disable @typescript-eslint/no-explicit-any */
import { withApiAuthRequired, getAccessToken } from "@auth0/nextjs-auth0";
import type { NextApiRequest, NextApiResponse } from "next";

export default withApiAuthRequired(async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const audience = process.env.AUTH0_API_AUDIENCE;
    if (!audience) {
      throw new Error("AUTH0_API_AUDIENCE is not defined");
    }

    // Correct: pass audience inside authorizationParams
    const { accessToken } = await getAccessToken(req, res, {
      authorizationParams: {
        audience,
      },
    });

    res.status(200).json({ accessToken });
  } catch (error: any) {
    console.error(error);
    res.status(500).json({ error: error.message });
  }
});
