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

void setup(void) {
  Serial.begin(9600);
  Serial.println("Leitor NFC!\nAlterações no código por Aline Bravin Prasser");
  nfc.begin();
}

void loop(void) {
  Serial.println("\nAproxime uma tag NFC ao leitor.\n");

  if (nfc.tagPresent())
  {
    NfcTag tag = nfc.read();
    Serial.println(tag.getTagType());
    Serial.print("UID: ");Serial.println(tag.getUidString());

    if (tag.hasNdefMessage()) // caso a tag não tenha uma mensagem gravada
    {

      NdefMessage message = tag.getNdefMessage();
      Serial.print("\nMensagem desta tag: ");
      Serial.print(message.getRecordCount());
      Serial.print(" Mensagem");
      if (message.getRecordCount() != 1) {
        Serial.print("(s)");
      }
      Serial.println(".");

      // loop entre as mensagens, imprimindo cada uma delas
      int recordCount = message.getRecordCount();
      for (int i = 0; i < recordCount; i++)
      {
        Serial.print("\nMensagem gravada na tag: ");Serial.println(i+1);
        NdefRecord record = message.getRecord(i);

        Serial.print("  TNF: ");Serial.println(record.getTnf());
        Serial.print("  Tipo: ");Serial.println(record.getType()); // será "" para TNF_EMPTY

        int payloadLength = record.getPayloadLength();
        byte payload[payloadLength];
        record.getPayload(payload);

        Serial.print("  Payload (HEX): ");
        PrintHexChar(payload, payloadLength);

        String payloadAsString = "";
        for (int c = 0; c < payloadLength; c++) {
          payloadAsString += (char)payload[c];
        }
        Serial.print("  Payload (as String): ");
        Serial.println(payloadAsString);

        String uid = record.getId();
        if (uid != "") {
          Serial.print("  ID: ");Serial.println(uid);
        }
      }
    }
  }
  delay(3000);
}
