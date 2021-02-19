


function sign_up(){
    location.href = '/account/signup'
}

function home(){
    location.href = '/../..'
}

function login(){
    location.href = '/account/login'
}

function main(){
    location.href = '/bbs/main'
}

function group_del_member(user_id) {
    let result = confirm('정말 삭제할까요?')
    if (result) {
        location.href = '/group/group_del_member/' + user_id+ '/'
    }
}