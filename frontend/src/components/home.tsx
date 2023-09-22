import { Box, Typography } from "@mui/material";
import { Link } from "react-router-dom";

export default function Home() {
  let formId = "python";
  return (
    <Box>
      <Link to={`/${formId}`}>
        <Typography variant="h5">{`http://127.0.0.1:8000/api/visitor/form/${formId}`}</Typography>
      </Link>
    </Box>
  );
}
