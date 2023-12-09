from flask import Blueprint, request
from flask import render_template

bp = Blueprint('main', __name__, url_prefix='/')

data = [
  {
     "title": "코딩을 처음 하는 초보자들도 쉽게 배울 수 있는 초간단 파이썬(python) 무료 강의!",
     "image_url": "https://i.ytimg.com/vi/kWiCuklohdY/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDSzkhzgjYnt4DpcxHMmMKwCKHXgA",
     "link": "https://youtu.be/kWiCuklohdY?si=qQu5-g4U0D1_YvJe",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "html, css 없이 간편하게 웹디자인하기! BootStrap 활용 무료 강의",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA3MTJfMTI2%2FMDAxNjg5MTUwMDAzMDU2.7JkbRPE7Fhy5EMKwN5JlAUHLZ8BZ5NZxK9n9p-wnfQcg.eAZpJovsoWYV5WQlynhBDuk2hfsOgx_omFTo2ossuJgg.PNG.m_biz%2Fbootstrap.png&type=a340",
     "link": "https://youtu.be/3Az_hKsL9L8?si=XfE2krG0cdy55eCs",
     "source": "코딩알려주는누나 YOUTUBE"
  },
  {
     "title": "C 언어를 처음 접하는 사람들을 위한 C언어 무료 강의",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA4MjRfMTA5%2FMDAxNjkyODY2MTYwMjE5.uyx5PWvCl2o5GFdkCbchfT3C9DLzgYrTOViHmNmK5Vkg.TfivH8RnFQh_9IIrm-zytb8fJgj2Kq00XDWj7vHJh6Ag.PNG.teambloky12%2Fimage.png&type=l340_165",
     "link": "https://youtu.be/q6fPjQAzll8?si=JFDT14J43epok8t9",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "프론트엔드와 백엔드의 차이점은 뭘까? 웹개발이 목표라면 도움 될 기본 용어 정리!",
     "image_url": "https://i.ytimg.com/vi/aXi1H_4ncvs/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCL3M_kjQ785cNlpSX9Ap64H0YdSw",
     "link": "https://youtu.be/aXi1H_4ncvs?si=EsKpFO6DZNgBfYA",
     "source": "짐코딩 YOUTUBE"
  },
  {
     "title": "게임을 만들어 보고 싶은 사람들을 위한 Unity 무료 강의",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F8f%2Fb8%2Fd8%2F8fb8d89c878297b379aa8262ac977eef.jpg&type=a340",
     "link": "https://youtu.be/rJE6bhVUNhk?si=oY0_GJ2y8u6SVFjQ",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "프론트엔드와 백엔드의 차이점은 뭘까? 웹개발이 목표라면 도움 될 기본 용어 정리!",
     "image_url": "https://i.ytimg.com/vi/aXi1H_4ncvs/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCL3M_kjQ785cNlpSX9Ap64H0YdSw",
     "link": "https://youtu.be/aXi1H_4ncvs?si=EsKpFO6DZNgBfYA",
     "source": "짐코딩 YOUTUBE"
  },
  {
     "title": "mz 세대에 찾아온 코딩 열풍! 그 실상은 어떠할까?",
     "image_url": "https://i.ytimg.com/vi/u_kvcvvqTes/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLA28WeYGioRQ5_VL1kj6AfMJ9u7nw",
     "link": "https://youtu.be/u_kvcvvqTes?si=8ZHQkK5weov_RIyG",
     "source": "SBS News"
  },
  {
     "title": "본인 진로로 프론트 엔드 개발자와 백엔드 개발자 중 고민 중이라면, 이 영상을 보시는 것을 추천드립니다.",
     "image_url": "https://i.ytimg.com/vi/S9qAtvvvxio/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBjkYYeCW7HZeXMbGFH4snz7S6oiw",
     "link": "https://youtu.be/S9qAtvvvxio?si=ORCpH_Li0TiPJgrR",
     "source": "테헤란벨리 YOUTUBE"
  },
  {
     "title": "파이썬 가상 환경을 사용하는 방법을 알아보자! 파이썬 가상 환경 무료 강의",
     "image_url": "https://i.ytimg.com/vi/o_vKT80BBkw/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAnreUpsxByEl_SFFK-l3NvwTvv_w",
     "link": "https://youtu.be/o_vKT80BBkw?si=CI5zXGS4ZWBCnysq",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "영상으로 빠르게 배워보는 Github 사용법과 Git 설치 방법!",
     "image_url": "https://i.ytimg.com/vi/Fley6IFhlC8/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAlxIsdEUkOdj3l4bfXnaPC4laERw",
     "link": "https://youtu.be/aXi1H_4ncvs?si=EsKpFO6DZNgBfYA",
     "source": "코딩알려주는누나 YOUTUBE"
  },
  {
     "title": "파이썬을 활용해서 머신러닝을 해보자! 파이썬 응용 무료 강의",
     "image_url": "https://i.ytimg.com/vi/TNcfJHajqJY/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCxEcKcuvYlucaMKNbX3H-KE-PULw",
     "link": "https://youtu.be/TNcfJHajqJY?si=16gWlJNFK6hEFe-w",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "웹개발, 어디서부터 시작할지 모르겠다면 로드맵을 참고해보시는 건 어떨까요?",
     "image_url": "https://academy.dream-coding.com/logo-long.svg",
     "link": "https://academy.dream-coding.com/pages/roadmap?tab=basic",
     "source": "짐코딩 YOUTUBE"
  },
  {
     "title": "프론트엔드와 백엔드의 차이점은 뭘까? 웹개발이 목표라면 도움 될 기본 용어 정리!",
     "image_url": "https://i.ytimg.com/vi/aXi1H_4ncvs/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCL3M_kjQ785cNlpSX9Ap64H0YdSw",
     "link": "https://youtu.be/aXi1H_4ncvs?si=EsKpFO6DZNgBfYA",
     "source": "Dream Coding Academy"
  },
  {
     "title": "9시간만 투자하면 여러분도 Java를 활용해 웹사이트 만들 수 있습니다. Java 무료 강의",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDAzMDlfMTM4%2FMDAxNTgzNzQzNDg1MzE1.kpMBeFFV4b0N_Va9AAFzsCLzt2K1NgMgQTPN2jX2zIQg.akwx66cB5rgWQWDlN0fDNFdMVDV2_vI1qLacXfqr-RAg.JPEG.7887yj%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5.jpg&type=a340",
     "link": "https://youtu.be/NQq0dOoEPUM?si=PYWw6JbnjWVI6BqV",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "SKT에서 개발 중이라는 비전 AI를 활용한 발달장애인 분석 기술에 관하여",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20230806_113%2F1691252772679W6Axc_JPEG%2F92388556395614812_650929349.jpg&type=a340",
     "link": "https://biz.newdaily.co.kr/site/data/html/2023/11/07/2023110700127.html",
     "source": "뉴 데일리 경제, 김병욱 기자"
  },
  {
     "title": "게임 개발자가 게임 개발 포기하고 웹 개발자가 된 현실적인 이야기.",
     "image_url": "https://i.ytimg.com/vi/z2xxff3OpFQ/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCp1vXWb9_qnjFaz9N-iJHQ1UrRkQ",
     "link": "https://youtu.be/z2xxff3OpFQ?si=ofl1-t2ZPvhomALL",
     "source": "코딩루팡 YOUTUBE"
  },
  {
     "title": "조선일보 전광판 해킹했던 그 학생.. 근황을 알아보자.",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDEyMTNfODQg%2FMDAxNjA3ODE5MDYyNzg0.cvkQPkcYoq0fGwwZDCNZEuwDjX7jX5pdUX_B9fT638Ag.Oteah3UW34fr6W3xmXBLJ3oNUXU9iC9AIqV67pHMpO4g.JPEG.cydogg%2FSE-a7b5dac3-e643-4b29-bd62-c838a4a9ae76.jpg&type=a340 ",
     "link": "https://youtu.be/F-HGnmTQE20?si=mAuyM-VMYVolmfos",
     "source": "긱블 YOUTUBE"
  },
  {
     "title": "국어국문학과를 생각하는 학생들에게 드리는 학과 추천 가이드!",
     "image_url": "https://i.ytimg.com/vi/aXi1H_4ncvs/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCL3M_kjQ785cNlpSX9Ap64H0YdSw",
     "link": "https://youtu.be/aXi1H_4ncvs?si=EsKpFO6DZNgBfYA",
     "source": "짐코딩 YOUTUBE"
  },
  {
     "title": "프론트엔드와 백엔드의 차이점은 뭘까? 웹개발이 목표라면 도움 될 기본 용어 정리!",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimage.yes24.com%2Fgoods%2F59148412%2FXL&type=a340 ",
     "link": "https://youtu.be/J6XW0MwZ7v0?si=-wmsbS6f_HNlD1o7",
     "source": "포마스쿨 온라인 YOUTUBE"
  },
  {
     "title": "언어 학습을 시작하기 전에 알아두면 좋은 언어를 배우는 원칙",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTAyMTJfMTI4%2FMDAxNTQ5OTU0NjQzMDk4.FGa_QjRenIPnb3OsTPK7Jl8Vn-cwAIqsexOahO2HVkog.RUr5O8iZTeurNql0zdUSlK_0bLPE2pc1a3ulT226C6cg.JPEG.woorikangsan%2Fdepositphotos_99596028-stock-illustration-italian-language-foreign.jpg&type=a340",
     "link": "https://youtu.be/jXEf5t1w5ow?si=VWhuiqxqXGRs9aOq",
     "source": "런던쌤 YOUTUBE"
  },
  {
     "title": "영문학과 진학을 준비한다고? 생활기록부 추천 도서 모음집 보고 가!",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMTJfMzcg%2FMDAxNjEwMzgxMTEyNTA0.DfJgUy1qxKtJazn7aEyJb9ZFkzx_WJN0mmTYX8DmUbsg.FhuwWtvsF6nuYjEBVXVhvqhBN9iYayfGnvpvPVfq_yMg.PNG.ministory000%2F%25BE%25EE%25B9%25AE%25C7%25D0%25B0%25FA_%25C3%25DF%25C3%25B5%25B5%25B5%25BC%25AD_1_%25281%2529.png&type=a340",
     "link": "https://blog.naver.com/ministory000/222204458824",
     "source": "ministory Blog"
  },
  {
     "title": "러시아어를 처음 공부하는 사람들을 위한 러시아 알파벳 발음과 필기 무료 강의!",
     "image_url": "https://search.pstatic.net/common?type=o&size=108x81&quality=75&direct=true&src=http%3A%2F%2Fdbscthumb.phinf.naver.net%2F1230_000_1%2F20120625174548414_KS3EO8MB0.png%2F163_p.png%3Ftype%3Dm1500",
     "link": "https://youtu.be/xzx0wT_xXsA?si=NesApffgTBkKZJW8",
     "source": "토르플 YOUTUBE"
  },
  {
     "title": "일본어 기초를 배우는 당신에게 추천하는 10시간만에 일본어 기초 익히기 강좌",
     "image_url": "https://search.pstatic.net/common?type=o&size=108x81&quality=75&direct=true&src=http%3A%2F%2Fdbscthumb.phinf.naver.net%2F1230_000_1%2F20120625174554812_TWE08D1Y3.png%2F194_p.png%3Ftype%3Dm1500",
     "link": "https://youtu.be/5CKhoIKiQcA?si=xDXdAkL7CM6p_qKd",
     "source": "유하 YOUTUBE"
  },
  {
     "title": "발음부터 반복해서 익혀보는 기본 중국어 300 단어 모음",
     "image_url": "https://i.ytimg.com/vi/k5Jq4OkV9b0/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAvdO9cMAimMZPSgkS8lwijXWlaZg",
     "link": "https://youtu.be/k5Jq4OkV9b0?si=nMRueMjjjYzpXcsO",
     "source": "중국어 다락원119 YOUTUBE"
  },
  {
     "title": "어문 계열 진학 희망 학생들을 위한 생활기록부 추천 도서 모음!",
     "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_3244103%2F32441033318.20230919125555.jpg&type=w216",
     "link": "https://happythings200.tistory.com/entry/%EC%83%9D%EA%B8%B0%EB%B6%80-%EB%8F%85%EC%84%9C%ED%99%9C%EB%8F%99%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%A7%84%EB%A1%9C-%ED%95%99%EA%B3%BC%EB%B3%84-%EC%B6%94%EC%B2%9C%EB%8F%84%EC%84%9C2-%EC%96%B4%EB%AC%B8%EA%B3%84%EC%97%B4",
     "source": "마더짱짱 님"
  },
  {
     "title": "세계에서 많이 쓰이는 언어의 순위와 특징은 뭘까?",
     "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2087_000_1%2F20130828202736993_D6COF9M7M.jpg%2Fnhn1_43_i1_m.jpg%3Ftype%3Dw450_fst%23450x407%23c407&type=f208_208",
     "link": "https://ccgv.tistory.com/entry/%EC%96%B8%EC%96%B4%EC%88%9C%EC%9C%84",
     "source": "ccgv tistory"
  },
  {
     "title": "초보도 외국어를 빠르게 익힐 수 있는 방법?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNjEyMjJfODMg%2FMDAxNDgyMzgyMDE4Nzkz.89gc8SIcxVGmpuVMFHp-l3eHy_k4Btgw3XEux8D4GWsg.rPfoX2SaDR5jwcYG8RNDxo3gDSqjsk1RJ8SPn_DeVl8g.JPEG%2FI_nyXoBJIKqbugYlFkhzR4G6NnJ8.jpg&type=a340",
     "link": "https://youtu.be/4PIKRu1H7fQ?si=GDP63gsflBdWeety",
     "source": "존쌤의언어습득법 YOUTUBE"
  },
  {
     "title": "러시아언어문화학과에 대한 여러 소문을 알아보자!",
     "image_url": "https://i.ytimg.com/vi/bnWNY7UaaoI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB0ZhFsFKaitVDo8sG_S5vjKsVluQ",
     "link": "https://youtu.be/bnWNY7UaaoI?si=x6ecFlcMVuN1_eJ7",
     "source": "충북대학교 교육방송국 CUBS"
  },
  {
     "title": "4개의 언어를 쓰는 나라, 스위스? 어떤 언어를 쓰는지 자세히 알아보자",
     "image_url": "https://search.pstatic.net/common?type=o&size=108x81&quality=75&direct=true&src=http%3A%2F%2Fdbscthumb.phinf.naver.net%2F1230_000_1%2F20120702113301741_JNOA37WIZ.png%2F171_p.png%3Ftype%3Dm1500",
     "link": "https://youtu.be/E72enEAMJeY?si=bNjCScDwFnnBRqTr",
     "source": "스위스청년 YOUTUBE"
  },
  {
     "title": "영문학과 학생들과 직접 이야기를 나눠보았다.",
     "image_url": "https://i.ytimg.com/vi/fOBJvDn1hjo/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDcIPU-m3dHaDMM3-zHr9TumCgvFQ",
     "link": "https://youtu.be/fOBJvDn1hjo?si=MqUKfTpCMsiBv0MW",
     "source": "Floresco 님"
  },
  {
     "title": "간호학과 진학을 목표로 하는 학생들을 위한 추천 도서 목록",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMDRfMjY1%2FMDAxNjA5NzY1MjcxMjE5.dojHcy6ir22eP1gs6r8hx-xmiVppkJUZ6HGMt3x66ocg.IvYUunJrawJzkMk93SABdQb_oU8p0YPQa6DR9dsL8JYg.JPEG.hks627%2Fx9791196443146.jpg&type=a340",
     "link": "https://post.naver.com/viewer/postView.naver?volumeNo=36268525&memberNo=37155911&vType=VERTICAL",
     "source": "나도코딩 YOUTUBE"
  },
  {
     "title": "드라마를 통해 쉽게 배우는 의학용어! (Feat. 낭만닥터 김사부)",
     "image_url": "https://i.ytimg.com/vi/0mUyJ58fH0M/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCAvH3gqRBNt27vDCdIs6TYmoHo4g",
     "link": "https://www.youtube.com/watch?v=0mUyJ58fH0M",
     "source": "진리Day YOUTUBE"
  },
  {
     "title": "간호학과 학생이라면 반드시 숙지하고 있어야 할 케이스 작성법",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fd2v80xjmx68n4w.cloudfront.net%2Fgigs%2FJ9IO01650892275.jpg&type=a340",
     "link": "https://www.instagram.com/p/CqciJCfr0tH/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==",
     "source": "간호사 대표모임 간준모"
  },
  {
     "title": "간호학과 졸업생이 알려주는 실습 시 도움이 될 조언 10가지.",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MDdfMTUz%2FMDAxNjQ5MzE1MjY3OTA5.1dyQtcC4BEMcOna9DsjWoyMbdd2qb3yM0BpczPdreYwg.wLhN2MdWtLxOfVPH_kWTRu7KSC2GGQbGj7WH5kPg4Nsg.JPEG.chomchom64%2FIMG_2207.JPG&type=sc960_832",
     "link": "https://youtu.be/gmxgsWfv47w?si=CrjtjgI8BsqxRICO",
     "source": "요조숙녀 두팔짱 YOUTUBE"
  },
  {
     "title": "의대 진학이 목적이라면 이 책은 읽어봐야지! 서울대학교 의과대학 추천 도서",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA5MTJfNzEg%2FMDAxNjk0NTA0MTg3Njk1.r2XENHguDHEHZqbmsga2sMETcGWBVoA3_XDP9Q1X1b0g.DHKHXirgURXLF8EigD9oFn6q3aCqoyB7BbSo0iKW8Lgg.JPEG.lorain0331%2FIMG_3419.jpg&type=sc960_832",
     "link": "https://bakul.tistory.com/entry/%EC%9D%98%EA%B3%BC%EB%8C%80%ED%95%99-%ED%95%84%EB%8F%85%EC%84%9C-%EB%8C%80%ED%95%99-%EC%A0%84%EA%B3%B5%EB%B3%84-%EC%B6%94%EC%B2%9C%EB%8F%84%EC%84%9C%EC%84%9C%EC%9A%B8%EB%8C%80-%EC%9D%98%EA%B3%BC%EB%8C%80%ED%95%99",
     "source": "완전꿀정보 님"
  },
  {
     "title": "악성민원에 소아과 떠나는 의료진들",
     "image_url": "https://i.ytimg.com/vi/IzB48A5Sj38/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBS-qBfr4xAOpwMJmI_2epfuQMvGw",
     "link": "https://youtu.be/IzB48A5Sj38?si=3lPT0wpPcT74gdzK",
     "source": "SBS News"
  },
  {
     "title": "간호학과 편입 기초 가이드 2024 ver.",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2Ff6%2Fa0%2F2a%2Ff6a02af339a4cf323c9dc487f92e91e9.jpg&type=a340",
     "link": "https://youtu.be/FMeq-pSlIDA?si=3KkZGoWrkNR-Qnf_",
     "source": "진프로의 학점관리 YOUTUBE"
  },
  {
     "title": "면접을 준비하는 간호사를 위한 면접 질문 리스트!",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA1MTRfMjQg%2FMDAxNTg5NDIzODIwMDA4.aPYcYUtlumw3PgA-e04zl8DfDoH53T--UInLGEuK2csg.VBvm4chD3TEItgHIiO2RieeKJq_92b7lb6DPURjVoNcg.JPEG.hogam47%2F%25B0%25A3%25C8%25A3%25BB%25E7-01.jpg&type=sc960_832",
     "link": "https://blog.naver.com/hogam47/221962079139",
     "source": "스튜디오 호감 Blog"
  },
  {
     "title": "어렵다는 해부학 기초 용어를 쉽게 외워보자!",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150315_179%2Fhappycall222_1426410420736zaKry_JPEG%2F%25BF%25EE%25B5%25BF20140509_1251349.jpg&type=sc960_832",
     "link": "https://youtu.be/uvXflfq8BK8?si=4riK5Oyd1tfhtMRD",
     "source": "의학용어 톡톡 YOUTUBE"
  },
  {
     "title": "간호사 면접을 AI 면접으로 본다는데? AI 면접은 어떻게 준비해야 할까?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MjhfMzMg%2FMDAxNjg1MjY2OTk5OTA1.lE6RSXpa7NBoWnyggGuA9LANKNgrGYZ-w4hVe9A-XPsg.iU_KAhNLyNLOCtBNH4LgDnskwTsqN-2V_iOi1PhewkYg.PNG.men_nurse%2Fimage.png&type=a340",
     "link": "https://blog.naver.com/nursecoach_/223113984318",
     "source": "간코치 Blog"
  },
  {
     "title": "간호사 취업 준비 시 가장 먼저 준비해야 할 것들이 있다?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA3MjJfMjky%2FMDAxNjU4NDc2OTYxNTg0.p2RcKS8sDP7HUdTIr4OL4mf7mIe_7H79iUH-lKcXrJ4g.gg9X10d7Rljh5Jxhknc448PpolWm9UISujrbPVaTTzAg.PNG.dreamnurse7%2F%25BA%25ED%25B7%25CE%25B1%25D7_%25C5%25DB%25C7%25C3%25B8%25B41.png&type=a340",
     "link": "https://blog.naver.com/dreamnurse7/222824525870",
     "source": "드림널스 Blog"
  },
  {
     "title": "부러진 뼈를 재생한다는 생체 바이오 잉크? 한 번 알아보자",
     "image_url": "https://i.ytimg.com/vi/JVZF6gc2zTo/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBNalUIJRhO07s0zE6vbuZXPj87Vg",
     "link": "https://youtu.be/JVZF6gc2zTo?si=Ihc6EOne0mldhAPg",
     "source": "SBS News"
  },
  {
     "title": "간호학과 편입 준비한다고?, 편입생이 알려주는 경험담 한 번 듣고 가는 건 어때?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MjFfMzUg%2FMDAxNjIxNjAwMTc4MDIy.RuHHG0xbkQStNG-Um3gxQYKkRZadbf_DOpkdgZHS92gg.zaPRsXR0L00Z9P3AjDnOkxFdSmsV0HoKgqND1yrj9SIg.JPEG.q200p%2FFB%25A3%25DFIMG%25A3%25DF1621598598726.jpg&type=a340",
     "link": "https://youtu.be/JXWAydHvV_s?si=U3CM8xK6KH2Zug-Z",
     "source": "앵뚜 YOUTUBE"
  },
  {
     "title": "수의학과를 졸업한 수의사들을 인터뷰해봤다.",
     "image_url": "https://i.ytimg.com/vi/OrFqqbNE268/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCOLiXdOIZRH42P-PoS7LoaviJaaw",
     "link": "https://www.youtube.com/watch?v=OrFqqbNE268",
     "source": "동물의사 YOUTUBE"
  },
  {
     "title": "건강 생각해서 먹었는데 오히려 독이 된다는 영양제?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5090%2F2014%2F05%2F19%2F20140519103647650576_59_20140519104007.jpg&type=a340",
     "link": "https://youtu.be/_AK1_ydErr0?si=zCPg4ofSc2WCis7l",
     "source": "SBS News"
  },
  {
     "title": "산소는 왜 o가 아니라 o2일까? 화학 입문자를 위한 무료 강의!",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2F2c%2F17%2Fa0%2F2c17a08fd994e4c87e1fe76022ef8490.jpg&type=a340",
     "link": "https://youtu.be/Q5CxuacRUjw?si=TRkHgZ2L_7qDxdbP",
     "source": "성주단지 YOUTUBE"
  },
  {
     "title": "네이처, 초전도 물질 개발 논문 철회?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA4MTFfMjg4%2FMDAxNjkxNzIxNjYzOTUx.M65K7_CKIWpcf_k8Rm9SSgV8XfQbAFoiS9srisZ9p10g.O0en8qvr6H_Q5MvfWIQGFjWkteLxW_Xy_67dRFbCaaIg.PNG.pp335315%2Fimage.png&type=a340",
     "link": "https://www.yna.co.kr/view/AKR20231108004800072?input=1195m",
     "source": "연합뉴스, 고일환 기자"
  },
  {
     "title": "생명과학과와 생명공학과의 차이점은 무엇일까? 영상으로 쉽게 알아보자",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwww.abnewswire.com%2Fuploads%2F1692687959.jpeg&type=a340",
     "link": "https://youtu.be/qacIQluVzqw?si=RZBAcImARWHIFzmY",
     "source": "생공돌이 YOUTUBE"
  },
  {
     "title": "간단하게 정리하는 물리학1 역학과 관련된 공식들",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMDlfMTc2%2FMDAxNTczMjkwNjc3Mjgz.w_Iwn5nq1awSzRI5eI0HjFVBgyknk0GcR5wgRd5ovgIg.AU9hTzwMw3VGc9eB9pXD2Blkwn78PsC72TscfkZQsrsg.JPEG.galaxyenergy%2F1573289086396.jpg&type=a340",
     "link": "https://youtu.be/SGekEiOGipc?si=YKre662pualxeS2P",
     "source": "김광명의 물리세계 YOUTUBE"
  },
  {
     "title": "산화, 환원 반응을 활용해 만드는 신호등 실험!",
     "image_url": "https://i.ytimg.com/vi/T5_pCLapxmo/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBi7h8mkU0G-bitNgmi6jsga-4-YQ",
     "link": "https://youtu.be/T5_pCLapxmo?si=DvG6WUFwppwIq6eU",
     "source": "케미가 체질 YOUTUBE"
  },
  {
     "title": "최초의 바이러스는 어디에서 왔을까?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA5MTRfMjA3%2FMDAxNjk0NjY1Mjg5Nzc3._XaOqigjldy3mhjey7zAuf5uLbeUA0LF4MSvYfS3SBQg.H7h4gAwA6_gUuwFfAppFTtm_l9JxftXV-f3U_mpQwhIg.PNG.tuktakped1%2Fimage.png&type=sc960_832",
     "link": "https://youtu.be/v3y8WvbS-KE?si=bsk_fGuw_6QJso6K",
     "source": "과학드림 YOUTUBE"
  },
  {
     "title": "화학과와 화학공학과는 어떤 차이가 있을까?",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTAzMDRfMjEy%2FMDAxNTUxNjI5NjQ2OTY1.AuCKKj30lxOlOmh7Ed9GPDLtnijzdIBqnNlRgM1nZhQg.b3m94CXR_XkeqMwcZF1uIvj546X9AsF93PR1Lyi8ObMg.JPEG.corning3%2F%25C8%25AD%25C7%25D09901.jpg&type=sc960_832",
     "link": "https://youtu.be/wpYU7RyW8cI?si=GNoloKVP5UEXTFtM",
     "source": "화학하악 YOUTUBE"
  },
  {
     "title": "물리학과 선배가 말하는 물리학과",
     "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2Fe9%2Ff2%2F8e%2Fe9f28e93605e7536cf186116afa975f8.jpg&type=a340",
     "link": "https://youtu.be/clR7dOO5MGs?si=jNGgfjbWH5yiG8-v",
     "source": "라이프코드 YOUTUBE"
  },
  {
     "title": "화학공학과 졸업자가 알려주는 화학공학과 졸업 후 진로!",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MDRfMjEy%2FMDAxNTk5MjAxMDgyMjY4.-3TKz8hGnX7RICj7h_vvYTVUcn7MCSsyuMBot3nCsL8g.8dDgqin0K0s7rEPVvAf-W5EX_7ytKMReupN1gYRVXTkg.JPEG.shrinkles%2F2020_07_%25C1%25F7%25BE%25F705_013_%25C8%25AD%25C7%25D0%25B0%25F8%25C7%25D0%25B1%25E2%25BC%25FA%25C0%25DA_.jpg&type=sc960_832",
     "link": "https://youtu.be/uimH7hicc3Y?si=RMKuEbXotIIW7eH5",
     "source": "주니 YOUTUBE"
  },
  {
     "title": "식물세포 DNA 추출 실험!",
     "image_url": "https://i.ytimg.com/vi/paY7HsClU7s/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAcNcsFbwnWnKYdqRfL-5RLpmJL8A",
     "link": "https://youtu.be/paY7HsClU7s?si=6tgpjUIkpvhbn2TF",
     "source": "한국생명공학연구소 YOUTUBE"
  },
  {
     "title": "침수식물도 광합성을 할 수 있을까? 실험을 통해 알아보자",
     "image_url": "https://i.ytimg.com/vi/BcFz0gGVuVU/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAtYUg4vwGX6jj725qfg14BJnnmHw",
     "link": "https://youtu.be/BcFz0gGVuVU?si=HnlDebUDEEnZP6a9",
     "source": "YTN science"
  },
  {
     "title": "나노 기술, 들어는 봤는데 제대로 모른다고? 이 영상으로 알려줄게!",
     "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5433%2F2016%2F12%2F26%2F0000002743_001_20161226112054365.jpg&type=a340",
     "link": "https://youtu.be/DPIPFj8ldq4?si=gEkSAt6-w65XN40E",
     "source": "안될과학 YOUTUBE"
  }
]


@bp.route('/')
def main_site():
   return render_template('main_cover.html')


@bp.route('/language')
def language_site():
   return render_template('language.html')


@bp.route('/science')
def science_site():
   return render_template('science.html')


@bp.route('/computer_engineering')
def ComputerEngineering_site():
   return render_template('ComputerEngineering.html')


@bp.route('/nursing')
def nursing_site():
   return render_template('nursing.html')


@bp.route('/search', methods=['GET', 'POST'])
def search():
   query = request.form.get('query')
   results = []
   if query:
      for item in data:
         if query.lower() in item['title'].lower():
            results.append(item)
   return render_template('search_results.html', results=results, query=query)