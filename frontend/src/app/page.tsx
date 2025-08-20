"use client";
import { useUser } from "@auth0/nextjs-auth0/client";
import Link from "next/link";

export default function Home() {
  const { user, error, isLoading } = useUser();

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
