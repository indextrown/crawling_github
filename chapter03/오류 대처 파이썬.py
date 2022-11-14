# headers={'user-agent':'Mozila/5.0'} 봇으로 접근 가능하게 함
# 클릭하다보면 element click intercepted 에러가 발생해요
# javascript로 클릭을 직접 하도록 만들어주면 됩니다.
# driver.execute_script("arguments[0].click();", image)