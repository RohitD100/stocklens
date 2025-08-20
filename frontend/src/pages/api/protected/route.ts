import { getSession } from "@auth0/nextjs-auth0";

export async function GET(req: Request) {
  console.log("req :", req);
  const session = await getSession();

  if (!session?.user) {
    return new Response("Unauthorized", { status: 401 });
  }

  return Response.json({
    message: "This is a protected App Router API route",
    user: session.user,
  });
}
