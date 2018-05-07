#if 1
#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);
#else 0

#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
#endif

void setup() {
      Serial.begin(9600);
      Serial.println("Escreva em uma tag NFC!\nAlterações no código por Aline Bravin Prasser");
      nfc.begin();
}

void loop() {
    Serial.println("\nAproxime uma tag NFC do leitor!");
    if (nfc.tagPresent()) {
        NdefMessage message = NdefMessage();
        message.addUriRecord(" "); //INSIRA DENTRO DAS ASPAS A MENSAGEM QUE DESEJA GRAVAR!

        bool success = nfc.write(message);
        if (success) {
          Serial.println("Mensagem gravada com sucesso!");        
        } else {
          Serial.println("Erro ao inserir mensagem.");
        }
    }
    delay(5000);
}
