import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, IconButton } from '@mui/material';
import { FaCartShopping } from "react-icons/fa6"; // Cart icon

const Navbar = () => {
  const navigate = useNavigate();
  const [headerColor, setHeaderColor] = useState("var(--background-color)"); // 헤더 초기 색상
  const [color, setColor] = useState("var(--text-color)"); // 글 색 초기 색상
  const [boxShadow, setBoxShadow] = useState("none"); // 초기 색상



  // 스크롤 위치에 따라 색상 변경
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 70) {
        setHeaderColor("rgba(5, 15, 19, 0.8)"); // 스크롤이 50px 이상일 때 어두운 색상
        setColor("var(--background-color)")
        setBoxShadow("0px 5px 10px rgba(9, 29, 37, 0.2)")

      } else {
        setHeaderColor("var(--background-color)"); // 기본 색상
        setColor("var(--text-color)")
        setBoxShadow("none")
      }
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <AppBar
      position="fixed"
      style={{
        backgroundColor: headerColor, // 스크롤에 따라 배경색 변경
        color:color,
        boxShadow: boxShadow,
        backdropFilter: "blur(10px)",
        transition: "background-color 0.3s ease-out", // 색상 변경에 부드러운 전환 효과
        paddingLeft: "2rem",
        paddingRight: "2rem"

      }}
    >
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1, marginTop: "0px" }} >
          <IconButton color="inherit"  style={{ padding: "10px", margin: "0px" }} onClick={() => {navigate("/home")}} >
            <FaCartShopping size="1.2rem" />
          </IconButton>
        </Typography>
        <Button color="inherit">
          모의 면접
        </Button>
        <Button color="inherit">
          내 히스토리
        </Button>
        &nbsp;&nbsp;&nbsp;
        <Button color="inherit" variant="outlined" onClick={() => {navigate("/login")}} >
          로그인
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
