#include <ESP8266WiFi.h>
#include <WiFiServer.h>

const char *ssid = "+FIBRATELECOM(IVO) 2.4G";
const char *password = "16019813";
// Set your Static IP address
IPAddress local_IP(192, 168, 1, 184);
// Set your Gateway IP address
IPAddress gateway(192, 168, 1, 1);

IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);   // optional
IPAddress secondaryDNS(8, 8, 4, 4); // optional

WiFiServer server(8266); // Cria servidor na porta 8266
WiFiClient client;       // Cria o objeto client

void handler(String message);
int led = 0; // Pino para comutar o relé
void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
    Serial.println("STA Failed to configure");
  }

  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.println("IP address: ");
  Serial.print(WiFi.localIP());

  // Inicia
  server.begin();

  pinMode(led, OUTPUT);
}

void loop() {
  if (client.connected()) {
    if (client.available() > 0) {
      String req = "";
      while (client.available() > 0) {
        char z = client.read();
        req += z;
      }
      Serial.print("O cliente ");
      Serial.print(client.remoteIP());
      Serial.print(" contatou o servidor ");
      Serial.print(WiFi.localIP());
      Serial.println(" com a seguinte mensagem: ");
      // Mensagem
      Serial.println(req);

      // Resposta
      client.print("O servidor ");
      client.print(client.remoteIP());
      client.print(" recebeu sua mensagem: ");
      // Mensagem
      client.println(req);

      handler(req);
    }
  } else {
    client = server.available();
    delay(1);
  }
}

void handler(String message) {
  if (message.indexOf("on") > 0)
    digitalWrite(led, HIGH);
  if (message.indexOf("off") > 0)
    digitalWrite(led, LOW);
}
