import { useMutation } from "@tanstack/react-query";
import axios from "axios";

// interface Visitor {
//   form: number;
//   auth_type: string;
//   auth_value: string;
// }

function createVisitor(data) {
  return axios.post("http://127.0.0.1:8000/api/visitor/auth/", data);
}

export default function useCreateVisitor() {
  return useMutation(createVisitor);
}
