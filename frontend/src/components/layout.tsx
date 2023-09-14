import { Outlet } from "react-router-dom";
import { Container, Box } from "@mui/material";

export default function Layout() {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        width: "100vw",
        overflow: "hidden",
      }}
    >
      {/* <Box
        sx={{
          backgroundColor: "#FDA9FF",
          width: "411px",
          height: "411px",
          borderRadius: "50%",
          position: "fixed",
          top: "-96px",
          left: "-104px",
        }}
      />
      <Box
        sx={{
          backgroundColor: "#fff",
          width: "307px",
          height: "307px",
          borderRadius: "50%",
          position: "fixed",
          top: "-197px",
          left: "142px",
        }}
      /> */}
      <Container maxWidth="sm">
        <Outlet />
      </Container>
      {/* <Box
        sx={{
          backgroundColor: "#9AFFED",
          width: "307px",
          height: "307px",
          borderRadius: "50%",
          position: "fixed",
          right: "-110px",
          bottom: "100px",
        }}
      />
      <Box
        sx={{
          backgroundColor: "#FFEE94",
          width: "307px",
          height: "307px",
          borderRadius: "50%",
          position: "fixed",
          right: "-150px",
          bottom: "-100px",
        }}
      /> */}
    </Box>
  );
}
