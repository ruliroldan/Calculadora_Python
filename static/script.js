// static/script.js
function calcularEdad() {
    var añoNacimiento = document.getElementById('año_nacimiento').value;
    var añoActual = new Date().getFullYear();
    var edad = añoActual - añoNacimiento;

    document.getElementById('edadResultado').textContent = `Tienes ${edad} años.`;
    document.getElementById('resultado').classList.remove('hidden');
}