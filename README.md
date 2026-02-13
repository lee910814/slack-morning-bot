# 🌅 Slack Morning Bot

> 매일 아침 날씨, 뉴스, 할 일을 자동으로 알려주는 Slack 봇

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Slack](https://img.shields.io/badge/Slack-API-purple)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
  <img src="docs/demo.gif" alt="데모" width="600">
</p>

---

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [시작하기](#-시작하기)
- [사용 방법](#-사용-방법)
- [프로젝트 구조](#-프로젝트-구조)
- [배포](#-배포)
- [트러블슈팅](#-트러블슈팅)
- [향후 계획](#-향후-계획)
- [기여하기](#-기여하기)
- [라이센스](#-라이센스)
- [연락처](#-연락처)

---

## 🎯 프로젝트 소개

매일 아침 출근 전, 날씨 확인하고 뉴스 검색하는 시간이 아깝다고 느꼈습니다.
**"이거 자동화하면 어떨까?"** 하는 생각에서 시작한 프로젝트입니다.

### 해결한 문제
- ❌ 매일 아침 여러 앱을 확인하는 번거로움
- ❌ 중요한 뉴스를 놓치는 일
- ❌ 팀원들과 정보 공유의 어려움

### 솔루션
- ✅ 매일 정해진 시간에 자동으로 정보 수집
- ✅ Slack 하나로 모든 정보 확인
- ✅ 팀 전체가 동일한 정보 공유

### 개발 기간 & 인원
- **기간**: 2026.02.13 ~ 2026.02.13(기능 확장 예정)
- **인원**: 1명 (개인 프로젝트)
- **목적**: 포트폴리오 & 실제 사용

---

## ✨ 주요 기능

### 1. 🌤 실시간 날씨 정보
- OpenWeather API를 통한 현재 날씨
- 기온, 체감온도, 날씨 상태
- 습도 정보

### 2. 📰 주요 뉴스 요약
- Google News RSS 기반 뉴스 수집
- 카테고리별 자동 분류 (정치/경제/사회)
- 중복 뉴스 제거 알고리즘

### 3. ✅ 오늘의 할 일
- 일정 관리 및 리마인더
- 팀원 공통 일정 공유

### 4. ⏰ 완전 자동화
- GitHub Actions 기반 서버리스 실행
- 매일 정해진 시간 자동 발송
- 컴퓨터 꺼져도 작동

---

## 🛠 기술 스택

### Language & Framework
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)

### APIs & Libraries
- **Slack SDK** `3.27.1` - Slack 메시지 전송
- **feedparser** `6.0.10` - RSS 뉴스 파싱
- **requests** `2.31.0` - HTTP 통신
- **python-dotenv** `1.0.1` - 환경변수 관리

### External APIs
- **Slack API** - 메시지 전송
- **OpenWeather API** - 날씨 정보
- **Google News RSS** - 뉴스 수집

### DevOps & CI/CD
- **GitHub Actions** - 서버리스 자동 실행
- **Git & GitHub** - 버전 관리

### Development Tools
- **VS Code** - 개발 환경
- **Git** - 버전 관리

---

## 🚀 시작하기

### 사전 요구사항
```bash
