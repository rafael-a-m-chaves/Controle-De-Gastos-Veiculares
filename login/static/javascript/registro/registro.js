function exibirOcultar(val){
    var propietario = document.getElementById('propietario');
    var empresa = document.getElementById('empresa');
    var user = document.getElementById('user');
    var password = document.getElementById('password');
    var email = document.getElementById('email');
    var salvar = document.getElementById('salvar');

        

        if(val.value === "TRUE"){
            $(empresa).hide();
            $(user).hide();
            $(password).hide();
            $(email).hide();
            $(salvar).hide();
            $(propietario).show();
        }
        else{
            $(empresa).show();
            $(user).show();
            $(password).show();
            $(email).show();
            $(salvar).show();
            $(propietario).hide();
        }
    };