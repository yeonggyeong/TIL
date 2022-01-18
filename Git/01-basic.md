# GIT BASIC_01

> Git이란 소스코드를 효과적으로 관리하기 위해 개발된 **'분산형 버전 관리 시스템'** 입니다.

> Git을 통해서는 코드의 변경을 쉽게 확인이 가능하고, 특정 시점으로 돌아갈 수 있다. 


> Git이 관리하는 파일을 **repository** 라고 한다.

> Git은 원격 저장소와 로컬 저장소로 나눌 수 있다.
```
1. 원격 저장소 ( Remote Repository ) : 파일이 Git Server에서 관리되며, 다른 사람과의 공유가 가능하다.
2. 로컬 저장소 ( Local Repository ) : 개인 PC에 파일이 저장되는 개인 저장소이다.
```

---


Git을 사용하는 간단한 방법은 아래와 같다. 

### 1. 초기화 ( init )
 
 git으로 파일, 폴더를 관리하기 위해서는 해당 폴더를 생성하고 repository로 지정해줘야 한다. 

```
# 1) git으로 관리하기 위한 폴더 생성
$ mkdir new_project(폴더명)

# 2) git으로 관리하고 싶은 폴더로 이동
$ cd new_project

# 3) 폴더를 repository로 초기화
$ git init
```

### 2. 서명하기

자신이 한 commit이라는 것을 알리기 위해서 서명을 등록해야 한다.
```
# 1) 이름 등록하기
$ git config --global user.name '이름'
# 2) 메일 등록하기
$ git config --global user.email '메일주소' 
# 3) 서명 확인하기
$ git config --global user.name
$ git config --global user.email
```

3)에 나온 이름과 메일이 설정한 서명과 같다면 성공 !

### 3. 작업 저장하기

원격저장소에 파일의 버전을 올리기 위해서는 로컬 저장소에서 작업하던 작업물을 저장하고 commit 해야 한다.

```
# 1-1) 해당 파일을 스테이징 단계로 올리기
$ git add <filename>
# 1-2) 원하는 파일 여러 개를 스테이징 단계로 올리기
$ git add <filename> <filename>
# 1-3) 해당 위치에 있는 모든 파일을 스테이징 단계로 올리기
$ git add .
# 2) 스테이징 단계에서 내리기
$ git restore --staged <filename>

```

스테이징 단계로 올린 파일만 버전 생성 즉, commit이 가능하다.

따라서 add를 통해 원하는 파일을 스테이징 단계로 올려야한다.

다른 폴더에 있는 파일까지 스테이징 하기 위해서는 최상단 repository로 이동해야 한다.

> 버전 관리를 원하는 파일들을 경우에 따라 스테이징 단계로 올린다. 

```
# 2) commit 하기 (버전 만들기)
$ git commit -m '변경이유'
```
 -m '변경이유'를 생략할 수 있지만 버전관리를 위해서는 변경이유를 상세하게 적는 것이 좋다.

 ### 4) 상태 확인

 원격 저장소에 버전을 올리기 전 상태를 확인 할 수 있다.
 
 ```
 # 1) 저장 여부 확인
 $ git log
 # 2) commit 상태확인
 $ git status
 ```

 commit을 하기 위해서는 저장한 후에 생성해야 한다.

2)의 결과가 초록색이면 commit이 가능하고, 빨간색이면 commit이 불가능하다는 의미이다.

### 5) 원격저장소와 로컬저장소 연결

원격저장소에 저장하기 위해서는 원격 저장소와 로컬 저장소를 연결해야 한다.

```
# 1) 저장소 연결하기
$ git remote add origin <git주소>
# 2) 저장소 확인하기
$ git remote -v
```

> origin의 주소와 원하는 url의 주소가 동일하다면 성공 !

### 6) local repo -> remote repo ( push )

local repository에 저장해 놓은 commit을 remote repository로 push 해야 한다.
```
# push 하기
$ git push origin master
```

### 7) 원격 저장소 복제

원격 저장소에 있는 버전을 사용하기 위해서는 로컬 저장소로 복제해야 한다.
```
# 1) clone 하기
$ git clone <원격저장소url>
# 2) pull
$ git pull origin master
```

최초 복제를 한 후에는 pull 을 통해 버전 업데이트를 할 수 있다.

### 8) repository 해제하기

init으로 repository를 초기화한다면, rollback을 통해 git에서 파일 관리를 해제 할 수 있다.

```
# 1-1) rollback 하기
$ git rollback
# 1-2) 삭제하기
$ rm -rf .git/
```

### 9) Git Checklist

1. repository 안에 repository 생성하지 않기
2. home directory를 repository로 설정하지 않기
   

   




