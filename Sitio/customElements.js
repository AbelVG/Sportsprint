const template = document.createElement('template');
this.innerHTML =
`<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<div class="menu">
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="Home.html">Inicio</a>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-controls="bs-example-navbar-collapse-1" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <div class="navbar-nav">
                        <a class="nav-item nav-link" href="Catalogo.html">Catálogo</a>
                        <a class="nav-item nav-link" href="QS.html">¿Quiénes somos?</a>
                    </div>
                </div>  
            </nav>
</div>`;


class menu extends HTMLElement{
    constructor(){
        super();


        this.attachShadow({mode: 'open'});

        this.shadowRoot.appendChild(template.content.cloneNode(true));
        
    }
    
}

customElements.define("menu-component", menu)