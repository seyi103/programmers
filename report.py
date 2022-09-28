from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    #중복 제거
    report = list(set(report))
    #각 사용자마다 신고한 아이디 저장
    user = defaultdict(set)
    #사용자마다 신고당한 횟수 저장
    count = defaultdict(int)
    
    for i in report:
        #report의 첫 원소는 이용자id, 두번쨰는 신고한 id
        uid, rid = i.split()
        # 신고자가 신고한 id 추가
        user[uid].add(rid)
        # 신고당한 id의 신고 횟수 추가
        count[rid] += 1
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if count[u]>=k:
                result +=1
        answer.append(result)
    return answer