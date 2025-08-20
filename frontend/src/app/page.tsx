"use client";
import { useUser } from "@auth0/nextjs-auth0/client";
import Link from "next/link";
import { useEffect } from "react";

export default function Home() {
  const { user, error, isLoading } = useUser();

  useEffect(() => {
    const handleTestApi = async () => {
      try {
        const tokenRes = await fetch("/api/token");
        const { accessToken } = await tokenRes.json();
        const res = await fetch("http://127.0.0.1:8000/news", {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        const data = await res.json();
        console.log("Backend response:", data);
      } catch (er) {
        console.error(er);
      }
    };

    if (user) {
      handleTestApi();
    }
  }, [user]);

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>{error.message}</p>;

  return (
    <div className="flex h-screen items-center justify-center">
      {user ? (
        <div className="flex flex-col items-center gap-4">
          <p>Welcome {user.name} 🎉</p>
          <Link
            href="/api/auth/logout"
            className="rounded-lg bg-red-500 px-4 py-2 text-white hover:bg-red-600"
          >
            Logout
          </Link>
        </div>
      ) : (
        <Link
          href="/api/auth/login"
          className="rounded-lg bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
        >
          Login
        </Link>
      )}
    </div>
  );
}
