import { Box } from "@mui/material";
import { Link } from "react-router-dom";

export default function Home() {
  let formId = "python";
  return (
    <Box>
      <Link
        to={`/${formId}`}
      >{`http://127.0.0.1:8000/api/visitor/${formId}`}</Link>
    </Box>
  );
}
