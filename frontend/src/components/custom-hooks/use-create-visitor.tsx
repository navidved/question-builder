import { useMutation } from "@tanstack/react-query";
import axios from "axios";

interface Visitor {
  form: number;
  auth_type: string;
  auth_value: string;
}

const createVisitor = async (data: Visitor) => {
  const { data: response } = await axios.post(
    "http://127.0.0.1:8000/api/visitor/create",
    data
  );
  return response.data;
};

export default function useCreateVisitor() {
  return useMutation(createVisitor);
}
