import { create } from "zustand";
type AuthState = {
  formAuthValue: string;
  authError: boolean;
};

type AuthAction = {
  setFormAuthValue: (formAuthValue: AuthState["formAuthValue"]) => void;
  setAuthError: (authError: AuthState["authError"]) => void;
};

export const useAuthCheckStore = create<AuthState & AuthAction>((set) => ({
  formAuthValue: "",
  authError: false,
  setFormAuthValue: (authValue) => set(() => ({ formAuthValue: authValue })),
  setAuthError: (errorValue) => set(() => ({ authError: errorValue })),
}));
